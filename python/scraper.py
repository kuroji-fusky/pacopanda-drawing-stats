"""
Scraper

Scrapes public drawing data from Paco Panda

Copyright 2021-2023 Kerby Keith Aquino
MIT License
"""
import argparse
import multiprocessing

from parinton import Parinton


def main():
	arg_desc = "Scrapes and parses Paco art from FurAffinity, Weasyl, and InkBunny"
	parser = argparse.ArgumentParser(description=arg_desc)

	parser.add_argument('-u', '--update',
						help="Updates the latest artwork",
						action='store_true')

	parser.add_argument('--update-local',
						help="Updates the latest artwork",
						action='store_true')

	parser.add_argument('-m', '--minimal',
						help="Minimizes console input and only prints required info"
							 " (i.e. artwork title, current page, etc.)",
						action='store_true')

	parser.add_argument('-p', '--production',
						help="Launches the server in production mode",
						action='store_true')

	parser.add_argument('--cron',
						help="Only used for cron jobs, or task scheduler jobs for Windows",
						action='store_true')
	
	paco = Parinton()

	paco.check_cache()


if __name__ == "__main__":
	main()
