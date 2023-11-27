"""
## Logger

It logs things. Pretty neat, I guess lol

Copyright 2021-2023 Kerby Keith Aquino
MIT License
"""
import logging
from sys import platform
from typing import Literal
from colorama import init, Back, Fore, Style, just_fix_windows_console as JUST_FIX_THE_GODDAMN_THING_FOR_WINDOWS_YOU_FAK

init(autoreset=True)

if platform == "win32" or platform == "cygwin":
    JUST_FIX_THE_GODDAMN_THING_FOR_WINDOWS_YOU_FAK()

LogStatus = Literal["warn", "error", "info", "debug"]


# TODO fix duplicate stream thingy on console
def log(status: LogStatus = "info", *args):
    status_colors = {
        "info": (Fore.WHITE, Back.BLUE, logging.INFO),
        "warn": (Fore.YELLOW, Back.BLACK, logging.WARNING),
        "error": (Fore.WHITE, Back.RED, logging.ERROR),
        "debug": (Fore.CYAN, Back.BLACK, logging.DEBUG),
    }

    fore_color, back_color, log_level = status_colors.get(
        status.lower(), status_colors["info"])

    logging.basicConfig(format="%(asctime)s %(message)s",
                        datefmt="%m-%D-%Y %H:%M:%S", level=log_level)
    logger = logging.getLogger()

    console = logging.StreamHandler()
    formatter = logging.Formatter(
        f"%(asctime)s {fore_color}{back_color}{Style.BRIGHT}{status.upper()}{Style.RESET_ALL} - %(message)s")

    console.setFormatter(formatter)

    logger.addHandler(console)

    logger.log(log_level, ' '.join(args))
