"""
Parinton

Parinton Entry Point

Copyright 2021-2023 Kerby Keith Aquino
MIT License
"""
import os
from datetime import datetime
from typing import Optional

from dotenv import load_dotenv

from parinton.exceptions import *
from parinton.logger import PacoLogger
from parinton.types import FixedBaseURLs, FixedDictArtwork, CacheData
from parinton.utils import load_file, save_file, format_time

logger = PacoLogger(time=True)

OptBool = Optional[bool]

BASE_URL: FixedBaseURLs = {
    "furaffinity": "https://www.furaffinity.net",
    "weasyl": "https://www.weasyl.com",
    "inkbunny": "https://inkbunny.net"
}


class Parinton:
    def __init__(self) -> None:
        self.cache_filename = "paco-cache.json"

        self.redis_url: Optional[str] = None
        self.bypass_cache = False

    def bootstrap(self,
                  bypass_config: OptBool = False,
                  bypass_cache: OptBool = False,
                  production: OptBool = False) -> None:
        """
        An initalizer for checking the config and cache, this must be called first before anything else!

        :param bypass_config: Bypasses the config
        :param bypass_cache: Bypasses the cache file
        :param production: Points the config to production environment
        """
        self._load_config(bypass=bypass_config, production=production)
        self.check_cache(bypass=bypass_cache)

    def _load_config(self, bypass: OptBool = False, production: OptBool = False) -> None:
        """
        Loads a Redis URL based on its environment. Make sure you know what you're doing!

        :param bypass: Bypass the need to load the config
        :param production: A boolean whether to use the production environment
        :return: None
        """
        load_dotenv()

        _logger = "[ ⚙️ Redis Config ]"

        DEV_URL = os.getenv('DEV_REDIS_URL')
        PROD_URL = os.getenv('PROD_REDIS_URL')
        REDIS_PROTOCOL = "redis://"

        if bypass:
            logger.log('info', "{} {}".format(
                _logger, 'Redis config bypassed'))
            return

        def env_error(env_key):
            logger.log('error', "{} {}".format(
                _logger, 'Redis protocol not found!'))

            raise EnvironmentValueError(f"Key '{env_key}' doesn't begin with '{REDIS_PROTOCOL}'\n\n"
                                        "If you think this is a mistake, running tests, or populating the cache file, "
                                        "add the '--bypass-config' flag to populate the cache locally on your system."
                                        )

        if DEV_URL is None:
            raise EnvironmentNotFound(".env key 'DEV_REDIS_URL' isn't found!")

        if not DEV_URL.startswith(REDIS_PROTOCOL):
            env_error('DEV_REDIS_URL')

        if not PROD_URL.startswith(REDIS_PROTOCOL):
            env_error('PROD_REDIS_URL')

        if not production and PROD_URL:
            raise EnvironmentProductionError(".env key 'PROD_REDIS_URL' found, but running in a dev instead.",
                                             "Rerun the script with '--prod' flag!")

        if production and PROD_URL is None:
            raise EnvironmentNotFound(
                "Production mode enabled, but .env key 'PROD_REDIS_URL' isn't found!")

        if production and PROD_URL:
            self.redis_url = PROD_URL
            logger.log('success', "{} {}".format(
                _logger, 'Redis production environment loaded'))

        if DEV_URL:
            self.redis_url = DEV_URL
            logger.log('success', "{} {}".format(
                _logger, 'Redis dev environment loaded'))

    def check_cache(self, bypass: OptBool = False) -> None:
        """
        Checks for a cache file that consists of the creation date, paginated pages, and artwork metadata.

        This cache functionality is to save bulk requests every time the script is run (mostly for testing); otherwise
        sending too much traffic will cause it to get rate limited temporarily and I might not able to retrieve data.

        :param bypass: A boolean to either bypass cache checks
        """
        _logger = "[ ⚡ Cache Check ]"

        current_dt = datetime.now()

        prepend_data: CacheData = {
            'cached_time': current_dt.isoformat(),
            'pagination': {
                'furaffinity': '0',
                'weasyl': '0',
                'inkbunny': '0'
            },
            'data': {
                'furaffinity': [],
                'weasyl': [],
                'inkbunny': []
            }
        }

        if bypass:
            self.bypass_cache = True
            return

        try:
            logger.log('info', "{} {}".format(_logger, "Cache file found!"))
            cached_data = load_file(self.cache_filename)

            cached_dt = cached_data.get('cached_time')

            delta = current_dt - datetime.fromisoformat(cached_dt)
            delta_week = delta.days > 7

            if not delta_week:
                logger.log('info', "{} {}".format(
                    _logger, "A week hasn't passed yet, repurposing cached values"))
                logger.log('info',
                           "{} {} {}".format(_logger, "Elapsed time since cache creation:", format_time(delta)))
            else:
                ...

        except FileNotFoundError:
            logger.log('warn', "{} {}".format(
                _logger, "No cache file found, created file and loaded"))

            save_file(prepend_data, self.cache_filename)


paco = Parinton()
