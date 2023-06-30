"""
## Parinton

Entry point for initialzing configs, parsers, and managing character data to the database

Copyright 2021-2023 Kerby Keith Aquino
MIT License
"""
import os
from datetime import datetime
from typing import Optional

from bs4 import Tag
from dotenv import load_dotenv

from parinton.exceptions import EnvironmentValueError, EnvironmentProductionError, EnvironmentNotFound
from parinton.logger import PacoLogger
from parinton.types import CachedData, FixedBaseURLs, BaseLiterals, ArtworkDictType, ArtworkReturnType, AverageDateReturnType
from parinton.utils import load_file, save_file, format_time, page_req

logger = PacoLogger(time=True)

OptBool = Optional[bool]

BASE_URL: FixedBaseURLs = {
    "furaffinity": "https://www.furaffinity.net",
    "weasyl": "https://www.weasyl.com",
    "inkbunny": "https://inkbunny.net"
}


class Parinton:
    def __init__(self) -> None:
        self.cache_filename = "paco-cache.json"

        self.redis_url: Optional[str] = None
        self.bypass_cache = False

    def bootstrap(self,
                  bypass_config: OptBool = False,
                  bypass_cache: OptBool = False,
                  production: OptBool = False) -> None:
        """
        An initalizer for checking the config and cache, this must be called first before anything else!

        :param bypass_config: Bypasses the config
        :param bypass_cache: Bypasses the cache file
        :param production: Points the config to production environment
        """
        self._load_config(bypass=bypass_config, production=production)
        self.check_cache(bypass=bypass_cache)

    def _load_config(self, bypass: OptBool = False, production: OptBool = False) -> None:
        """
        Loads a Redis URL based on its environment. Make sure you know what you're doing!

        :param bypass: Bypass the need to load the config
        :param production: A boolean whether to use the production environment
        :return: None
        """
        load_dotenv()

        _logger = "[ ⚙️ Redis Config ]"

        DEV_URL = os.getenv('DEV_REDIS_URL')
        PROD_URL = os.getenv('PROD_REDIS_URL')
        REDIS_PROTOCOL = "redis://"

        if bypass:
            logger.log('info', "{} {}".format(
                _logger, 'Redis config bypassed'))
            return

        def env_error(env_key):
            logger.log('error', "{} {}".format(
                _logger, 'Redis protocol not found!'))

            raise EnvironmentValueError(f"Key '{env_key}' doesn't begin with '{REDIS_PROTOCOL}'\n\n"
                                        "If you think this is a mistake, running tests, or populating the cache file, "
                                        "add the '--bypass-config' flag to populate the cache locally on your system."
                                        )

        if DEV_URL is None:
            raise EnvironmentNotFound(".env key 'DEV_REDIS_URL' isn't found!")

        if not DEV_URL.startswith(REDIS_PROTOCOL):
            env_error('DEV_REDIS_URL')

        if not PROD_URL.startswith(REDIS_PROTOCOL):
            env_error('PROD_REDIS_URL')

        if not production and PROD_URL:
            raise EnvironmentProductionError(".env key 'PROD_REDIS_URL' found, but running in a dev instead.",
                                             "Rerun the script with '--prod' flag!")

        if production and PROD_URL is None:
            raise EnvironmentNotFound(
                "Production mode enabled, but .env key 'PROD_REDIS_URL' isn't found!")

        if production and PROD_URL:
            self.redis_url = PROD_URL
            logger.log('success', "{} {}".format(
                _logger, 'Redis production environment loaded'))

        if DEV_URL:
            self.redis_url = DEV_URL
            logger.log('success', "{} {}".format(
                _logger, 'Redis dev environment loaded'))

    def check_cache(self, bypass: OptBool = False) -> None:
        """
        Checks for a cache file that consists of the creation date, paginated pages, and artwork metadata.

        This cache functionality is to save bulk requests every time the script is run (mostly for testing); otherwise
        sending too much traffic will cause it to get rate limited temporarily and I might not able to retrieve data.

        :param bypass: A boolean to either bypass cache checks
        """
        _logger = "[ ⚡ Cache Check ]"

        current_dt = datetime.now()

        prepend_data: CachedData = {
            'cached_time': current_dt.isoformat(),
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
            return

        try:
            logger.log('info', "{} {}".format(_logger, "Cache file found!"))
            cached_data = load_file(self.cache_filename)

            cached_dt = cached_data.get('cached_time')

            delta = current_dt - datetime.fromisoformat(cached_dt)
            delta_week = delta.days > 7

            if not delta_week:
                logger.log('info', "{} {}".format(
                    _logger, "A week hasn't passed yet, repurposing cached values"))
                logger.log('info',
                           "{} {} {}".format(_logger, "Elapsed time since cache creation:", format_time(delta)))
            else:
                ...

        except FileNotFoundError:
            logger.log('warn', "{} {}".format(
                _logger, "No cache file found, created file and loaded"))

            save_file(prepend_data, self.cache_filename)


class PacoArtParser(Parinton):
    def __init__(self) -> None:
        super().__init__()

        self._description: Tag | None = None

        self.__is_fa = self.__url_startswith('furaffinity')

    @staticmethod
    def __url_startswith(base: BaseLiterals):
        return BASE_URL[base]

    def iterate_paginated_pages(self, entry_url: str, next_selector: str) -> int:
        """
        Gets a number of all the iterated pages by providing its CSS selectors with the "Previous" and "Next" buttons,
        then stores it in cache

        :param entry_url: The beginning point for URL to paginate and iterate over
        :param next_selector: The CSS selector of a "Next" button 
        :return: A number of all the iterated pages
        """
        _logger = "[ 🔁 Iterator ]"

        iterated_pages: Optional[str | int] = 0
        cached_data: Optional[CachedData] = None

        if not self.bypass_cache:
            cached_data = load_file(self.cache_filename)['pagination']

        if self.__is_fa:
            if not self.bypass_cache and cached_data.get('furaffinity') == '0':
                print('This must be a recently created cache')

            logger.log('info', "{} {}".format(
                _logger, "Iterating gallery pages from FurAffinity"))

        if self.__url_startswith('weasyl'):
            # TODO replace the 'iterated_pages' with a query to iterate over
            ...

        while True:
            if self.__url_startswith('furaffinity') and self.__url_startswith('inkbunny'):
                iterate_url = f'{entry_url}{iterated_pages}/?'
                next_button = page_req(iterate_url).select_one(next_selector)

                iterated_pages += 1
                final_iter_pages = iterated_pages - 1

                print("{} {} {}".format(
                    _logger, 'Iterated pages so far:', final_iter_pages))

                if not next_button:
                    return final_iter_pages

            if self.__url_startswith('weasyl'):
                ...

    def get_art_metadata(self, url: str, selector: ArtworkDictType) -> ArtworkReturnType:
        """
        Gets the page metadata from a page request

        :param url: The artwork URL
        :param selector: Requires a dict of CSS selectors for title, description, date, and iterable tags
        :return: An object that returns a title, description, date, and a list of tags
        """
        title_selector = selector.get("title")
        desc_selector = selector.get("description")
        tags_selector = selector.get("tags")
        date_selector = selector.get("date")

        _page = page_req(url)
        tags_list = [str(tag) for tag in _page.select(tags_selector)]

        self._description = _page.select_one(desc_selector)

        return {
            "title": str(_page.select_one(title_selector).text),
            "description": str(self._description.text),
            "date": str(_page.select_one(date_selector)['title']),
            "tags": tags_list
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

        # TODO use difflib.get_close_matches for this one
        MEDIUM = ['digital', 'traditional']
        PROGRAMS = ['photoshop', 'medibang', 'procreate']
        TRADITIONAL_TOOLS = ['gouaches', 'watercolors',
                             'colored pencils', 'markers', 'indian ink', 'pencils']

        TOOLS = [*PROGRAMS, *TRADITIONAL_TOOLS]

        # TODO if nothing is detected, return "Not specified"
        ...

    @staticmethod
    def get_average_dates(dates: list[str]) -> AverageDateReturnType:
        """
        A time series method that gets an average of artworks posted based on a ranges of dates

        :param dates: Requires a list of date strings that will be parsed automatically 
        :return: A dict of the total and average
        """
        ...


class PacoCharacterParser(Parinton):
    def __init__(self) -> None:
        """
        For adding, removing, and editing character data from the database

        Mostly for its use on command line only
        """
        super().__init__()

    def list(self, filter_value: str) -> None:
        ...

    def add(self, name: str, species: str) -> None:
        ...

    def remove(self, name: str, species: str) -> None:
        ...


paco = Parinton()
paco_parse = PacoArtParser()
paco_chars = PacoCharacterParser()
