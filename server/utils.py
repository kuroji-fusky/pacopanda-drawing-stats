import json
import yaml
from typing import Any
from datetime import timedelta


def load_file(file: str) -> Any:
    """
    Opens file, will open as JSON or parse to YAML if respective file extension is detected

    :param file: File name
    :return File contents
    """
    with open(file, 'r', encoding='utf-8') as f:
        if file.endswith('.json'):
            return json.load(f)

        if file.endswith('.yml') or file.endswith('.yaml'):
            return yaml.safe_load(f)

        return f.read()


def save_file(data, file: str, indent: bool = False) -> None:
    """
    Saves file, will autosave as JSON if file extension is detected

    :param data: Garbage
    :param file: File name
    :return File contents
    """
    with open(file, 'w+', encoding='utf-8') as f:
        if file.endswith('.json'):
            if not indent:
                json.dump(data, f, ensure_ascii=True)
                return

            json.dump(data, f, ensure_ascii=True, indent=2)
        else:
            f.write(data)


def load_characters() -> list[dict[str, str]]:
    return load_file("characters.yml")


def format_time(time: timedelta) -> str:
    """
    Formats delta time (current time - whatever time has passed) to
    readable time

    :param time: Requires a timedelta type
    :return: A string with a readable time format D HH:MM:SS
    :raises TypeError: If the time parameter is not of type timedelta
    """
    if not isinstance(time, timedelta):
        raise TypeError("Invalid input type. Param 'time' must be a timedelta.")  # NOQA

    SECS_IN_DAYS = 86400

    _dm_days, _dm_seconds = divmod(time.total_seconds(), SECS_IN_DAYS)

    d = f"{int(_dm_days)} days" if _dm_days != 1 else f"{int(_dm_days)} day"
    h, remainder = divmod(_dm_seconds, 3600)
    m, s = divmod(remainder, 60)

    h, m, s = map(lambda v: str(v).zfill(2), map(int, (h, m, s)))

    return f"{d} {h}:{m}:{s}"
