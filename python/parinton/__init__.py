from bs4 import BeautifulSoup
from requests import Session

from typing import Optional
from parinton.typings import _BaseURLs, _ConfigLiteral

BASE_URL: _BaseURLs = {
    "furaffinity": "https://www.furaffinity.net",
    "weasyl": "https://www.weasyl.com",
    "inkbunny": "https://inkbunny.net"
}


class Parinton:
    def __init__(self, verbose_log: Optional[bool] = False):
        if verbose_log is None:
            verbose_log = False

    def create_config(self, environment: _ConfigLiteral):
        """
        Only for CLI use, don't call this function!
        """
        ...

    def load_config(self, fn: str):
        ...

    @staticmethod
    def page_req(url: str):
        try:
            _req = Session().get(url, timeout=None)
            return BeautifulSoup(_req.text, "html.parser")
        except ConnectionError:
            raise ConnectionError
