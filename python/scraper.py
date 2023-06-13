"""
Scraper

Scrapes public drawing data from Paco Panda

Copyright 2021-2023 Kerby Keith Aquino
MIT License
"""
import argparse

from parinton import paco


def main():
    arg_desc = "Scrapes and parses Paco art from FurAffinity, Weasyl, and InkBunny"
    parser = argparse.ArgumentParser(description=arg_desc)

    parser.add_argument('--bypass-cache',
                        help="Bypasses cache file",
                        action='store_true')

    parser.add_argument('--bypass-config',
                        help="Bypasses config for connecting to Redis",
                        action='store_true')

    args = parser.parse_args()

    paco.load_config(bypass=args.bypass_config)

    paco.check_cache(bypass=args.bypass_cache)


if __name__ == "__main__":
    main()
