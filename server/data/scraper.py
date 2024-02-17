"""
## Scraper

Copyright 2021-2024 Kerby Keith Aquino
Licensed under Apache-2.0
"""
import re
import sys
import argparse
from utils import load_characters
from extractor import WebExtractor

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


class RequiredParameter(Exception):
    pass


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


def parse_medium(description: str, tags: list[str]) -> dict[str, str]:
    if description is None or tags is None:
        raise RequiredParameter("Param can't be None or empty string")

    parsed_desc = description.splitlines()[-1]


def parse_characters(description: str, tags: list[str]) -> dict[str, str]:
    if description is None or tags is None:
        raise RequiredParameter("Param can't be None or empty string")

    char_list = load_characters()

    # This will be utilized 90% of the time
    desc_split = description.splitlines()
    parsed_desc = list(filter(None, desc_split))

    mediums = parsed_desc[-1]

    parsed_medium = [re.sub(r'\.|\/', '', x) for x in mediums.split()]
    parsed_medium = list(filter(None, parsed_medium))


def main():
    extractor = WebExtractor(mode="static")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    main()
