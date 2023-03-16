"""
Panda Paco Utils

Copyright 2022-2023 Kerby Keith Aquino; MIT license
"""
import json
from datetime import datetime
from os import path

from bs4 import BeautifulSoup, Tag

from paco_utils import soup_req, get_ua, update_json
from paco_utils.constants import BASE_FA, BASE_WS, BASE_IB, current_date
from paco_utils.logger import info, success, warn

url_error = 'Invalid URL, expected URLs from either FurAffinity, Weasyl, and InkBunny only!'

parser_metadata: dict[str, int] = {
	'pages': 1,
	'artworks': 0,
}


def time_difference(date_input: datetime):
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
		self.__is_furaffinity: bool = url.startswith(BASE_FA)
		self.__is_weasyl: bool = url.startswith(BASE_WS)
		self.__is_inkbunny: bool = url.startswith(BASE_IB)

		fn_fa_cache = "fa-pages-cache.json"

		if not self.__is_furaffinity and not self.__is_weasyl and not self.__is_inkbunny:
			raise ValueError(url_error)

		if self.__is_furaffinity:
			"""
			Check if the cached JSON file exists, otherwise, start snooping available
			pages then generate cached results
			"""
			if path.isfile(fn_fa_cache):
				success("Cache file has been found! Cached data applied!")

				with open(fn_fa_cache, "r") as f:
					cached_logs = json.load(f).get('logs')

					parser_metadata.update(
						pages=cached_logs.get('pages'),
						artworks=cached_logs.get('artworks')
					)

					cached_date = datetime.strptime(cached_logs.get('cached_date'), "%Y-%m-%dT%H:%M:%S.%f")
					is_week_passed = (current_date - cached_date).days == 7

					scared = time_difference(cached_date)
					info(f"Time since cached results: {scared}\n")

					if is_week_passed:
						return

				return

			if not path.isfile(fn_fa_cache):
				warn("No cached file found, generating one...")

			next_btn_selector = ".submission-list:first-child .inline:nth-child(3)"
			gallery_items_selector = 'figure'

			# Paw-n intended
			p, aw = parser_metadata.get('pages'), parser_metadata.get('artworks')

			while True:
				gallery_page = soup_req(f"{url}{p}/")

				next_btn = gallery_page.select(next_btn_selector)[0]
				next_btn = next_btn.find('button')

				if next_btn is None:
					success(f"{p} pages found! Along with the total of {aw} artworks counted")

					parser_metadata.update(pages=p, artworks=aw)
					info("Saving to cache...")

					save_to_cache = {
						"cached_date": current_date.isoformat(),
						**parser_metadata
					}

					update_json(fn_fa_cache, save_to_cache, time_series=False)
					break

				info(f"Found so far: {p} pages, {aw} artworks")

				items = gallery_page.find_all(gallery_items_selector)

				p += 1
				aw += len(items)

			return

		if self.__is_weasyl:
			gallery_page = soup_req(url, get_ua(BASE_WS))
			return

		if self.__is_inkbunny:
			gallery_page = soup_req(url, get_ua(BASE_IB))
			return


class SubmissionParser:
	title: str | None
	description: str | None
	img: str | None
	tags: list[str] | None
	date: datetime | None
	date_difference: str | None

	def __init__(self, url: str):
		"""Parses artworks' information from FurAffinity, Weasyl, and InkBunny

		:param url: It requires a URL to give you the good stuff
		"""
		self.__art_page: BeautifulSoup | None = None

		self.__is_furaffinity: bool = url.startswith(BASE_FA)
		self.__is_weasyl: bool = url.startswith(BASE_WS)
		self.__is_inkbunny: bool = url.startswith(BASE_IB)

		if not self.__is_furaffinity and not self.__is_weasyl and not self.__is_inkbunny:
			raise ValueError(url_error)

		if self.__is_furaffinity:
			self.__art_page = soup_req(url, get_ua(BASE_FA))

		if self.__is_weasyl:
			self.__art_page = soup_req(url, get_ua(BASE_WS))

		if self.__is_inkbunny:
			self.__art_page = soup_req(url, get_ua(BASE_IB))

		self.__fa_contents: Tag | None = self.__art_page.select_one(".submission-content section")
		self.__date: datetime | str | None = None

		# We pass dates here, so we can calculate the difference here for the updater
		if self.__is_furaffinity:
			fa_date = self.__fa_contents.select_one("span.popup_date")['title']
			self.__date = datetime.strptime(fa_date, "%b %d, %Y %H:%M %p")

		if self.__is_weasyl:
			pass

		if self.__is_inkbunny:
			pass

	def __getattr__(self, item):
		# Oh god my 'if' nesting game hella mad lol
		if item == "title":
			if self.__is_furaffinity:
				fa_title = self.__fa_contents.find(class_="submission-title").text.strip()
				return fa_title

			if self.__is_weasyl:
				return

			if self.__is_inkbunny:
				return

		if item == "img":
			if self.__is_furaffinity:
				fa_img = self.__art_page.select_one("img#submissionImg")
				fa_img = f"https:{fa_img['data-fullview-src']}"
				return fa_img

			if self.__is_weasyl:
				return

			if self.__is_inkbunny:
				return

		if item == "description":
			if self.__is_furaffinity:
				fa_desc = self.__fa_contents.select_one(".submission-description")
				fa_desc = fa_desc.text.strip()
				return fa_desc

			if self.__is_weasyl:
				return

			if self.__is_inkbunny:
				return

		if item == "tags":
			tags_list: list[str] = []

			if self.__is_furaffinity:
				tags_iterable = self.__art_page.select("section.tags-row span.tags")
				for tag in tags_iterable:
					tags_list.append(tag.text)

				return tags_list

			if self.__is_weasyl:
				return

			if self.__is_inkbunny:
				return

		if item == "date":
			return self.__date

		if item == "date_difference":
			if self.__is_furaffinity:
				return

			if self.__is_weasyl:
				return

			if self.__is_inkbunny:
				return
