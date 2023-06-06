from typing import TypedDict, Optional, Literal

"""
Config types
"""
_ConfigLiteral = Optional[Literal["prod", "dev"]]


class _RedisConfig(TypedDict):
    password: str
    username: str
    host: str
    port: str | int


class ConfigJSONType(TypedDict):
    development: _RedisConfig
    production: _RedisConfig


"""
Parser and selector types
"""
class _BaseURLs(TypedDict):
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
