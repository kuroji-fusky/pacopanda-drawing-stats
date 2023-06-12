"""
Parinton

Parinton Entry Point

Copyright 2021-2023 Kerby Keith Aquino
MIT License
"""

import json
from datetime import datetime
from typing import Optional
from difflib import get_close_matches

from bs4 import BeautifulSoup
from bs4.element import Tag
from requests import Session
from requests.exceptions import ConnectionError

from parinton.typings import _FixedBaseURLs, _ArtworkReturnType, _ArtworkDictType

BASE_URL: _FixedBaseURLs = {
	"furaffinity": "https://www.furaffinity.net",
	"weasyl": "https://www.weasyl.com",
	"inkbunny": "https://inkbunny.net"
}


def _load_file(f):
	with open(f, 'r') as fi:
		if f.endswith('.json'):
			return json.load(fi)

		return fi.read()


class Parinton:
	REDIS_URL: str | None = ''

	def load_config(self, fn: str):
		...

	@staticmethod
	def check_cache():
		_cache_filename = "paco-cache.json"

		_current_dt = datetime.now()
		_cached_dt: str | None = None
		_cached_time = "cached_time"

		_cache_dict: dict[str, str | _FixedBaseURLs] = {
			_cached_time: _current_dt.isoformat(),
			'pagination': {
				'furaffinity': '0',
				'weasyl': '0',
				'inkbunny': '0'
			}
		}

		try:
			_cached_dt: dict[str, str] = _load_file(_cache_filename)
			_cached_dt = _cached_dt.get(_cached_time)

			print(_cached_dt)

		except FileNotFoundError:
			print("No cache file found, creating one...")

			with open(_cache_filename, 'w') as fo:
				json.dump(_cache_dict, fo, ensure_ascii=True)

	@staticmethod
	def page_req(url: str):
		try:
			_req = Session().get(url, timeout=None)
			return BeautifulSoup(_req.text, "html.parser")

		except ConnectionError:
			raise ConnectionError


class PacoParser(Parinton):
	def __init__(self, url: Optional[str] | None) -> None:
		self._url = url
		self._description: Tag | None = None

	def get_art_metadata(self, selector: _ArtworkDictType) -> _ArtworkReturnType:
		"""
		Gets the page metadata from a page request
		
		:param selector: Requires a dict of CSS selectors for title, description, date, and iterable tags
		:return: An object that returns a title, description, date, and a list of tags
		"""
		title_selector = selector.get("title")
		desc_selector = selector.get("description")
		tags_selector = selector.get("tags")
		date_selector = selector.get("date")

		_page = self.page_req(self._url)
		_tags_list = [str(tag) for tag in _page.select(tags_selector)]

		self._description = _page.select_one(desc_selector)

		# TODO use param for getting the text attr
		return {
			"title": str(_page.select_one(title_selector)),
			"description": str(self._description),
			"date": str(_page.select_one(date_selector)),
			"tags": _tags_list
		}

	def parse_medium(self) -> None:
		"""
		There's a common pattern that in every artwork descriptions; he lists what tools
		and medium of the artwork (i.e. "Digital. Photoshop.")

		My approach is to go to the last lines of the description using .split('\n')
		and match mediums and whatever tools he uses
		"""
		# TODO do something with this crap
		_desc = self._description

		_MEDIUM = ['digital', 'traditional']

		# TODO use difflib.get_close_matches for this one
		_PROGRAMS = ['photoshop', 'medibang', 'procreate']
		_TRAD_TOOLS = ['gouaches', 'watercolors', 'colored pencils', 'markers', 'indian ink', 'pencils']

		_TOOLS = [*_PROGRAMS, *_TRAD_TOOLS]

		# TODO if nothing is detected, return "not specified"
		...
