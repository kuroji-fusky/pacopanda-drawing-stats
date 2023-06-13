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

	args = parser.parse_args()

	paco.load_config()

	if args.bypass_cache:
		print('bypassed cache file')


if __name__ == "__main__":
	main()
