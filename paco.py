"""
P2DS - Paco Scraper

Copyright 2022-2023 Kerby Keith Aquino; MIT license
"""
import argparse
import time

from paco_utils.base import PacoClubhouse
from paco_utils.constants import current_date
from paco_utils.logger import ColorLogger
from paco_utils.parsers import IterateGallery, SubmissionParser

arg_desc = "Scrapes and parses Paco art from FurAffinity, Weasyl, and InkBunny"

parser = argparse.ArgumentParser(description=arg_desc)

parser.add_argument('-u', '--update',
					help="Updates the latest artwork",
					action='store_true')

parser.add_argument('-nv', '--no-verbose',
					help="Minimizes console input and only prints required info"
						 " (i.e. artwork title, current page, etc.)",
					action='store_true')

parser.add_argument('--cron',
					help="Only used for cron jobs",
					action='store_true')

args = parser.parse_args()


def main():
	logger = ColorLogger(prefix="Updater")
	base = PacoClubhouse()

	fa_url = base.b_furaffinity
	ws_url = base.b_weasyl
	ib_url = base.b_inkbunny

	if args.update:
		logger.info("Updating data from FA")

		gallery_page = base.soup_req(f"{fa_url}/gallery/pacopanda")
		first_artwork = gallery_page.select_one('figure')

		first_artwork_link = first_artwork.find("a")['href']
		first_artwork_link = f"{fa_url}{first_artwork_link}"

		artwork = SubmissionParser(url=first_artwork_link)

		data: dict[str, str | list[str]] = {
			"title": artwork.title,
			"description": artwork.description,
			"img": artwork.img,
			"link": first_artwork_link,
			"date": artwork.date.isoformat(),
			"tags": artwork.tags,
			"retrieved": current_date.isoformat(),
		}

		logger.info(f'Retrieved "{data["title"]}"')
		time.sleep(1)
		base.update_json("fa-art-tl.json", data, time_series=True)

	else:
		fa_page = f"{fa_url}/gallery/pacopanda/"
		ws_page = f"{ws_url}/submissions/pandapaco"
		ib_page = f"{ib_url}/gallery/pandapaco/"

		# TODO	1) parsed with '--all' or '-A' argument
		# TODO	2) for certain platforms: it's parsed with either of the ff:
		# TODO 		'--platform' or '-pf'
		# TODO		args & default: 'fa' or 'furaffinity'
		# TODO		args: 'ws' or 'weasyl'
		# TODO		args: 'ib' or 'inkbunny'

		# for gl_page in [fa_gallery_page, ws_gallery_page, ib_gallery_page]:
		# 	IterateGallery(gl_page)
		IterateGallery(ws_page)


if __name__ == "__main__":
	main()
