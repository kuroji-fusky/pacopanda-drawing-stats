"""
## Scraper

Copyright 2021-2023 Kerby Keith Aquino
MIT License
"""
import sys
import argparse
import requests
import json
import yaml
from .logger import log
from typing import Literal, Any
from datetime import timedelta
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

PLATFORMS = ['furaffinity', 'weasyl', 'inkbunny', 'deviantart', 'tumblr']

parser = argparse.ArgumentParser(description="The Paco Scraper")

parser.add_argument(
    "--platform",
    default=PLATFORMS[0],
    const=PLATFORMS[0],
    nargs='?',
    choices=PLATFORMS,
    type=str,
    help='Fetches data from a specific platform, the default is %(default)s')

args = parser.parse_args()
session = requests.Session()


# --------------------------------------------------------------------- #
#                                                                       #
#                          SHARED FUNCTIONS                             #
#                                                                       #
# --------------------------------------------------------------------- #
def load_file(file: str) -> Any:
    """
    Opens file, will open as JSON or parse to YAML if file extension is detected

    :param file: File name
    :return File contents
    """
    with open(file, 'r', encoding='utf-8') as f:
        if file.endswith('.json'):
            return json.load(f)

        if file.endswith('.yml') or file.endswith('.yaml'):
            return yaml.safe_load(f)

        return f.read()


def save_file(data, file: str, indent: bool = False) -> None:
    """
    Saves file, will autosave as JSON if file extension is detected

    :param data: Garbage
    :param file: File name
    :return File contents
    """
    with open(file, 'w+', encoding='utf-8') as f:
        if file.endswith('.json'):
            if not indent:
                json.dump(data, f, ensure_ascii=True)
                return

            json.dump(data, f, ensure_ascii=True, indent=2)
        else:
            f.write(data)


def format_time(time: timedelta) -> str:
    """
    Formats delta time (current time - whatever time has passed) to
    readable time

    :param time: Requires a timedelta type
    :return: A string with a readable time format D HH:MM:SS
    :raises TypeError: If the time parameter is not of type timedelta
    """
    if not isinstance(time, timedelta):
        raise TypeError("Invalid input type. Param 'time' must be a timedelta.")  # NOQA

    _dm_days, _dm_seconds = divmod(time.total_seconds(), 86400)

    d = f"{int(_dm_days)} days" if _dm_days != 1 else f"{int(_dm_days)} day"
    h, remainder = divmod(_dm_seconds, 3600)
    m, s = divmod(remainder, 60)

    h, m, s = map(lambda v: str(v).zfill(2), map(int, (h, m, s)))

    return f"{d} {h}:{m}:{s}"


# --------------------------------------------------------------------- #
#                                                                       #
#                            WEB EXTRACTOR                              #
#                                                                       #
# --------------------------------------------------------------------- #
class WebExtractor:
    """
    The combined powers of BeautifulSoup and Selenium, all in one class!
    """

    def __init__(self, mode: Literal["static", "dynamic"] = "static") -> None:
        self._scrape_mode = mode
        self._driver = webdriver.Firefox(keep_alive=True)

    def url_request(self, url: str):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Kurowo 1.0; https://kuroji.fusky.pet)'
        }

        if self._scrape_mode == "static":
            _req = session.get(url, headers=headers)
            log("debug", ("Request {}, recieved status code {}").format(url, _req.status_code))  # NOQA

            return BeautifulSoup(_req.text, "html.parser")

        if self._scrape_mode == "dynamic":
            self._driver.get(url)


static_extractor = WebExtractor(mode="static")


def iterate_pages(entry_url: str) -> list[str]:
    """
    Gets a number of all the iterated pages by providing its CSS selectors with the "Next" button,

    :param entry_url: The beginning point for URL to paginate and iterate over
    :param next_selector: The CSS selector of a "Next" button 
    :return: A number of all the iterated pages
    """
    _cache_filename = "cached-page-results.json"
    _url = {
        'fa': 'furaffinity.net',
        'ws': 'weasyl.com',
        'ib': 'inkbunny.com'
    }

    # Check for cached results first to save requests
    try:
        cached_results = load_file(_cache_filename)

        if _url['fa'] in entry_url:
            cached_fa_num = cached_results.get('fa')

            log("info", "CACHE HIT: Retrieved results: {}".format(len(cached_fa_num)))
            return cached_fa_num

    except FileNotFoundError:
        log("info", "CACHE MISS: Iterating...")
        iterated_pages = []

        # This'll recurse until a "Next" button is not found
        while True:
            iterate_url = entry_url
            iterated_pages = len(iterated_pages)

            next_button = None

            _request = static_extractor.url_request(iterate_url)

            if _url['fa'] in entry_url:
                # FurAffinity, for some reason, wraps the Next button on a <form> which is strange
                next_button = _request.select('.submission-list .inline:last-child form')  # NOQA
                iterated_pages.append(iterate_url)

            print("Iterated url so far: {}".format(iterated_pages))

            if not next_button:
                print("Iterated {} page(s)", iterated_pages)
                save_file({}, _cache_filename)

                return iterated_pages


# --------------------------------------------------------------------- #
#                                                                       #
#                              PARSERS                                  #
#                                                                       #
# --------------------------------------------------------------------- #
def get_art_metadata(url: str, selector: str) -> dict[str, Any]:
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

    _page = static_extractor.url_request(url)
    tags_list = [str(tag) for tag in _page.select(tags_selector)]

    _description = _page.select_one(desc_selector)

    return {
        "title": str(_page.select_one(title_selector).text),
        "date": str(_page.select_one(date_selector).get('title')),
        "description": str(_description.text),
        "tags": tags_list
    }


def main():
    print(args.platform)
    # TODO Check cache for iterated pages, continue otherwise
    fa_pages = iterate_pages('https://www.furaffinity.net/gallery/pacopanda')

    for page_url in fa_pages:
        _page = static_extractor.url_request(page_url)
    ...

    # Convert characters.yml into dicts
    characters = load_file("characters.yml")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    main()
