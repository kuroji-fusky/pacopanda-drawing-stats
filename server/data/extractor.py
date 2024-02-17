import requests
from typing import Literal
from ..logger import log
from slugify import slugify
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Firefox as WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


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
