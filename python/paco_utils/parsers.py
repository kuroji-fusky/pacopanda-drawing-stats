"""
Panda Paco Utils

Copyright 2022-2023 Kerby Keith Aquino; MIT license
"""
from datetime import datetime

from bs4 import BeautifulSoup, Tag

from paco_utils import gimme_soop, get_ua
from paco_utils.constants import BASE_FA, BASE_WS, BASE_IB

url_error = 'Invalid URL, expected URLs from either FurAffinity, Weasyl, and InkBunny only!'


class IterateGallery:
	def __init__(self, url: str, bypass_cache: bool | None = None):
		"""Iterate over gallery pages

		:param url: Requires a gallery page for it to iterate over with

		:param bypass_cache: In order to save large HTTP requests, all iterated
			pages will be saved in a JSON file, you can override this behavior if needed
		"""

		self.__url = url
		self.__iter_page: BeautifulSoup | None = None

		self.__metadata: dict[str, int] = {
			"pages": 1,
			"artworks": 0
		}

		self.__is_furaffinity: bool = self.__url.startswith(BASE_FA)
		self.__is_weasyl: bool = self.__url.startswith(BASE_WS)
		self.__is_inkbunny: bool = self.__url.startswith(BASE_IB)

		if not self.__is_furaffinity and not self.__is_weasyl and not self.__is_inkbunny:
			raise ValueError(url_error)

		if self.__is_furaffinity:
			self.__iter_page = gimme_soop(self.__url, get_ua(BASE_FA))

			mutate_url: str = "no"

			next_btn = self.__iter_page.select(".submission-list:first-child .inline:nth-child(3)")[0]
			next_btn_available = next_btn.find('button') is not None

		if self.__is_weasyl:
			self.__iter_page = gimme_soop(self.__url, get_ua(BASE_WS))

		if self.__is_inkbunny:
			self.__iter_page = gimme_soop(self.__url, get_ua(BASE_IB))


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

		self.__url = url
		self.__art_page: BeautifulSoup | None = None

		self.__is_furaffinity: bool = self.__url.startswith(BASE_FA)
		self.__is_weasyl: bool = self.__url.startswith(BASE_WS)
		self.__is_inkbunny: bool = self.__url.startswith(BASE_IB)

		if not self.__is_furaffinity and not self.__is_weasyl and not self.__is_inkbunny:
			raise ValueError(url_error)

		if self.__is_furaffinity:
			self.__art_page = gimme_soop(self.__url, get_ua(BASE_FA))

		if self.__is_weasyl:
			self.__art_page = gimme_soop(self.__url, get_ua(BASE_WS))

		if self.__is_inkbunny:
			self.__art_page = gimme_soop(self.__url, get_ua(BASE_IB))

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
