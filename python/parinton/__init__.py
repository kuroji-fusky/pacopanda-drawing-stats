"""
## Parinton

Entry point for initialzing configs, parsers, and managing character data to the database

Copyright 2021-2023 Kerby Keith Aquino
MIT License
"""
from typing import Optional
from bs4 import Tag
from parinton.logger import PacoLogger
from parinton.types import ArtworkDictType, ArtworkReturnType, AverageDateReturnType
from parinton.utils import load_file, page_req

logger = PacoLogger(time=True)

BASE_URL = {
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

        TOOLS = [*MEDIUM, *PROGRAMS, *TRADITIONAL_TOOLS]

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


paco = Parinton()
paco_parse = PacoArtParser()
