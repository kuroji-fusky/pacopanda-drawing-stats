"""
Utils

Helper functions for common file manipulations

Copyright 2021-2023 Kerby Keith Aquino
MIT License
"""
import json
from typing import Dict
from datetime import timedelta

from bs4 import BeautifulSoup
from requests import Session
from requests.exceptions import ConnectionError

from parinton.types import SaveCacheType, CacheData


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


def load_file(file: str):
    """
    Opens file, will open as JSON if file extension is detected

    :param file: File name
    :return Nothing
    """
    with open(file, 'r', encoding='utf-8') as fi:
        if file.endswith('.json'):
            return json.load(fi)

        return fi.read()


def save_file(data, file: str) -> None:
    """
    Saves file, will autosave as JSON if file extension is detected

    :param data: Garbage
    :param file: File name
    :return Nothing
    """
    with open(file, 'w', encoding='utf-8') as fo:
        if file.endswith('.json'):
            json.dump(data, fo, ensure_ascii=True)
        else:
            fo.write(data)


def save_to_cache(save_type: SaveCacheType = 'data', save_value: Dict = None) -> None:
    """
    Saves data to cache

    :param save_type: Must be values 'date', 'pagination', and 'data'
    :param save_value: The save value, must be a dict
    :return: 
    """
    cache_data: CacheData = load_file('paco-cache.json')

    date_st, date_dict = save_type == "date", cache_data.get("cached_time")
    paginate_st, paginate_dict = save_type == "pagination", cache_data.get(
        "pagination")
    data_st, data_dict = save_type == "data", cache_data.get("data")

    if not date_st and not paginate_st and not date_st:
        raise ValueError(
            f"Save type \"{save_type}\" invalid. Only valid types are 'date', 'pagination', and 'data'")

    if date_st:
        date_dict |= save_value

    if paginate_st:
        paginate_dict |= save_value

    if data_st:
        data_dict |= save_value

    save_file(cache_data, "paco-cache.json")


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
