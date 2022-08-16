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
import time
import subprocess

user_agent = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)"
        "AppleWebKit/537.36 (KHTML, like Gecko)"
        "Chrome/45.0.2454.101 Safari/537.36"
    ),
    "referer": "https://furaffinity.net/",
}

rs = requests.Session()


def main():
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

    with open("updater.json", "r+", encoding="utf-8") as f:
        data = json.load(f)["updater"]

    for i in range(len(data)):
        if re.sub("(Got latest artwork - )", "", data[i]["message"]) == art_data["title"]:
            print(f'"{art_title}" already exists, skipping...')
            data.append({
                "message": f"Skipped {art_title}",
                "time_log": str(datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")),
                "data": {}
            })

            with open("updater.json", "w", encoding="utf-8") as f:
                json.dump({"updater": data}, f, ensure_ascii=False, indent=2)

        else:
            print(f'Found "{art_title}"!')
            data.append({
                "message": f"Got latest artwork - {art_title}",
                "time_log": str(datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")),
                "data": art_data
            })

            with open("updater.json", "w", encoding="utf-8") as f:
                json.dump({"updater": data}, f, ensure_ascii=False, indent=2)

    print(datetime.now().strftime("%m-%d-%Y"))


with ThreadPoolExecutor(max_workers=55) as executor:
    executor.map(main, range(155))

if __name__ == "__main__":
    main()
