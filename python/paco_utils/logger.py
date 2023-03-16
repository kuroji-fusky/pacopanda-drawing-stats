"""
Panda Paco Utils

Copyright 2022-2023 Kerby Keith Aquino; MIT license
"""
from colorama import just_fix_windows_console
from colorama import Back, Fore, Style

just_fix_windows_console()

W_FG, B_FG, FLUSH = Fore.LIGHTWHITE_EX, Fore.LIGHTBLACK_EX, Style.RESET_ALL
WARN_BG, INFO_BG, ERROR_BG, SUCCESS_BG = Back.LIGHTYELLOW_EX, Back.CYAN, Back.RED, Back.GREEN


def error(msg):
	print(f"{ERROR_BG}{W_FG} ERROR {FLUSH} {msg}")


def warn(msg):
	print(f"{WARN_BG}{B_FG} WARN {FLUSH} {msg}")


def info(msg):
	print(f"{INFO_BG}{W_FG} INFO {FLUSH} {msg}")


def success(msg):
	print(f"{SUCCESS_BG}{W_FG} SUCCESS {FLUSH} {msg}")
