"""
Parsers

Helper stuff for manipulating data

Copyright 2021-2023 Kerby Keith Aquino
MIT License
"""
from typing import Optional
from bs4.element import Tag

from parinton import Parinton
from parinton import _ArtworkDictType, _ArtworkReturnType
from parinton.typings import _AverageDateReturnType


class PacoArtParser(Parinton):
	def __init__(self, url: Optional[str] | None = None) -> None:
		super().__init__()

		self._url = url
		self._description: Tag | None = None

	def parse_medium(self) -> None:
		"""
		There's a common pattern that in every artwork descriptions; he lists what tools
		and medium of the artwork (i.e. "Digital. Photoshop.")

		My approach is to go to the last lines of the description using .split('\n')
		and match mediums and whatever tools he uses
		"""
		# TODO do something with this crap
		_desc = self._description

		_MEDIUM = ['digital', 'traditional']

		# TODO use difflib.get_close_matches for this one
		_PROGRAMS = ['photoshop', 'medibang', 'procreate']
		_TRAD_TOOLS = ['gouaches', 'watercolors', 'colored pencils', 'markers', 'indian ink', 'pencils']

		_TOOLS = [*_PROGRAMS, *_TRAD_TOOLS]

		# TODO if nothing is detected, return "not specified"
		...

	def get_art_metadata(self, selector: _ArtworkDictType) -> _ArtworkReturnType:
		"""
		Gets the page metadata from a page request

		:param selector: Requires a dict of CSS selectors for title, description, date, and iterable tags
		:return: An object that returns a title, description, date, and a list of tags
		"""
		title_selector = selector.get("title")
		desc_selector = selector.get("description")
		tags_selector = selector.get("tags")
		date_selector = selector.get("date")

		_page = self.page_req(self._url)
		_tags_list = [str(tag) for tag in _page.select(tags_selector)]

		self._description = _page.select_one(desc_selector)

		# TODO use param for getting the text attr
		return {
			"title": str(_page.select_one(title_selector).text),
			"description": str(self._description.text.strip()),
			"date": str(_page.select_one(date_selector)),
			"tags": _tags_list
		}

	@staticmethod
	def get_average_dates(dates: list[str]) -> _AverageDateReturnType:
		"""
		A time series method that gets an average of artworks posted based on a ranges of dates
		
		:param dates: Requires a list of date strings that will be parsed automatically 
		:return: A dict of the total and average
		"""
		...


class PacoCharacters(Parinton):
	def __init__(self) -> None:
		"""
		For adding, removing, and editing character data from the database
		
		Mostly for its use on command line only
		"""
		super().__init__()

	def list(self):
		...

	def add(self):
		...

	def remove(self):
		...


parser = PacoArtParser()
character = PacoCharacters()
