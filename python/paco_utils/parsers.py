"""
Panda Paco Utils

Copyright 2022-2023 Kerby Keith Aquino; MIT license
"""
import json
from datetime import datetime
from os import path

from bs4 import BeautifulSoup, Tag

from paco_utils.base import soup_req, get_ua, update_json
from paco_utils.constants import BASE_FA, BASE_WS, BASE_IB, current_date
from paco_utils.logger import info, success, warn

url_error = 'Invalid URL. Expected URLs from either FurAffinity, Weasyl, and InkBunny only!'

metadata: dict[str, int] = {
	'pages': 1,
	'artworks': 0,
}


def time_difference(date_input: datetime) -> str:
	delta = (current_date - date_input)

	def fill_zeros(n: int) -> str:
		if n < 10:
			return f"0{n}"

		return str(n)

	seconds = fill_zeros(delta.seconds % 60)
	minutes = fill_zeros(delta.seconds // 60 % 60)
	hours = fill_zeros(delta.seconds // 3600)

	return f"{hours}h {minutes}m {seconds}s"


class IterateGallery:
	def __init__(self, url: str):
		"""Iterate over gallery pages

		:param url: Requires a gallery page for it to iterate over with
		"""
		self._is_furaffinity: bool = url.startswith(BASE_FA)
		self._is_weasyl: bool = url.startswith(BASE_WS)
		self._is_inkbunny: bool = url.startswith(BASE_IB)

		fn_fa_cache = "fa-pages-cache.json"

		if not self._is_furaffinity and not self._is_weasyl and not self._is_inkbunny:
			raise ValueError(url_error)

		if self._is_furaffinity:
			"""
			Check if the cached JSON file exists, otherwise, start snooping available
			pages then generate cached results
			"""
			if path.isfile(fn_fa_cache):
				success("Cache file found. Cached data has been applied.")

				with open(fn_fa_cache, "r") as f:
					cached_logs = json.load(f).get('logs')

					metadata.update(
						pages=cached_logs.get('pages'),
						artworks=cached_logs.get('artworks')
					)

					cached_date = datetime.strptime(cached_logs.get('cached_date'), "%Y-%m-%dT%H:%M:%S.%f")

					is_week_passed = (current_date - cached_date).days == 7

					cache_time_computed = time_difference(cached_date)
					info(f"Time since cached results: {cache_time_computed}\n")

					if not is_week_passed:
						info("A week hasn't passed yet. If it does, it will update the cache.")
					"""
					Return if a week as passed and overwrite and update the cache data 
					"""
					if is_week_passed:
						return

				return

			if not path.isfile(fn_fa_cache):
				warn("No cached file found, generating one...")

			next_btn_selector = ".submission-list:first-child .inline:nth-child(3)"
			gallery_items_selector = 'figure'

			# Paw-n intended
			p, aw = metadata.get('pages'), metadata.get('artworks')

			"""
			Loop through every page available via pagination, then break
			the loop if the "Next" button isn't available
			"""
			while True:
				gallery_page = soup_req(f"{url}{p}/")

				next_btn = gallery_page.select(next_btn_selector)[0]
				next_btn = next_btn.find('button')

				items = gallery_page.find_all(gallery_items_selector)

				info(f"Found so far: {p} pages, {aw} artworks")

				p += 1
				aw += len(items)

				if next_btn is None:
					success(f"{p} pages found! Along with the total of {aw} artworks counted")

					metadata.update(pages=p, artworks=aw)
					info("Saving to cache...")

					save_to_cache = {
						"cached_date": current_date.isoformat(),
						**metadata
					}

					update_json(fn_fa_cache, save_to_cache, time_series=False)
					break
			return

		if self._is_weasyl:
			gallery_page = soup_req(url, get_ua(BASE_WS))
			return

		if self._is_inkbunny:
			gallery_page = soup_req(url, get_ua(BASE_IB))
			return

	def page_iterator(self):
		pass


class SubmissionParser:
	title: str | None
	description: str | None
	img: str | None
	tags: list[str] | None
	date: datetime | None
	date_difference: str | None

	def __init__(self, url: str | None = None):
		"""Parses artworks' information from FurAffinity, Weasyl, and InkBunny

		:param url: It requires a URL to give you the good stuff
		"""
		self._art_page: BeautifulSoup | None = None

		self._is_furaffinity: bool = url.startswith(BASE_FA)
		self._is_weasyl: bool = url.startswith(BASE_WS)
		self._is_inkbunny: bool = url.startswith(BASE_IB)

		self._json_contents = None

		if not self._is_furaffinity and not self._is_weasyl and not self._is_inkbunny:
			raise ValueError(url_error)

		if self._is_furaffinity:
			self._art_page = soup_req(url, get_ua(BASE_FA))

		if self._is_weasyl:
			self._art_page = soup_req(url, get_ua(BASE_WS))

		if self._is_inkbunny:
			self._art_page = soup_req(url, get_ua(BASE_IB))

		self._fa_contents: Tag | None = self._art_page.select_one(".submission-content section")
		self._date: datetime | str | None = None

		# We pass dates here, so we can calculate the difference here for the updater
		if self._is_furaffinity:
			fa_date = self._fa_contents.select_one("span.popup_date")['title']
			self._date = datetime.strptime(fa_date, "%b %d, %Y %H:%M %p")

		if self._is_weasyl:
			pass

		if self._is_inkbunny:
			pass

	def __getattr__(self, item):
		if item == "title":
			if self._is_furaffinity:
				fa_title = self._fa_contents.find(class_="submission-title").text.strip()
				return fa_title

			if self._is_weasyl:
				return

			if self._is_inkbunny:
				return

		if item == "img":
			if self._is_furaffinity:
				fa_img = self._art_page.select_one("img#submissionImg")
				fa_img = f"https:{fa_img['data-fullview-src']}"
				return fa_img

			if self._is_weasyl:
				return

			if self._is_inkbunny:
				return

		if item == "description":
			if self._is_furaffinity:
				fa_desc = self._fa_contents.select_one(".submission-description")
				fa_desc = fa_desc.text.strip()
				return fa_desc

			if self._is_weasyl:
				return

			if self._is_inkbunny:
				return

		if item == "tags":
			tags_list: list[str] = []

			if self._is_furaffinity:
				tags_iterable = self._art_page.select("section.tags-row span.tags")
				for tag in tags_iterable:
					tags_list.append(tag.text)

				return tags_list

			if self._is_weasyl:
				return

			if self._is_inkbunny:
				return

		if item == "date":
			return self._date

		if item == "date_difference":
			if self._is_furaffinity:
				return

			if self._is_weasyl:
				return

			if self._is_inkbunny:
				return

	def from_json(self, file_path: str | None):
		with open(file_path, "r") as f:
			self._json_contents = json.load(f)
		
		return

	def characters(self):
		pass
