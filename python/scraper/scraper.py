import json
import requests
import re
from bs4 import BeautifulSoup

from concurrent.futures import ThreadPoolExecutor
from utils import success_msg

"""Global variables"""
base_url: str = "https://www.furaffinity.net"
user_agent = {
  "User-Agent": (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)"
    "AppleWebKit/537.36 (KHTML, like Gecko)"
    "Chrome/45.0.2454.101 Safari/537.36"
  ),
  "referer": base_url
}
gallery_url = f"{base_url}/gallery/pacopanda"

rs = requests.Session()


def req_soup(url: str):
    req = rs.get(url, headers=user_agent, timeout=None)
    return BeautifulSoup(req.text, "html.parser")


# TODO: Memoize current pages to prevent multiple requests
def get_available_pages():
  current_page: int = 0

  pages_soup = req_soup(f"{gallery_url}/{current_page}/?")
  pages_pagination = pages_soup.find("button", class_="button standard")

  while pages_pagination:
    current_page += 1
    pages_soup = req_soup(f"{gallery_url}/{current_page}/?")
    next_page_url = pages_soup.find("form", {"action": f"/gallery/pacopanda/{current_page + 1}/"})

    if next_page_url is None:
      print(f"Found page {current_page}")
      break

    pages_pagination = pages_soup.find("button", class_="button standard").get_text("Next")
    print(f"Found page {current_page}")
    
  success_msg(f"{current_page} pages found")
  return current_page


paco_db: list = []


def artwork_item(art_id: str):
  artwork_soup = req_soup(f"{base_url}/view/{art_id}")

  # Title
  title_getter = artwork_soup.find(class_="submission-title")
  artwork_title = title_getter.find("p").get_text()

  # Description
  description_getter = artwork_soup.find(class_="submission-description user-submitted-links")
  artwork_description = description_getter.get_text().strip()

  # Date - remote the timestamp and retrieve year via regexp
  date_getter: str = artwork_soup.find("span", class_="popup_date")["title"]

  artwork_date = re.sub(" (\d?\d:\d?\d) ([AP]?M)", "", date_getter)
  artwork_year = re.search("(20\d\d)", date_getter).group(1)

  # Image
  img_getter = artwork_soup.find(class_="submission-area")

  if not img_getter.find("img"):
    artwork_img = "Null, no image or other media"
  else:
    img_getter = artwork_soup.find("img", id="submissionImg")["src"]
    artwork_img = f"https:{img_getter}"

  # Tags
  artwork_tags = set()
  tag_getter = artwork_soup.find_all("span", class_="tags")

  for tag in tag_getter:
    artwork_tag = tag.find("a", {"href": re.compile("/search/*")}).get_text()
    artwork_tags.add(artwork_tag)

  print({
    "title": artwork_title,
    "img_link": artwork_img,
    "date": artwork_date,
    "year": artwork_year,
    "description": artwork_description,
    "tags": artwork_tags,
  })


def main():
  total_pages = get_available_pages()

  """Get 48 artworks through a for loop"""
  for page in range(1, total_pages):
    art_pages_soup = req_soup(f"{gallery_url}/{page}/?")

    art_pages_items = art_pages_soup.find_all("figure", id=re.compile("sid-*"))

    for item in art_pages_items:
      if "id" in item.attrs:
        url_concat = re.sub("sid-", "", item["id"])
        artwork_item(url_concat)


if __name__ == "__main__":
  with ThreadPoolExecutor(max_workers=65) as e:
    e.map(main(), range(165))
