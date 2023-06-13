from typing import TypedDict, List, Dict


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
    furaffinity: List[_ArtworkDictType]
    weasyl: List[_ArtworkDictType]
    inkbunny: List[_ArtworkDictType]


class _ArtworkReturnType(TypedDict):
    title: str
    description: str
    tags: List[str]
    date: str


class _AverageDateReturnType(TypedDict):
    total: int
    average: int


_CacheDictData = Dict[str, str | _FixedBaseURLs | _FixedBaseArtwork]
