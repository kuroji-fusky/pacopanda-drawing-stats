"""
P2DS - Logger Utility

Copyright 2022-2023 Kerby Keith Aquino; MIT license
"""
from typing import Optional

from colorama import just_fix_windows_console
from colorama import Back, Fore, Style

just_fix_windows_console()

W_FG, B_FG, FLUSH = Fore.LIGHTWHITE_EX, Fore.LIGHTBLACK_EX, Style.RESET_ALL
WARN_BG, WARN_FG = Back.LIGHTYELLOW_EX, Fore.LIGHTYELLOW_EX
INFO_BG, INFO_FG = Back.CYAN, Fore.CYAN
NOTE_BG, NOTE_FG = Back.BLUE, Fore.BLUE
ERROR_BG, ERROR_FG = Back.RED, Fore.RED
SUCCESS_BG, SUCCESS_FG = Back.GREEN, Fore.GREEN


class ColorLogger:
	def __init__(self, prefix: Optional[str] = None, minimal: Optional[bool] = False):
		if prefix is None:
			prefix = ''

		self._minimal = minimal
		self._prefix = prefix

		self._info_blk = f"{INFO_BG}{W_FG} INFO {FLUSH}"
		self._note_blk = f"{NOTE_BG}{W_FG} NOTE {FLUSH}"
		self._warn_blk = f"{WARN_BG}{B_FG} WARN {FLUSH}"
		self._err_blk = f"{ERROR_BG}{W_FG} ERROR {FLUSH}"
		self._success_blk = f"{SUCCESS_BG}{W_FG} SUCCESS {FLUSH}"

		self._info_min = f"{INFO_FG}Info"
		self._note_min = f"{NOTE_FG}Note"
		self._warn_min = f"{WARN_FG}Info"
		self._err_min = f"{ERROR_FG}Error"
		self._success_min = f"{SUCCESS_FG}Success"

		self._prefixed_blk = f"{self._prefix}:{FLUSH}"
		self._prefixed_min = f"{self._prefix}:"

	def _logger(self, color_blk: str, color_min: str, fore_color: str, args):
		if not self._minimal and not self._prefix:
			return print(f"{color_blk} {args}")

		if not self._minimal and self._prefix:
			return print(f"{color_blk} {fore_color}{self._prefixed_blk} {args}")

		if self._minimal and not self._prefix:
			return print(f"{color_min}: {args}{FLUSH}")

		if self._minimal and self._prefix:
			return print(f"{color_min} from {self._prefixed_min} {args}{FLUSH}")

	def error(self, args):
		self._logger(color_blk=self._err_blk, color_min=self._err_min, fore_color=ERROR_FG, args=args)

	def warn(self, args):
		self._logger(color_blk=self._warn_blk, color_min=self._warn_min, fore_color=WARN_FG, args=args)

	def info(self, args):
		self._logger(color_blk=self._info_blk, color_min=self._info_min, fore_color=INFO_FG, args=args)

	def note(self, args):
		self._logger(color_blk=self._note_blk, color_min=self._note_min, fore_color=NOTE_FG, args=args)

	def success(self, args):
		self._logger(color_blk=self._success_blk, color_min=self._success_min, fore_color=Fore.LIGHTGREEN_EX, args=args)
