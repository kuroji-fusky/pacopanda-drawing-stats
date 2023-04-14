"""
P2DS - Web Scraper and Data Parsers
The brain of the operations

Copyright 2022-2023 Kerby Keith Aquino; MIT license
"""
import json
from datetime import datetime
from os import path
from typing import Optional, Union, Any

from bs4 import BeautifulSoup, Tag, ResultSet

from paco_utils.base import soup_req, get_ua, update_json, time_difference
from paco_utils.constants import BASE_FA, BASE_WS, BASE_IB, current_date
from paco_utils.exceptions import OperationConflictError, SpecificURLError
from paco_utils.logger import ColorLogger

cache_filename = "paco-cache.json"

logger = ColorLogger(prefix="Parsers")


class PacoBase:
	"""Base class for checking URLs"""
	page_metadata: dict[str, int] = {'pages': 1, 'artworks': 0}

	def __init__(self, url: str, json_fn: Optional[str] = None):
		if url and json_fn:
			raise OperationConflictError(
				"Both URL and JSON params are used - this will cause operation conflicts that will lead"
				" to confusion! Please pass either `url` or `json_fn` params only.")

		if url:
			self.is_fa: bool = url.startswith(BASE_FA)
			self.is_ws: bool = url.startswith(BASE_WS)
			self.is_ib: bool = url.startswith(BASE_IB)

			if not self.is_fa and not self.is_ws and not self.is_ib:
				raise SpecificURLError(
					'Invalid URL. Expected URLs from either FurAffinity, Weasyl, and InkBunny only!')

		if json_fn:
			logger.info("JSON param is passed, URL checks have been skipped.")

	def check_cache(self):
		"""
		Checks for any cached results usually in JSON format.
		"""
		if not path.isfile(cache_filename):
			logger.warn("No cached file found")

			# TODO rewrite json logic for prepending empty data
			# with open(cache_filename, "a", encoding='utf-8') as nf:
			# 	pre_populate = {
			# 		'last_checked': current_date.isoformat(),
			# 		'furaffinity': {},
			# 		'weasyl': {},
			# 		'inkbunny': {}
			# 	}
			# 
			# 	json.dump(pre_populate, nf)
			return

		with open(cache_filename, "r", encoding='utf-8') as f:
			logger.success("Cache file found. Cached data has been applied.")

			cached_logs = json.load(f).get('logs')
			self.page_metadata.update(pages=cached_logs.get('pages'), artworks=cached_logs.get('artworks'))

			cached_date = datetime.strptime(cached_logs.get('last_checked'), "%Y-%m-%dT%H:%M:%S.%f")

			is_week_passed = (current_date - cached_date).days == 7

			cache_time_computed = time_difference(cached_date)
			logger.info(f"Time since cached results: {cache_time_computed}\n")

			if not is_week_passed:
				logger.info("A week hasn't passed yet. If it does, it will update the cache.")

			# Return if a week as passed and overwrite and update the cache data 
			if is_week_passed:
				return

		return


class IterateGallery(PacoBase):
	def __init__(self, url: str, json_fn: Optional[str] = None, bypass_cache: Optional[bool] = False):
		"""Iterate over gallery pages

		:param url: Requires a gallery page for it to iterate over with
		"""
		super().__init__(url, json_fn)

		iter_prefix_msg = "Iterating submissions from"

		if not bypass_cache:
			self.check_cache()

		if url or url and bypass_cache:
			if self.is_fa:
				logger.info(f"{iter_prefix_msg} FurAffinity")

				next_btn_selector = ".submission-list:first-child .inline:nth-child(3)"
				gallery_items_selector = 'figure'

				p: Optional[int] = self.page_metadata.get('pages')
				aw: Optional[int] = self.page_metadata.get('artworks')

				# FurAffinity and InkBunny uses index-based URL pagination, however but Weasyl doesn't,
				# as it uses query-based pagination

				# Loop through every page available via pagination
				while True:
					gallery_page = soup_req(f"{url}{p}/")
					next_btn = gallery_page.select(next_btn_selector)[0]
					next_btn = next_btn.find('button')

					items = gallery_page.find_all(gallery_items_selector)

					logger.info(f"Found so far: {p} pages, {aw} artworks")

					p += 1
					aw += len(items)

					if next_btn is None:
						logger.success(f"{p} pages found! Along with the total of {aw} artworks counted")

						self.page_metadata.update(pages=p, artworks=aw)
						logger.info("Saving to cache...")

						# TODO rewrite json logic for prepending empty data
						save_to_cache = {
							"last_checked": current_date.isoformat(),
							"fa": {**self.page_metadata}
						}

						update_json(cache_filename, save_to_cache, time_series=False)
						break
				return

			if self.is_ws:
				prev_query: str = ''

				logger.info(f"{iter_prefix_msg} Weasyl")

				gallery_page = soup_req(url, get_ua(BASE_WS))

				next_btn_selector = "a.button:last-child"
				gallery_items_selector = 'li.item'

				if prev_query is None:
					...

				p, aw = self.page_metadata.get('pages'), self.page_metadata.get('artworks')

				ws_next_link = gallery_page.select_one(next_btn_selector)

				# TODO filter the query after '?'
				prev_query = ws_next_link['href']

				return

			if self.is_ib:
				logger.info(f"{iter_prefix_msg} InkBunny")

				gallery_page = soup_req(url, get_ua(BASE_IB))
				return


class SubmissionParser(PacoBase):
	def __init__(self, url: str, json_fn: Optional[str] = None):
		"""Parses artworks' information from FurAffinity, Weasyl, and InkBunny

		:param url: It requires a URL to give you the good stuff
		"""
		super().__init__(url, json_fn)

		self._json_data = json_fn
		self._art_page: BeautifulSoup | None = None

		# TODO Skip these conditions if json method is called
		if url:
			if self.is_fa:
				self._art_page = soup_req(url, get_ua(BASE_FA))

			if self.is_ws:
				self._art_page = soup_req(url, get_ua(BASE_WS))

			if self.is_ib:
				self._art_page = soup_req(url, get_ua(BASE_IB))

			self._fa_contents: Tag = self._art_page.select_one(".submission-content section")
			self._date: datetime | str | None = None

			# We pass dates here, so we can calculate the difference here for the updater
			if self.is_fa:
				fa_date = self._fa_contents.select_one("span.popup_date")['title']
				self._date = datetime.strptime(fa_date, "%b %d, %Y %H:%M %p")

			if self.is_ws:
				pass

			if self.is_ib:
				pass

	@property
	def title(self):
		if self.is_fa:
			fa_title = self._fa_contents.find(class_="submission-title").text.strip()
			return fa_title

		if self.is_ws:
			return

		if self.is_ib:
			return

	# noinspection SpellCheckingInspection
	@property
	def img(self):
		if self.is_fa:
			fa_img = self._art_page.select_one("img#submissionImg")
			# noinspection SpellCheckingInspection
			fa_img = f"https:{fa_img['data-fullview-src']}"
			return fa_img

		if self.is_ws:
			return

		if self.is_ib:
			return

	@property
	def description(self):
		if self.is_fa:
			fa_desc = self._fa_contents.select_one(".submission-description")
			fa_desc = fa_desc.text.strip()
			return fa_desc

		if self.is_ws:
			return

		if self.is_ib:
			return

	@property
	def tags(self):
		tags_list: list[str] = []

		if self.is_fa:
			tags_iterable: Union[ResultSet[Tag], Any] = self._art_page.select("section.tags-row span.tags")
			for tag in tags_iterable:
				tags_list.append(tag.text)

			return tags_list

		if self.is_ws:
			return

		if self.is_ib:
			return

	@property
	def date(self):
		return self._date

	@property
	def date_difference(self):
		if self.is_fa:
			return

		if self.is_ws:
			return

		if self.is_ib:
			return

	def filter_characters(self):
		# TODO filter by ignored tags
		data = self._json_data

		pass

	def find_medium(self):
		data = self._json_data

		medium_type = ("Digital", "Traditional")
		# noinspection SpellCheckingInspection
		programs = ["Procreate", "Photoshop", "Medibang"]

		pass

	def find_tags(self):
		data = self._json_data
		collected_tags: list[str] = []

		pass
