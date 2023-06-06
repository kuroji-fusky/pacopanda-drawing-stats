"""
Characters CLI Manager

Uses the Redis database to manage characters drawn by Paco

Copyright 2021-2023 Kerby Keith Aquino
MIT License
"""
from argparse import ArgumentParser


def main():
    arg_desc = "Manages characters"

    parser = ArgumentParser(description=arg_desc)

    parser.add_argument('-A', '--add',
                        help="Adds a character",
                        action='store_true')

    parser.add_argument('-L', '--list',
                        help="Lists all the characters",
                        action='store_true')

    parser.add_argument('-R', '--remove',
                        help="Removes a character",
                        action='store_true')


if __name__ == "__main__":
    main()
