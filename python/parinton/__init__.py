"""
## Parinton

Entry point for initialzing configs, parsers, and managing character data to the database

Copyright 2021-2023 Kerby Keith Aquino
MIT License
"""
from typing import Optional, Any
from parinton.logger import PacoLogger
from parinton.utils import page_req

logger = PacoLogger(time=True)


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

        next_button = page_req(iterate_url).select_one(next_selector)

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

    _page = page_req(url)
    tags_list = [str(tag) for tag in _page.select(tags_selector)]

    _description = _page.select_one(desc_selector)

    return {
        "title": str(_page.select_one(title_selector).text),
        "date": str(_page.select_one(date_selector).get('title')),
        "description": str(_description.text),
        "tags": tags_list
    }
