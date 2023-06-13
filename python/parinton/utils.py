"""
Utils

Helper functions for common file manipulations

Copyright 2021-2023 Kerby Keith Aquino
MIT License
"""
import json
from typing import Any
from datetime import timedelta


def load_file(file: str) -> Any:
    with open(file, 'r', encoding='utf-8') as fi:
        if file.endswith('.json'):
            return json.load(fi)

        return fi.read()


def save_json(data: Any, file: str) -> None:
    with open(file, 'w', encoding='utf-8') as fo:
        json.dump(data, fo, ensure_ascii=True)


def format_time(time: timedelta) -> str:
    _d = f"{time.days} days" if time.days != 1 else f"{time.days} day"
    _h = str(time.seconds // 3600).zfill(2)
    _m = str(time.seconds // 60 % 60).zfill(2)
    _s = str(time.seconds % 60).zfill(2)

    output = f"{_d} {_h}:{_m}:{_s}"

    return output
