"""
Paco Scraper Script

Copyright 2022-2023 Kerby Keith Aquino; MIT license
"""
import argparse
import time

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from parinton.base import Parinton
from parinton.constants import current_date
from parinton.logger import ColorLogger
from parinton.parsers import IterateGallery, SubmissionParser


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

    args = parser.parse_args()

    logger = ColorLogger(prefix="Updater")
    base = Parinton()

    fa_url, ws_url, ib_url = base.b_furaffinity, base.b_weasyl, base.b_inkbunny

    if args.update:
        logger.note("Logger set")
        logger.info("Updating data from FA")
        gallery_page = base.soup_req(f"{fa_url}/gallery/pacopanda")

        first_artwork = gallery_page.select_one('figure')

        first_artwork_link = first_artwork.find("a")['href']
        first_artwork_link = f"{fa_url}{first_artwork_link}"

        artwork = SubmissionParser(url=first_artwork_link)

        data = artwork.parse(include_retrieved_item=True)
        print(data)

        data_old: dict[str, str | list[str]] = {
            "title": artwork.title,
            "description": artwork.description,
            "img": artwork.img,
            "link": first_artwork_link,
            "date": artwork.date.isoformat(),
            "tags": artwork.tags,
            "retrieved": current_date.isoformat(),
        }

        logger.info(f'Retrieved "{data_old["title"]}"')
        time.sleep(1)
        base.update_json("fa-art-tl.json", data_old, time_series=True)

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
