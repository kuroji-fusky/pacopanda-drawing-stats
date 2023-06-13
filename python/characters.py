"""
Characters CLI Manager

Uses the Redis database to manage characters drawn by Paco

Copyright 2021-2023 Kerby Keith Aquino
MIT License
"""
from parinton import paco
from argparse import ArgumentParser


def main():
    arg_desc = "Manages characters from the database"

    parser = ArgumentParser(description=arg_desc)

    parser.add_argument('-a', '--add',
                        help="Adds a character",
                        action='store_true')

    parser.add_argument('-l', '--list',
                        help="Lists all the characters",
                        action='store_true')

    parser.add_argument('-R', '--remove',
                        help="Removes a character",
                        action='store_true')

    parser.add_argument('--bypass-config',
                        help="Bypasses config for connecting to Redis",
                        action='store_true')

    parser.add_argument('--bypass-cache',
                        help="Bypasses cache file",
                        action='store_true')

    args = parser.parse_args()

    paco.initalize(bypass_config=args.bypass_config, bypass_cache=args.bypass_cache)


if __name__ == "__main__":
    main()
