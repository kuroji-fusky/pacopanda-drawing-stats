"""
Paco Daily Self-Updater

Licensed under MIT License
"""
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import requests
import re
import json
import subprocess

user_agent = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)"
        "AppleWebKit/537.36 (KHTML, like Gecko)"
        "Chrome/45.0.2454.101 Safari/537.36"
    ),
    "referer": "https://furaffinity.net/"
}

rs = requests.Session()

time_log = str(datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"))


def append_data(can_append: bool):
    if can_append is False:
        return {
            "message": f"No data provided: either the latest artwork already exists or has been skipped.",
            "time_log": time_log,
            "data": {}
        }

    return {
        "message": f"Got latest artwork - {art_title}",
        "time_log": time_log,
        "data": art_data
    }


def main():
    global art_title
    global art_data

    print("Grabbing the latest and greatest")

    url = rs.get("https://furaffinity.net/gallery/pacopanda/",
                 headers=user_agent, timeout=5)
    soup_parse = BeautifulSoup(url.text, "html.parser")

    latest_art = soup_parse.find("figure", id=re.compile("sid-*"))
    latest_art_url = latest_art.find("a")["href"]

    artwork_page = rs.get(
        f"https://furaffinity.net{latest_art_url}", headers=user_agent, timeout=5)
    soup_parse = BeautifulSoup(artwork_page.text, "html.parser")

    art_title = soup_parse.find(
        "div", class_="submission-title").find("p").get_text()

    art_img = "https:" + soup_parse.find("img", id="submissionImg")["src"]

    art_date_get = soup_parse.find("span", class_="popup_date")["title"]
    art_date = re.sub(" (\d?\d:\d?\d) ([AP]?M)", "", str(art_date_get))

    art_year = re.search("(\d\d\d\d)", art_date).group(1)

    art_data = {
        "title": art_title,
        "image": art_img,
        "date": art_date,
        "year": art_year,
    }

    try:
        with open("updater.json", "r+", encoding="utf-8") as f:
            drawing_data = json.load(f)["updater"]

        for i in range(len(drawing_data)):
            if re.sub("(Got latest artwork - )", "", drawing_data[i]["message"]) == art_data["title"]:
                print("Artwork already exists - skipping")
                drawing_data.append(append_data(False))
                with open("updater.json", "w", encoding="utf-8") as f:
                    json.dump({"updater": drawing_data}, f,
                              ensure_ascii=False, indent=2)
                return

            print(f"{art_title} added!")
            drawing_data.append(append_data(True))
            with open("updater.json", "w", encoding="utf-8") as f:
                json.dump({"updater": drawing_data}, f,
                          ensure_ascii=False, indent=2)
            return

    except FileNotFoundError:
        print("File doesn't exist! Creating one...")
        with open("updater.json", "w", encoding="utf-8") as f:
            json.dump({"updater": [append_data(True)]},
                      f, ensure_ascii=False, indent=2)


with ThreadPoolExecutor(max_workers=55) as executor:
    executor.map(main, range(155))

if __name__ == "__main__":
    main()
