"""
## Utils

Helper functions for common file manipulations

Copyright 2021-2023 Kerby Keith Aquino
MIT License
"""
import json
from typing import Dict, Any
from datetime import timedelta

from bs4 import BeautifulSoup
from requests import Session
from requests.exceptions import ConnectionError

from parinton.types import SaveCacheType, CachedData


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


def load_file(file: str) -> Any:
    """
    Opens file, will open as JSON if file extension is detected

    :param file: File name
    :return File contents
    """
    with open(file, 'r', encoding='utf-8') as fi:
        if file.endswith('.json'):
            return json.load(fi)

        return fi.read()


def save_file(data, file: str, indent: bool = False) -> None:
    """
    Saves file, will autosave as JSON if file extension is detected

    :param data: Garbage
    :param file: File name
    :return File contents
    """
    with open(file, 'w', encoding='utf-8') as fo:
        if file.endswith('.json'):
            if not indent:
                json.dump(data, fo, ensure_ascii=True)
                return

            json.dump(data, fo, ensure_ascii=True, indent=2)
        else:
            fo.write(data)


def cache_data(save_type: SaveCacheType = 'data', save_value: Dict = None) -> None:
    """
    Saves data to cache

    :param save_type: Must be values 'date', 'pagination', and 'data'
    :param save_value: The save value, must be a dict
    :return:
    """
    _cache_data: CachedData = load_file('paco-cache.json')

    date_st, date_dict = save_type == "date", _cache_data.get("cached_time")
    paginate_st, paginate_dict = save_type == "pagination", _cache_data.get(
        "pagination")
    data_st, data_dict = save_type == "data", _cache_data.get("data")

    if not date_st and not paginate_st and not date_st:
        raise ValueError(
            f"Save type \"{save_type}\" invalid. Only valid types are 'date', 'pagination', and 'data'")

    if date_st:
        date_dict |= save_value

    if paginate_st:
        paginate_dict |= save_value

    if data_st:
        data_dict |= save_value

    save_file(_cache_data, "paco-cache.json")


def format_time(time: timedelta) -> str:
    """
    Formats delta time (current time - whatever time has passed) to
    readable time

    :param time: Requires a timedelta type
    :return: A string with a readable time format D HH:MM:SS
    :raises TypeError: If the time parameter is not of type timedelta
    """
    if not isinstance(time, timedelta):
        raise TypeError(
            "Invalid input type. Param 'time' must be a timedelta.")

    _days, _seconds = divmod(time.total_seconds(), 86400)
    d = f"{int(_days)} days" if _days != 1 else f"{int(_days)} day"

    h, remainder = divmod(_seconds, 3600)
    m, s = divmod(remainder, 60)

    h, m, s = map(lambda v: str(v).zfill(2), map(int, (h, m, s)))

    output = f"{d} {h}:{m}:{s}"

    return output


def is_empty_string(s: str) -> bool:
    """
    A wrapper function to check if a string is empty or contains only whitespaces.
    """
    return not s.strip()
