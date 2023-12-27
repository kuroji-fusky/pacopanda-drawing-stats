"""
## Scraper

Copyright 2021-2024 Kerby Keith Aquino
Licensed under Apache-2.0
"""
import sys
import argparse
import requests
from typing import Literal
from ..logger import log
from functools import partial
from utils import load_file, save_file, load_characters
from slugify import slugify
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Firefox as WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

base_urls = {
    'furaffinity': 'furaffinity.net',
    'weasyl': 'weasyl.com',
    'inkbunny': 'inkbunny.com',
    'deviantart': 'deviantart.com',
    'tumblr': 'tumblr.com'
}
platforms = list(url for url in base_urls.keys())

parser = argparse.ArgumentParser(description="The Paco Scraper")

parser.add_argument(
    "--platform",
    default=platforms[0],
    const=platforms[0],
    nargs='?',
    choices=platforms,
    type=str,
    help='Fetches data from a specific platform, the default is %(default)s')

args = parser.parse_args()


# --------------------------------------------------------------------- #
#                                                                       #
#                            WEB EXTRACTOR                              #
#                                                                       #
# --------------------------------------------------------------------- #
class StaticWebdriverError(Exception):
    """
    Throws an exception that invoke a Selenium-specific function when 'static' mode is specified,
    used the WebExtractor class.
    """
    pass


class WebExtractor:
    """
    The combined powers of BeautifulSoup and Selenium, all in one class!
    """

    def __init__(self, mode: Literal["static", "dynamic"] = "static") -> None:
        self._scrape_mode = mode

        self._is_static_mode = self._scrape_mode == "static"
        self._is_dynamic_mode = self._scrape_mode == "dynamic"

    def _check_static_error(self):
        if self._is_static_mode or self._driver is None:
            raise StaticWebdriverError("Can't invoke a Selenium-specific function when 'static' mode is specified.")  # NOQA

    def url_request(self, url: str):
        _session = requests.Session()
        _headers = {
            'User-Agent': 'Mozilla/5.0 (https://kurojifusky.com) - for Paco Drawing Stats',
            'Referer': url
        }

        if self._is_static_mode:
            _req = _session.get(url, headers=self._headers)
            log("debug", f"Request {url}, recieved status code {_req.status_code}")  # NOQA

            return BeautifulSoup(_req.text, "html.parser")

        if self._is_dynamic_mode:
            profile = webdriver.FirefoxProfile()
            profile.set_preference("general.useragent.override", _headers)

            driver = webdriver.Firefox(profile)
            driver.get(url)


def iterate_pages(entry_url: str) -> list[str]:
    """
    Gets a number of all the iterated pages by providing its CSS selectors with the "Next" button,

    :param entry_url: The beginning point for URL to paginate and iterate over
    :return: A number of all the iterated pages
    """
    extractor = WebExtractor(mode="static")

    _cache_filename = "cached-page-results.json"
    _cache_prefix = ""

    # Check for cached results first to save requests
    try:
        cached_results = load_file(_cache_filename)

        if base_urls['furaffinity'] in entry_url:
            cached_fa_num = cached_results.get('fa')

            log("info", f"CACHE HIT: Retrieved results: {len(cached_fa_num)}")
            return cached_fa_num

    except FileNotFoundError:
        log("info", "CACHE MISS: Iterating...")
        iterated_pages = []

        # This'll recurse until a "Next" button is not found
        _iterate_url = entry_url
        iterated_pages = len(iterated_pages)

        next_button = None

        def update_url(url: str):
            global _iterate_url

            iterated_pages.append(url)
            _iterate_url = url
            return

        while True:
            _request = extractor.url_request(_iterate_url)

            # TODO use a callback function to simplify this to the main func
            if base_urls['furaffinity'] in entry_url:
                # FurAffinity, for some reason, wraps the Next button on a <form> which is strange
                next_button = _request.select_one('.submission-list .inline:last-child form')  # NOQA
                next_button_link = next_button.get('href')

                update_url(next_button_link)

            log("debug", f"Iterated url so far: {iterated_pages}")

            if not next_button:
                log("info", f"Iterated {len(iterated_pages)} page(s)")
                save_file({}, _cache_filename)

                return iterated_pages


# --------------------------------------------------------------------- #
#                                                                       #
#                              PARSERS                                  #
#                                                                       #
# --------------------------------------------------------------------- #
def get_art_metadata(url: str, **selectors) -> dict[str, str | int | list[str]]:
    """
    Gets the page metadata from a page request

    :param url: The artwork URL
    :param selectors: a keyword args of CSS selectors for title, description, date, and iterable tags
    :return: An object that returns a title, description, date, and a list of tags
    """
    extractor = WebExtractor(mode="static")

    title_selector = selectors.get("title")
    desc_selector = selectors.get("description")
    tags_selector = selectors.get("tags")
    date_selector = selectors.get("date")

    _page = extractor.url_request(url)
    _description = _page.select_one(desc_selector)

    output = {
        "title": str(_page.select_one(title_selector).text),
        "date": str(_page.select_one(date_selector).get('title')),
        "description": str(_description.text),
        "tags": [str(tag) for tag in _page.select(tags_selector)]
    }

    return output


def main():
    extractor = WebExtractor(mode="static")

    def fa_fetch():
        # Do stuff here
        pass

    fa_pages = iterate_pages('https://www.furaffinity.net/gallery/pacopanda', fa_fetch)  # NOQA

    for page_url in fa_pages:
        _page = extractor.url_request(page_url)

    characters = load_characters()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    main()
