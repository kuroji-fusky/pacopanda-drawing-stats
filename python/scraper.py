"""
Scraper

Scrapes public drawing data from Paco Panda

Copyright 2021-2023 Kerby Keith Aquino
MIT License
"""
import argparse
import threading
from typing import Literal

from parinton import paco, FixedBaseURLs, BASE_URL, load_file, CacheData, save_file
from parinton.parsers import paco_parse


def main():
    arg_desc = "Scrapes and parses Paco art from FurAffinity, Weasyl, and InkBunny"
    parser = argparse.ArgumentParser(description=arg_desc)

    parser.add_argument('--bypass-all',
                        help="Bypasses checks for Redis config and cache (used for debugging only)",
                        action='store_true')

    parser.add_argument('--bypass-config',
                        help="Bypasses config for connecting to Redis",
                        action='store_true')

    parser.add_argument('--bypass-cache',
                        help="Bypasses cache file",
                        action='store_true')

    parser.add_argument('-P', '--prod',
                        help="Set the script to run in production mode",
                        action='store_true')

    args = parser.parse_args()

    if not args.bypass_all:
        paco_parse.bootstrap(bypass_config=args.bypass_config,
                             bypass_cache=args.bypass_cache,
                             production=args.prod)

    else:
        paco_parse.bootstrap(bypass_config=True,
                             bypass_cache=True,
                             production=args.prod)

    FA_GALLERY_LIMIT, WS_GALLERY_LIMIT, IB_GALLERY_LIMIT = 48, 60, 60
    FA_GALLERY_URL = f'{BASE_URL.get("furaffinity")}/gallery/pacopanda/'
    WS_GALLERY_URL = f'{BASE_URL.get("weasyl")}/submissions/pandapaco/'

    # def furaffinity():
    #     total_pages = paco_parse.iterate_paginated_pages(entry_url=FA_GALLERY_URL,
    #                                                      next_selector='div.aligncenter .inline:last-child > form')
    # 
    #     print(total_pages * FA_GALLERY_LIMIT)
    # TODO implement threading on these
    # furaffinity()



if __name__ == "__main__":
    main()
