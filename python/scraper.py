"""
Scraper

Scrapes public drawing data from Paco Panda

Copyright 2021-2023 Kerby Keith Aquino
MIT License
"""
import argparse
import threading

from parinton import paco


def main():
    arg_desc = "Scrapes and parses Paco art from FurAffinity, Weasyl, and InkBunny"
    parser = argparse.ArgumentParser(description=arg_desc)

    parser.add_argument('--bypass-config',
                        help="Bypasses config for connecting to Redis",
                        action='store_true')

    parser.add_argument('--bypass-cache',
                        help="Bypasses cache file",
                        action='store_true')

    parser.add_argument('-P', '--prod',
                        help="Set the script to production",
                        action='store_true')

    args = parser.parse_args()

    paco.initalize(bypass_config=args.bypass_config, bypass_cache=args.bypass_cache, production=args.prod)


if __name__ == "__main__":
    main()
