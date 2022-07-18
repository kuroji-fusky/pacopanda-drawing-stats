from colorama import *
from bs4 import BeautifulSoup
import concurrent.futures
import argparse
import json
import sys
import re
import requests

# Colorama stuff
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream

# Arg parse stuff for passing args on terminal
parser = argparse.ArgumentParser(description="Scrape drawing stats from FA")
parser.add_argument('-p', '--pages', type=int, metavar="<pages>",
                    help="Specify the number of pages to scrape")
parser.add_argument('-nv', '--no-verbose', action="store_true",
                    help="Keep the output quiet and c l e a n")
args = parser.parse_args()

user_agent = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)'
                             'AppleWebKit/537.36 (KHTML, like Gecko)'
                             'Chrome/45.0.2454.101 Safari/537.36'),
              'referer': 'https://furaffinity.net/'}

# The scraper stuff
paco_db = []
total_pages = 0
find_page = requests.get(
    f"https://furaffinity.net/gallery/pacopanda/{total_pages}/?", headers=user_agent, timeout=None)

if args.pages:
    total_pages = args.pages
    print(f"{Back.YELLOW}{Fore.LIGHTWHITE_EX}{Style.BRIGHT} Assigned pages - {total_pages} {Style.RESET_ALL}")

else:
    print(
        f"{Back.YELLOW}{Fore.LIGHTWHITE_EX}{Style.BRIGHT} No value for pages specified. Recursively finding all pages... {Style.RESET_ALL}")

    parse_pages = BeautifulSoup(find_page.text, 'html.parser')
    parse_pages = parse_pages.find(
        'button', {'type': 'submit'}).get_text("Next")

    while parse_pages:
        total_pages += 1
        find_page = requests.get(
            f"https://furaffinity.net/gallery/pacopanda/{total_pages}/?", headers=user_agent, timeout=None)
        parse_pages = BeautifulSoup(find_page.text, 'html.parser')
        parse_pages = parse_pages.find(
            'form', {'method': 'get', 'action': f'/gallery/pacopanda/{total_pages+1}/'})
        """
        The code above throws an error when the "Next" button is not found (the last page)
        If this error was thrown, break the loop and we'll have the number of total_pages collected!
        """
        if parse_pages is None:
            break

        parse_pages = parse_pages.find(
            'button', {'type': 'submit'}).get_text("Next")

        print(f"Found page {total_pages}\r")

    print(f"{total_pages} pages found!")


def save_json():
    with open("paco-fa-database.json", 'w', encoding="utf-8") as paco_db_append:
        json.dump({"database": paco_db}, paco_db_append, ensure_ascii=False)


"""
Get 48 artworks through a for loop in each pages
"""
for page in range(0, total_pages):
    parse_art = BeautifulSoup(find_page.text, 'html.parser')
    parse_art = parse_art.find_all('figure', {'id': re.compile("sid-*")})

    for art_id in parse_art:
        if 'id' in art_id.attrs:
            art_id_concat = re.sub('sid-', '', art_id['id'])
            find_page = requests.get(
                f"https://furaffinity.net/view/{art_id_concat}/", headers=user_agent, timeout=None)
            find_page_id_secs = find_page.elapsed.total_seconds()
            parse_art_id = BeautifulSoup(find_page.text, 'html.parser')

            # Get title
            find_title = parse_art_id.find(
                'div', {'class': 'submission-title'})
            art_title = find_title.find('p').get_text()

            # Get image
            detect_img = parse_art_id.find(
                'div', {'class': 'aligncenter submission-area'})

            if detect_img.find('img'):
                art_image = parse_art_id.find(
                    'img', {'id': 'submissionImg'})['src']
                art_image = f'https:{art_image}'

            # If no image is detected (i.e. video or flash content); then return null
            else:
                art_image = 'Null, item requested is anything other than an image.'

            # Get date
            art_date = parse_art_id.find(
                'span', {'class': 'popup_date'})['title']
            # print(art_date)

            # TODO: filter only date using regex
            # TODO: art_date = parse_art_id.find('span', {'title': re.compile(r" ([0-9]?[0-9]:[0-9]?[0-9]) ([AP]?M)")})

            # Get tags
            tags_array = set()
            art_tags = parse_art_id.find_all('span', {'class', 'tags'})

            for tags in art_tags:
                art_tag = tags.find(
                    'a', {'href': re.compile('/search/*')}).get_text()
                tags_array.add(art_tag)

            # Find description
            art_desc = parse_art_id.find(
                'div', {'class': 'submission-description user-submitted-links'}).get_text().strip()

            # Attach to a JSON file
            paco_db.append({
                'name': art_title,
                "description": art_desc,
                'date': art_date,
                'link': art_image,
                "tags": list(tags_array),
            })

        if args.no_verbose:
            print(f"{page+1}/{total_pages} page(s) | Appended \"{art_title}\"!")

        else:
            print(f"\nCurrently on page(s) {page+1} of {total_pages}")
            print(f"Appended \"{art_title}\"")

            if find_page_id_secs > 20:
                print(
                    f"{Fore.RED}{Style.BRIGHT}⚠️ Took {find_page_id_secs} sec(s) to complete.{Style.RESET_ALL}")
            elif find_page_id_secs > 10:
                print(
                    f"{Fore.YELLOW}{Style.BRIGHT}⚠️ Took {find_page_id_secs} sec(s) to complete.{Style.RESET_ALL}")
            else:
                print(
                    f"{Fore.GREEN}{Style.BRIGHT}✔️ Took {find_page_id_secs} sec(s) to complete.{Style.RESET_ALL}")

print(f"\n{Fore.GREEN}{Style.BRIGHT}✔️ Finished!{Style.RESET_ALL}")
print("\nSaving JSON file...")
# print(paco_db)
save_json()

print(f"{Fore.LIGHTWHITE_EX}{Back.GREEN}{Style.BRIGHT} === DONE! === {Back.RESET}")
