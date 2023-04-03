"""
P2DS - Base Utilities

Copyright 2022-2023 Kerby Keith Aquino; MIT license
"""
import json
from datetime import datetime
from os import path
from typing import Any

from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from paco_utils.constants import BASE_FA, rs, current_date
from paco_utils.logger import ColorLogger

ua_logger = ColorLogger(prefix="UserAgent")
json_logger = ColorLogger(prefix="JSON I/O")


def time_difference(date_input: datetime) -> str:
	delta = (current_date - date_input)

	def fill_zeros(n: int) -> str:
		if n < 10:
			return f"0{n}"

		return str(n)

	seconds = fill_zeros(delta.seconds % 60)
	minutes = fill_zeros(delta.seconds // 60 % 60)
	hours = fill_zeros(delta.seconds // 3600)

	return f"{hours}h {minutes}m {seconds}s"


def get_ua(url: str) -> dict[str, str]:
	"""
	Returns a random user agent

	:param url: Requires as 'referer' header
	"""
	if type(url) is not str:
		raise TypeError(f"Expected type 'str'; but got type {type(url)}")

	ua = UserAgent(browsers=['chrome', 'firefox', 'edge', 'safari'])
	ua_rnd = ua.random

	ua_logger.note(f"Using {ua_rnd}")
	ua_logger.note(f"Referer used: {url}")

	return {
		"User-Agent": ua_rnd,
		"referer": url
	}


def soup_req(url: str, user_agent: dict[str, str] | None = None):
	"""
	An abstraction that accepts URL and returns HTML via BeautifulSoup

	:param url: Required
	:param user_agent: Optional, used along with the `get_ua()` function
	"""
	if user_agent is None:
		user_agent = get_ua(BASE_FA)

	req = rs.get(url, headers=user_agent, timeout=None)
	return BeautifulSoup(req.text, "html.parser")


def update_json(file_name: str, data: Any, root_name: str | None = None, time_series: bool = False,
				overwrite: bool = False):
	if root_name is None:
		root_name = "logs"

	file_exists: bool = path.isfile(file_name)

	if file_exists:
		with open(file_name, "r+") as f:
			try:
				previous_data = json.load(f)

				if time_series:
					f.seek(0)
					json.dump({root_name: [data, *previous_data[root_name]]}, f, indent=2)
					f.truncate()
				else:
					json.dump({root_name: data}, f, indent=2)

			except json.decoder.JSONDecodeError:
				decode_err_msg = f"JSONDecodeError exception was thrown; which the file is invalid" \
								 f"JSON or most likely empty, populating data..."

				json_logger.warn(decode_err_msg)

				if time_series:
					json.dump({root_name: [data]}, f, indent=2)
				else:
					json.dump({root_name: data}, f, indent=2)

			json_logger.success(f"File updated!")

	else:
		json_logger.warn(f"File doesn't exist, creating file with populated data...")
		with open(file_name, "w") as f:
			if time_series:
				json.dump({root_name: [data]}, f, indent=2)
			else:
				json.dump({root_name: data}, f, indent=2)

			json_logger.success(f'File "{file_name}" created!')
