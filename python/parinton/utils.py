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
    """
    Opens file, will open as JSON if file extension is detected
    
    :param file: File name
    """
    with open(file, 'r', encoding='utf-8') as fi:
        if file.endswith('.json'):
            return json.load(fi)

        return fi.read()


def save_file(data: Any, file: str) -> None:
    """
    Saves file, will autosave as JSON if file extension is detected
    
    :param data: Your garbage
    :param file: File name
    """
    with open(file, 'w', encoding='utf-8') as fo:
        if file.endswith('.json'):
            json.dump(data, fo, ensure_ascii=True)

        fo.write(file)


def format_time(time: timedelta) -> str:
    """
    Formats delta time (current time - whatever time has passed) to
    readable time
    
    :param time: Requires a timedelta type
    :return: A string with a readable time format D HH:MM:SS
    """
    _d = f"{time.days} days" if time.days != 1 else f"{time.days} day"
    _h = str(time.seconds // 3600).zfill(2)
    _m = str(time.seconds // 60 % 60).zfill(2)
    _s = str(time.seconds % 60).zfill(2)

    output = f"{_d} {_h}:{_m}:{_s}"

    return output
