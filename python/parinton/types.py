from typing import TypedDict, List, Dict, Literal


class ArtworkDictType(TypedDict):
    title: str
    description: str
    tags: str
    date: str


class FixedDictArtwork(TypedDict, total=False):
    furaffinity: List[ArtworkDictType]
    weasyl: List[ArtworkDictType]
    inkbunny: List[ArtworkDictType]


class ArtworkReturnType(TypedDict, total=False):
    title: str
    description: str
    tags: List[str]
    date: str


class AverageDateReturnType(TypedDict):
    total: int
    average: float


BaseLiterals = Literal["furaffinity", "weasyl", "inkbunny"]

CachedData = Dict[str, str | FixedDictArtwork]
