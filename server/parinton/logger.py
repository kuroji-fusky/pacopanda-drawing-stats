import logging
from typing import Callable, Any

from colorama import init, Fore, Style, just_fix_windows_console
from datetime import datetime

init()
just_fix_windows_console()


class PacoLogger:
    def __init__(self, time: bool = False):
        self._include_time = time
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(LogFormatter(self._include_time))

        self.logger = logging.getLogger("PacoLogger")
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(console_handler)

    def log(self, level: str, *values: str) -> None:
        message = ' '.join(str(value) for value in values)
        getattr(self.logger, level)(message)


class LogFormatter(logging.Formatter):
    _RC = Style.RESET_ALL

    _LEVEL_COLORS = {
        "ERROR": Fore.RED,
        "WARNING": Fore.YELLOW,
        "SUCCESS": Fore.GREEN,
        "INFO": Fore.CYAN,
        "NOTE": Fore.BLUE,
        "VERBOSE": Fore.CYAN
    }

    def __init__(self, include_time: bool):
        self._include_time = include_time
        super().__init__()

    def format(self, record: logging.LogRecord) -> str:
        log_time = datetime.now().strftime("%H:%M:%S") if self._include_time else ""
        log_level = record.levelname
        log_color = f"{self._LEVEL_COLORS.get(log_level)}{log_level}{self._RC}"

        log_message = "[ {} {} ] {}".format(log_time, log_color, record.msg)

        return log_message


def singleton(cls: type) -> Callable[[tuple[Any, ...], dict[str, Any]], Any]:
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class SingletonPacoLogger(PacoLogger):
    pass
