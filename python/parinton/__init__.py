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
from parinton.logger import PacoLogger
from parinton.typings import _FixedBaseURLs, _FixedBaseArtwork, _CacheDictData
from parinton.utils import load_file, save_json

# from difflib import get_close_matches

BASE_URL: _FixedBaseURLs = {
    "furaffinity": "https://www.furaffinity.net",
    "weasyl": "https://www.weasyl.com",
    "inkbunny": "https://inkbunny.net"
}

logger = PacoLogger(time=True)


class Parinton:

    def __init__(self) -> None:
        self.redis_url: Optional[str] = None
        self.cached_data: Optional[_CacheDictData] = None

        self.bypass_cache: bool = False

    def load_config(self, bypass: Optional[bool] = False, production: Optional[bool] = False) -> None:
        """
        Loads a Redis URL based on its environment. Make sure you know what you're doing!
        
        :param bypass: Bypass the need to load the config
        :param production: A boolean whether to use the production environment
        :return: None
        """
        load_dotenv()

        _logger = "[ ⚙️ Redis Config ]"

        _DEV_URL = os.getenv('DEV_REDIS_URL')
        _PROD_URL = os.getenv('PROD_REDIS_URL')
        _REDIS_PROTOCOL = "redis://"

        if bypass:
            logger.log('info', "{} {}".format(_logger, 'Redis config bypassed'))
            return

        def _env_error(env_key):
            logger.log('error', "{} {}".format(_logger, 'Redis protocol not found!'))
            logger.log('info', "{} {}".format(_logger, 'NOTE:'))
            logger.log('info', "{} {}".format(_logger, f"If you're currently running tests or populating the cache file"
                                                       f", pass the '--bypass-config' to populate the cache locally."))
            raise EnvironmentValueError(f"Key '{env_key}' doesn't begin with '{_REDIS_PROTOCOL}'")

        if production and _PROD_URL is None:
            raise EnvironmentNotFound("Production mode enabled, but .env key 'PROD_REDIS_URL' isn't found!")

        if _DEV_URL is None:
            raise EnvironmentNotFound(".env key 'DEV_REDIS_URL' isn't found!")

        if not _DEV_URL.startswith(_REDIS_PROTOCOL):
            _env_error('DEV_REDIS_URL')

        if not _PROD_URL.startswith(_REDIS_PROTOCOL):
            _env_error('PROD_REDIS_URL')

        if production and _PROD_URL:
            self.redis_url = _PROD_URL

        if _DEV_URL:
            self.redis_url = _DEV_URL

    def check_cache(self, bypass: Optional[bool] = False):
        _logger = "[ ⚡ Cache Check ]"

        _cache_filename = "paco-cache.json"

        _current_dt = datetime.now()
        _cached_dt: Optional[_CacheDictData | str] = None
        _cached_time = "cached_time"

        _prepend_cache: _CacheDictData = {
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

        if bypass:
            self.bypass_cache = True
            logger.log('info', "{} {}".format(_logger, "Cache checker bypassed"))
            return

        try:
            logger.log('info', "{} {}".format(_logger, "Cache file found!"))
            self.cached_data = load_file(_cache_filename)

            _cached_dt = self.cached_data.get(_cached_time)

            _delta = _current_dt - datetime.fromisoformat(_cached_dt)
            _delta_week = _delta.days > 7

            if not _delta_week:
                logger.log('info', "{} {}".format(_logger, "A week hasn't passed yet, repurposing cached values"))
                logger.log('info', "{} {} {}".format(_logger, "Elapsed time:", _delta))

        except FileNotFoundError:
            logger.log('warn', "{} {}".format(_logger, "No cache file found, created file and loaded"))

            save_json(_prepend_cache, _cache_filename)

            self.cached_data = load_file(_cache_filename)

    @staticmethod
    def page_req(url: str) -> BeautifulSoup:
        """
        Sends an HTTP request and returns raw HTML markup
        
        :param url: A url required to make a request 
        :return: HTML output via BeautifulSoup
        """
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
