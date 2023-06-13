import logging
from datetime import datetime


class LogFormatter(logging.Formatter):
    def __init__(self, include_time):
        self._include_time = include_time
        super().__init__()

    def format(self, record):
        _log_time = datetime.now().strftime("%H:%M:%S") if self._include_time else ""
        _log_level = record.levelname
        return f"[ {_log_time} - {_log_level} ] {record.msg}"


class PacoLogger:
    _instance = None

    def __new__(cls, time=False):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._include_time = time
            cls._instance.logger = logging.getLogger("PacoLogger")
            cls._instance.logger.setLevel(logging.DEBUG)
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(LogFormatter(cls._instance._include_time))
            cls._instance.logger.addHandler(console_handler)

        return cls._instance

    def log(self, level: str, *values: object) -> None:
        message = ' '.join(str(value) for value in values)
        getattr(self.logger, level)(message)
