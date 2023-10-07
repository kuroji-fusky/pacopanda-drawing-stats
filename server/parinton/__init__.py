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
        self.bypass_cache = False


class PacoArtParser(Parinton):
    def __init__(self) -> None:
        super().__init__()

        self._description: Tag | None = None

        self.__is_fa = self.__url_startswith('furaffinity')

    @staticmethod
    def __url_startswith(base: BaseLiterals):
        return BASE_URL[base]

    def iterate_pages(self, entry_url: str, next_selector: str) -> int:
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
