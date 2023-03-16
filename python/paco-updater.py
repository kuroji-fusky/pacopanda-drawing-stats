from paco_utils import BASE_FA, give_me_soup, update_json
from paco_utils.constants import current_date
from paco_utils.logger import info
from paco_utils.parsers import SubmissionParser


def main():
	info("Updating data from FA")

	gallery_page = give_me_soup(f"{BASE_FA}/gallery/pacopanda")
	first_artwork = gallery_page.select_one('figure')

	first_artwork_link = first_artwork.find("a")['href']
	first_artwork_link = f"{BASE_FA}{first_artwork_link}"

	artwork = SubmissionParser(first_artwork_link)

	data = {
		"retrieved": current_date,
		"title": artwork.title(),
		"description": artwork.description(),
		"img": artwork.img(),
		"link": first_artwork_link,
		"date": artwork.date(),
	}

	info(f'Retrieved "{data["title"]}"')
	update_json("fa-art-tl.json", data)


if __name__ == "__main__":
	main()
