"""
Parinton -- Base Utilities

Copyright 2022-2023 Kerby Keith Aquino; MIT license
"""
import json
from datetime import datetime
from os import path
from typing import Any, Optional

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

import parinton.exceptions
from parinton.constants import current_date, base_url
from parinton.logger import ColorLogger

logger = ColorLogger()
ua_logger = ColorLogger(prefix="UserAgent")
json_logger = ColorLogger(prefix="JSON I/O")

cache_filename = "paco-cache.json"

rs = requests.Session()


class Parinton:
	"""Base class for checking URLs"""
	page_metadata: dict[str, int] = {'pages': 1, 'artworks': 0}

	b_furaffinity: Optional[str] = base_url.get("furaffinity")
	b_weasyl: Optional[str] = base_url.get("weasyl")
	b_inkbunny: Optional[str] = base_url.get("inkbunny")

	def __init__(self, url: Optional[str] = None, json_fn: Optional[str] = None):
		if url and json_fn:
			raise parinton.exceptions.OperationConflictError(
				"Both URL and JSON params are used - this will cause operation conflicts that will lead"
				" to confusion! Please pass either `url` or `json_fn` params only.")

		if url:
			self.is_fa: bool = url.startswith(self.b_furaffinity)
			self.is_ws: bool = url.startswith(self.b_weasyl)
			self.is_ib: bool = url.startswith(self.b_inkbunny)

			if not self.is_fa and not self.is_ws and not self.is_ib:
				raise parinton.exceptions.SpecificURLError(
					'Invalid URL. Expected URLs from either FurAffinity, Weasyl, and InkBunny only!')

		if json_fn:
			logger.info("JSON param is passed, URL checks have been skipped.")

	def soup_req(self, url: str, user_agent: dict[str, str] | None = None):
		"""
		An abstraction that accepts URL and returns HTML output via BeautifulSoup,
		will throw an exception if user has no internet connection
	
		:param url: Required
		:param user_agent: Optional, used along with the `get_ua()` method
		"""
		try:
			if user_agent is None:
				user_agent = self.get_ua(base_url.get("furaffinity"))

			req = rs.get(url, headers=user_agent, timeout=None)
			return BeautifulSoup(req.text, "html.parser")
		
		except requests.exceptions.ConnectionError:
			requests.exceptions.ConnectionError(
				"Failed to make a request; you probably have unstable or no internet connection, please try again.")

	def check_cache(self):
		"""
		Checks for any cached results usually in JSON format.
		"""
		if not path.isfile(cache_filename):
			logger.warn("No cached file found")

			# TODO rewrite json logic for prepending empty data
			# with open(cache_filename, "a", encoding='utf-8') as nf:
			# 	pre_populate = {
			# 		'last_checked': current_date.isoformat(),
			# 		'furaffinity': {},
			# 		'weasyl': {},
			# 		'inkbunny': {}
			# 	}
			# 
			# 	json.dump(pre_populate, nf)
			return

		with open(cache_filename, "r", encoding='utf-8') as f:
			logger.success("Cache file found. Cached data has been applied.")

			cached_logs = json.load(f).get('logs')
			self.page_metadata.update(pages=cached_logs.get('pages'), artworks=cached_logs.get('artworks'))

			cached_date = datetime.strptime(cached_logs.get('last_checked'), "%Y-%m-%dT%H:%M:%S.%f")

			is_week_passed = (current_date - cached_date).days == 7

			cache_time_computed = self.time_difference(cached_date)
			logger.info(f"Time since cached results: {cache_time_computed}\n")

			if not is_week_passed:
				logger.info("A week hasn't passed yet. If it does, it will update the cache.")

			# Return if a week as passed and overwrite and update the cache data 
			if is_week_passed:
				return

		return

	@staticmethod
	def get_ua(url: Optional[str]) -> dict[str, str]:
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

	@staticmethod
	def update_json(file_name: str, data: Any, root_name: Optional[str] = None, time_series: bool = False,
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

	@staticmethod
	def time_difference(date_input: datetime) -> str:
		delta = (current_date - date_input)

		seconds = (delta.seconds % 60).zfill(2)
		minutes = (delta.seconds // 60 % 60).zfill(2)
		hours = (delta.seconds // 3600).zfill(2)

		return f"{hours}h {minutes}m {seconds}s"
