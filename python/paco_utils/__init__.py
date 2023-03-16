"""
Panda Paco Utils

Copyright 2022-2023 Kerby Keith Aquino; MIT license
"""
import json
from typing import Any

from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from paco_utils.constants import BASE_FA, BASE_WS, BASE_IB, rs
from paco_utils.logger import warn, info, success


def get_ua(url: str) -> dict[str, str]:
	"""
	Returns a random user agent
	
	:param url: Requires as 'referer' header
	"""
	ua = UserAgent(browsers=['chrome', 'firefox', 'edge', 'safari'])

	ua_rnd = ua.random

	info(f"UserAgent: Using {ua_rnd}")

	return {
		"User-Agent": ua_rnd,
		"referer": url
	}


def gimme_soop(url: str, user_agent: dict[str, str] | None = None):
	"""
	An abstraction that accepts URL and returns HTML via BeautifulSoup
	
	:param url: Required
	:param user_agent: Optional, used along with the `get_ua()` function
	"""
	if user_agent is None:
		user_agent = get_ua(BASE_FA)

	req = rs.get(url, headers=user_agent, timeout=None)
	return BeautifulSoup(req.text, "html.parser")


def update_json(file_name: str, data: Any):
	# TODO place this in the SubmissionParser class for another layer of abstraction
	f_name = "UpdateJSON:"

	try:
		with open(file_name, "r+") as f:
			try:
				previous_data = json.load(f)

				f.seek(0)
				json.dump({'fa': [data, *previous_data['fa']]}, f, indent=2)
				f.truncate()

			except json.decoder.JSONDecodeError:
				warn(
					f"{f_name} JSONDecodeError exception was thrown; which the file is most likely empty, populating data...")
				json.dump({'fa': [data]}, f, indent=2)

			success(f"{f_name} File updated!")

	except FileNotFoundError:
		warn(f"{f_name} File doesn't exist, creating file with populated data...")
		with open(file_name, "w") as f:
			json.dump({'fa': [data]}, f, indent=2)

		success(f"{f_name} File created!")
