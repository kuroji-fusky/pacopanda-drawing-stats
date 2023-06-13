"""
Parinton

Parinton Entry Point

Copyright 2021-2023 Kerby Keith Aquino
MIT License
"""

import json
import os
from datetime import datetime
from typing import Optional

from bs4 import BeautifulSoup
from dotenv import load_dotenv
from requests import Session
from requests.exceptions import ConnectionError

from parinton.exceptions import EnvironmentNotFound, EnvironmentValueError
from parinton.typings import _FixedBaseURLs, _FixedBaseArtwork

# from difflib import get_close_matches

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
	def __init__(self) -> None:
		self.REDIS_URL: str | None = None

	def load_config(self, bypass: Optional[bool] = False, production: Optional[bool] = False) -> None:
		"""
		Loads a Redis URL based on its environment. Make sure you know what you're doing!
		
		:param bypass: Bypass the need to load the config
		:param production: A boolean whether to use the production environment
		:return: None
		"""
		load_dotenv()

		_PROD_URL = os.getenv('PROD_REDIS_URL')
		_DEV_URL = os.getenv('DEV_REDIS_URL')
		_REDIS_PROTOCOL = "redis://"
		if bypass:
			return

		def _env_error(env_key):
			raise EnvironmentValueError(f"{env_key} doesn't begin with {_REDIS_PROTOCOL}")

		if production and _PROD_URL is None:
			raise EnvironmentNotFound("Production mode enabled, but .env key 'PROD_REDIS_URL' isn't found!")

		if _DEV_URL is None:
			raise EnvironmentNotFound(".env key 'DEV_REDIS_URL' isn't found!")

		if not _DEV_URL.startswith(_REDIS_PROTOCOL):
			_env_error('DEV_REDIS_URL')

		if not _PROD_URL.startswith(_REDIS_PROTOCOL):
			_env_error('PROD_REDIS_URL')

		if production and _PROD_URL:
			self.REDIS_URL = _PROD_URL

		if _DEV_URL:
			self.REDIS_URL = _DEV_URL

	@staticmethod
	def check_cache():
		_cache_filename = "paco-cache.json"

		_current_dt = datetime.now()
		_cached_dt: str | None = None
		_cached_time = "cached_time"

		_cache_dict: dict[str, str | _FixedBaseURLs | _FixedBaseArtwork] = {
			_cached_time: _current_dt.isoformat(),
			'pagination': {
				'furaffinity': '0',
				'weasyl': '0',
				'inkbunny': '0'
			},
			'data': {
				'furaffinity': [],
				'weasyl': [],
				'inkbunny': []
			}
		}

		try:
			_cached_dt: dict[str, str | dict[str, str]] = _load_file(_cache_filename)
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

	def get_paginated_pages(self, prev_selector: str, next_selector: str) -> int:
		"""
		Gets a number of all the iterated pages by providing its CSS selectors with the "Previous" and "Next" buttons,
		then stores it in cache

		Sites like FurAffinity and InkBunny uses a paginated system to iterate over
		user generated content.

		:param prev_selector: The CSS selector of a "Previous" button 
		:param next_selector: The CSS selector of a "Next" button 
		:return: A number of all the iterated pages
		"""
		...


paco = Parinton()
