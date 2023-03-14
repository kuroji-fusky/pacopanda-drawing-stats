from utils import SubmissionParser, give_me_soup

FA_BASE = "https://www.furaffinity.net"
BASE_URL = f"{FA_BASE}/gallery/pacopanda"

UA = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)"
        "AppleWebKit/537.36 (KHTML, like Gecko)"
        "Chrome/45.0.2454.101 Safari/537.36"
    ),
    "referer": BASE_URL
}


def main():
    gallery_page = give_me_soup(BASE_URL)
    first_artwork = gallery_page.select_one('figure')

    first_artwork_link = first_artwork.find("a")['href']
    first_artwork_link = f"{FA_BASE}{first_artwork_link}"

    SubmissionParser(first_artwork_link).tags()


if __name__ == "__main__":
    main()
