"""
Paco Stats Utils

A set of utilities to abstract automation and web scraping

Copyright 2021-2023 Kerby Keith Aquino
MIT License
"""
import parinton
from parinton.typings import ArtworkReturnType, ArtworkDictType
from bs4.element import Tag


class ParseStuff(parinton.Parinton):
    def __init__(self, url: str, verbose_log: bool | None) -> None:
        super().__init__(verbose_log)

        self._url = url
        self._description: Tag | None = None

    def get_art_metadata(self, selector: ArtworkDictType) -> ArtworkReturnType:
        title_selector = selector.get("title")
        desc_selector = selector.get("description")
        tags_selector = selector.get("tags")
        date_selector = selector.get("date")

        _page = self.page_req(self._url)
        _tags_arr = [tag for tag in _page.select(tags_selector)]

        self._description = _page.select_one(desc_selector)

        # TODO use param for getting the text attr
        return {
            "title": _page.select_one(title_selector),
            "description": self._description,
            "date": _page.select_one(date_selector),
            "tags": _tags_arr
        }

    def parse_medium(self) -> None:
        """
        there's a common pattern that in every artwork descriptions; he lists what tools
        and medium of the artwork (i.e. "Digital. Photoshop.")

        my approach is to go to the last lines of the description using .split('\n')
        and match mediums and whatever tools he uses
        """
        # TODO do something with this crap
        desc = self._description
        ...

    def list_characters(self):
        ...

    def add_character(self):
        ...

    def remove_character(self):
        ...
