from typing import TypedDict


class _FixedBaseURLs(TypedDict):
	furaffinity: str
	weasyl: str
	inkbunny: str


class _PaginationType(TypedDict):
	prev_selector: str
	next_selector: str


class _ArtworkDictType(TypedDict):
	title: str
	description: str
	tags: str
	date: str


class _ArtworkReturnType(TypedDict):
	title: str
	description: str
	tags: list[str]
	date: str
