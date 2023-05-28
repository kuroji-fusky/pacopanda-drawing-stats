from typing import TypedDict, Optional, Literal

"""
Config types
"""
ConfigLiteral = Optional[Literal["prod", "dev"]]


class RedisConfig(TypedDict):
    password: str
    username: str
    host: str
    port: str | int


class ConfigJSONType(TypedDict):
    development: RedisConfig
    production: RedisConfig


"""
Parser and selector types
"""
class PacoBaseURLs(TypedDict):
    furaffinity: str
    weasyl: str
    inkbunny: str


class PaginationType(TypedDict):
    prev_selector: str
    next_selector: str


class ArtworkDictType(TypedDict):
    title: str
    description: str
    tags: str
    date: str


class ArtworkReturnType(TypedDict):
    title: str
    description: str
    tags: list[str]
    date: str
