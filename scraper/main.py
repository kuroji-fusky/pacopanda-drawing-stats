import json
import requests
import re
from bs4 import BeautifulSoup

from concurrent.futures import ThreadPoolExecutor
from utils import success_msg, error_msg

"""Global variables"""
base_url: str = "https://www.furaffinity.net"
user_agent = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)"
        "AppleWebKit/537.36 (KHTML, like Gecko)"
        "Chrome/45.0.2454.101 Safari/537.36"
    ), "referer": base_url
}
gallery_url = f"{base_url}/gallery/pacopanda"


def req(url: str):
    rs = requests.Session()
    return rs.get(url, headers=user_agent, timeout=None)


total_pages: int = 0


def get_available_pages():
    global total_pages  # This is generally a bad idea, but screw it lol
    current_page: int = 0

    pages_req = req(f"{gallery_url}/{current_page}/?")
    pages_soup = BeautifulSoup(pages_req.text, "html.parser")
    pages_pagination = pages_soup.find("button", class_="button standard")

    while pages_pagination:
        current_page += 1
        pages_req = req(f"{gallery_url}/{current_page}/?")
        pages_soup = BeautifulSoup(pages_req.text, "html.parser")
        next_page_url = pages_soup.find("form", {"action": f"/gallery/pacopanda/{current_page + 1}/"})

        if next_page_url is None:
            print(f"Find last page - {current_page}")
            break

        pages_pagination = pages_soup.find("button", class_="button standard").get_text("Next")
        print(f"Found page {current_page}")

    total_pages = current_page
    success_msg(f"{current_page} pages found")


paco_db: list = []


def main():
    get_available_pages()

    """Get 48 artworks through a for loop"""
    for page in range(1, total_pages):
        artwork_req = req(f"{gallery_url}/{page}/?")
        artwork_soup = BeautifulSoup(artwork_req.text, "html.parser")

        artwork_items = artwork_soup.find_all("figure", id=re.compile("sid-*"))

        for item in artwork_items:
            if "id" in item.attrs:
                url_concat = re.sub("sid-", "", item["id"])
                item_req = req(f"{base_url}/view/{url_concat}")
                item_soup = BeautifulSoup(item_req.text, "html.parser")

                # Title
                title_getter = item_soup.find(class_="submission-title")
                item_title = title_getter.find("p").get_text()

                # Description
                description_getter = item_soup.find(class_="submission-description user-submitted-links")
                item_description = description_getter.get_text().strip()

                # Date - remote the timestamp and retrieve year via regexp
                date_getter: str = item_soup.find("span", class_="popup_date")["title"]

                item_date = re.sub(" (\d?\d:\d?\d) ([AP]?M)", "", date_getter)
                item_year = re.search("(20\d\d)", date_getter).group(1)

                # Image
                img_getter = item_soup.find(class_="submission-area")
                if not img_getter.find("img"):
                    item_img = "Null, no image or other media"
                else:
                    img_getter = item_soup.find("img", id="submissionImg")["src"]
                    item_img = f"https:{img_getter}"

                # Tags
                item_tags = set()

                tag_getter = item_soup.find_all("span", class_="tags")

                for tag in tag_getter:
                    item_tag = tag.find("a", {"href": re.compile("/search/*")}).get_text()
                    item_tags.add(item_tag)

                print(
                    f"Title: {type(item_title)} | {item_title} \n",
                    f"Desc : {type(item_description)} | [omitted] \n",
                    f"Date : {type(item_date)} | {item_date} \n",
                    f"Tags : {type(item_tags)} | {item_tags} \n",
                    f"Link : {type(item_img)} | {item_img} \n",
                    f"Year : {type(item_year)} | {item_year} \n",
                )


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=65) as e:
        e.map(main(), range(165))
