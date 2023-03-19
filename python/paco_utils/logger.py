"""
PDS Logger Utility

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

	def error(self, args):
		if not self._minimal and not self._prefix:
			print(f"{self._err_blk} {args}")

		if not self._minimal and self._prefix:
			print(f"{self._err_blk} {ERROR_FG}{self._prefixed_blk} {args}")

		if self._minimal and not self._prefix:
			print(f"{self._err_min}: {args}{FLUSH}")

		if self._minimal and self._prefix:
			print(f"{self._err_min} from {self._prefixed_min} {args}{FLUSH}")

	def warn(self, args):
		if not self._minimal and not self._prefix:
			print(f"{self._warn_blk} {args}")

		if not self._minimal and self._prefix:
			print(f"{self._warn_blk} {WARN_FG}{self._prefixed_blk} {args}")

		if self._minimal and not self._prefix:
			print(f"{self._warn_min}: {args}{FLUSH}")

		if self._minimal and self._prefix:
			print(f"{self._warn_min} from {self._prefixed_min} {args}{FLUSH}")

	def info(self, args):
		if not self._minimal and not self._prefix:
			print(f"{self._info_blk} {args}")

		if not self._minimal and self._prefix:
			print(f"{self._info_blk} {INFO_FG}{self._prefixed_blk} {args}")

		if self._minimal and not self._prefix:
			print(f"{self._info_min}: {args}{FLUSH}")

		if self._minimal and self._prefix:
			print(f"{self._info_min} from {self._prefixed_min} {args}{FLUSH}")

	def note(self, args):
		if not self._minimal and not self._prefix:
			print(f"{self._note_blk} {args}")

		if not self._minimal and self._prefix:
			print(f"{self._note_blk} {NOTE_FG}{self._prefixed_blk} {args}")

		if self._minimal and not self._prefix:
			print(f"{self._note_min}: {args}{FLUSH}")

		if self._minimal and self._prefix:
			print(f"{self._note_min} from {self._prefixed_min} {args}{FLUSH}")

	def success(self, args):
		if not self._minimal and not self._prefix:
			print(f"{self._success_blk} {args}")

		if not self._minimal and self._prefix:
			print(f"{self._success_blk} {SUCCESS_FG}{self._prefixed_blk} {args}")

		if self._minimal and not self._prefix:
			print(f"{self._success_min}: {args}{FLUSH}")

		if self._minimal and self._prefix:
			print(f"{self._success_min} from {self._prefixed_min} {args}{FLUSH}")
