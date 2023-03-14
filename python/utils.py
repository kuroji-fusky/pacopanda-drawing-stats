import requests
from bs4 import BeautifulSoup
from datetime import datetime

BASE_FA = "https://www.furaffinity.net"
BASE_WS = "https://www.weasyl.com"
BASE_IB = "https://inkbunny.net"

rs = requests.Session()
current_date = datetime.now()


def get_ua(url: str = '') -> dict[str, str]:
    return {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)"
            "AppleWebKit/537.36 (KHTML, like Gecko)"
            "Chrome/45.0.2454.101 Safari/537.36"
        ),
        "referer": url
    }


def give_me_soup(url: str, user_agent: dict[str, str] = None):
    """
    :param url: A URL for BeautifulSoup to parse from to HTML.

    :param user_agent: This is optional, this is usually used with the `get_ua()` function.

    - Hello?
    - Hey, what's up?
    - I need your help; can you come here?
    - Uh, I can't; I'm buying clothes.
    - Alright, well hurry up and come over here.
    - I can't find them.
    - What do you mean, you "can't find them"?
    - I can't find them; there's only soup.
    - What do you mean, "there's only soup"?
    - It means, *there's only soup*.
    - Well, then get out of the soup aisle!
    - Alright! You don't have to shout at me!
    - *[footsteps]*
    - There's more soup!
    - What do you mean, "there's more soup"?!
    - There's just more soup!
    - Go into the next aisle!
    - ...there's still soup!
    - Where ARE you right now?!
    - I'm at *Soup*!
    - What do you mean, you're "AT SOUP"?!
    - I mean, I'm *at Soup*!
    - WHAT STORE ARE YOU IN?!
    - I'M AT THE SOUP STORE!!
    - **WHY ARE YOU BUYING CLOTHES AT THE SOUP STORE?!?!**
    - F**K YOU!!!

    Reference: https://youtu.be/72mcTwEleno?t=143
    """

    if user_agent is None:
        user_agent = get_ua(BASE_FA)

    req = rs.get(url, headers=user_agent, timeout=None)
    return BeautifulSoup(req.text, "html.parser")


class SubmissionParser:
    """Parses artworks links from FurAffinity, Weasyl, and InkBunny"""

    def __init__(self, url: str):
        self.__is_furaffinity = url.startswith(BASE_FA)
        self.__is_weasyl = url.startswith(BASE_WS)
        self.__is_inkbunny = url.startswith(BASE_IB)

        if not self.__is_furaffinity and not self.__is_weasyl and not self.__is_inkbunny:
            raise ValueError('Invalid URL, expected URLs from either FurAffinity, Weasyl, and InkBunny only!')

        self.__page: BeautifulSoup | None

        if self.__is_furaffinity:
            self.__page = give_me_soup(url, get_ua(BASE_FA))

        if self.__is_weasyl:
            self.__page = give_me_soup(url, get_ua(BASE_WS))

        if self.__is_inkbunny:
            self.__page = give_me_soup(url, get_ua(BASE_IB))

        self.__fa_contents = self.__page.select_one(".submission-content section")

        self.__date: datetime | None = None

        # We pass dates here so we can calculate the difference here for the updater
        if self.__is_furaffinity:
            fa_date = self.__fa_contents.select_one("span.popup_date")['title']
            self.__date = datetime.strptime(fa_date, "%b %d, %Y %H:%M %p")

        if self.__is_weasyl:
            pass

        if self.__is_inkbunny:
            pass

    def title(self):
        if self.__is_furaffinity:
            fa_title = self.__fa_contents.find(class_="submission-title").text.strip()
            return fa_title

        if self.__is_weasyl:
            return

        if self.__is_inkbunny:
            return

    def img(self):
        if self.__is_furaffinity:
            fa_img = self.__page.select_one("img#submissionImg")
            fa_img = f"https:{fa_img['data-fullview-src']}"
            return fa_img

        if self.__is_weasyl:
            return

        if self.__is_inkbunny:
            return

    def description(self):
        if self.__is_furaffinity:
            fa_desc = self.__fa_contents.select_one(".submission-description")
            fa_desc = fa_desc.text.strip()
            print(fa_desc)

        if self.__is_weasyl:
            return

        if self.__is_inkbunny:
            return

    def tags(self):
        tags_list: list[str] = []

        if self.__is_furaffinity:
            tags_iterable = self.__page.select("section.tags-row span.tags")
            for tag in tags_iterable:
                tags_list.append(tag.text)

            return tags_list

        if self.__is_weasyl:
            return

        if self.__is_inkbunny:
            return

    def date(self):
        return self.__date

    def date_difference(self):
        if self.__is_furaffinity:
            return

        if self.__is_weasyl:
            return

        if self.__is_inkbunny:
            return
