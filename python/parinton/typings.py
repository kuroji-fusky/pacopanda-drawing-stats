from typing import TypedDict


class _FixedBaseURLs(TypedDict):
	furaffinity: str
	weasyl: str
	inkbunny: str


class _ArtworkDictType(TypedDict):
	title: str
	description: str
	tags: str
	date: str


class _FixedBaseArtwork(TypedDict):
	furaffinity: list[_ArtworkDictType]
	weasyl: list[_ArtworkDictType]
	inkbunny: list[_ArtworkDictType]


class _ArtworkReturnType(TypedDict):
	title: str
	description: str
	tags: list[str]
	date: str


class _AverageDateReturnType(TypedDict):
	total: int
	average: int
