"""
## Scraper

Copyright 2021-2023 Kerby Keith Aquino
MIT License
"""
import sys
import argparse
import requests
from .logger import log
from typing import Literal, Any
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

parser = argparse.ArgumentParser(description="The Paco Scraper")

PLATFORMS = ['furaffinity', 'weasyl', 'inkbunny', 'deviantart', 'tumblr']

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


class WebExtractor:
    """
    The combined powers of BeautifulSoup and Selenium, all in one class.
    """

    def __init__(self, mode: Literal["static", "dynamic"] = "static") -> None:
        self.scrape_mode = mode
        self.driver = webdriver.Firefox(keep_alive=True)

    def url_request(self, url: str):
        if self.scrape_mode == "static":
            _req = session.get(url)
            log("debug", ("Request {}, recieved status code {}").format(
                url, _req.status_code))

            return BeautifulSoup(_req.text, "html.parser")

        if self.scrape_mode == "dynamic":
            self.driver.get(url)


crispy_dib = WebExtractor(mode="static")
crispy_zim = WebExtractor(mode="dynamic")


def iterate_pages(entry_url: str, next_selector: str) -> int:
    """
    Gets a number of all the iterated pages by providing its CSS selectors with the "Next" button

    :param entry_url: The beginning point for URL to paginate and iterate over
    :param next_selector: The CSS selector of a "Next" button 
    :return: A number of all the iterated pages
    """
    _logger = "[ 🔁 Iterator ]"

    iterated_pages = 0

    while True:
        iterate_url = entry_url

        next_button = crispy_dib.url_request(
            iterate_url).select_one(next_selector)

        iterated_pages += 1
        final_iter_pages = iterated_pages - 1

        print("{} {} {}".format(
            _logger, 'Iterated pages so far:', final_iter_pages))

        if not next_button:
            print("Iterated {} page(s)", final_iter_pages)
            return final_iter_pages


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

    _page = crispy_dib.url_request(url)
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
    # fa_art = iterate_pages(
    #     entry_url='https://www.furaffinity.net/gallery/pacopanda',
    #     next_selector='.submission-list .aligncenter .inline:last-child form')
    ...


if __name__ == "__main__":
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    main()
