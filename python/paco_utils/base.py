"""
Panda Paco Utils

Copyright 2022-2023 Kerby Keith Aquino; MIT license
"""
import json
from os import path
from typing import Any

from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from paco_utils.constants import BASE_FA, BASE_WS, BASE_IB, rs
from paco_utils.logger import warn, success, note


def get_ua(url: str) -> dict[str, str]:
	"""
	Returns a random user agent

	:param url: Requires as 'referer' header
	"""
	ua = UserAgent(browsers=['chrome', 'firefox', 'edge', 'safari'])

	ua_rnd = ua.random

	note(f"UserAgent: Using {ua_rnd}")
	note(f"Referer used: {url}")

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


def update_json(file_name: str, data: Any, root_name: str | None = None, time_series: bool = False):
	if root_name is None:
		root_name = "logs"

	debug_name = "JSON I/O:"
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
				decode_err_msg = f"{debug_name} JSONDecodeError exception was thrown; which the file is invalid" \
								 f"JSON or most likely empty, populating data..."

				warn(decode_err_msg)

				if time_series:
					json.dump({root_name: [data]}, f, indent=2)
				else:
					json.dump({root_name: data}, f, indent=2)

			success(f"{debug_name} File updated!")

	else:
		warn(f"{debug_name} File doesn't exist, creating file with populated data...")
		with open(file_name, "w") as f:
			if time_series:
				json.dump({root_name: [data]}, f, indent=2)
			else:
				json.dump({root_name: data}, f, indent=2)

			success(f'{debug_name} File "{file_name}" created!')
