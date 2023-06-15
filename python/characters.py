"""
Characters CLI Manager

Uses the Redis database to manage characters drawn by Paco

Copyright 2021-2023 Kerby Keith Aquino
MIT License
"""
from argparse import ArgumentParser

from parinton.parsers import paco_chars


def main():
    arg_desc = "Manages characters from the database"

    parser = ArgumentParser(description=arg_desc)

    parser.add_argument('-a', 'add',
                        help="Adds a character",
                        action='store_true')

    parser.add_argument('-l', 'list',
                        help="Lists all the characters",
                        action='store_true')

    parser.add_argument('-R', 'remove',
                        help="Removes a character",
                        action='store_true')

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

    paco_chars.bootstrap(bypass_config=args.bypass_config, bypass_cache=args.bypass_cache)


if __name__ == "__main__":
    main()
