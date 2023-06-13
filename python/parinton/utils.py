"""
Utils

Helper functions for common file manipulations

Copyright 2021-2023 Kerby Keith Aquino
MIT License
"""
import json
from typing import Any


def load_file(f: str) -> Any:
    with open(f, 'r', encoding='utf-8') as fi:
        if f.endswith('.json'):
            return json.load(fi)

        return fi.read()


def save_json(data: Any, f: str) -> None:
    with open(f, 'w', encoding='utf-8') as fo:
        json.dump(data, fo, ensure_ascii=True)
