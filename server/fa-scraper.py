"""
Paco Panda FurAffinity Scraper

Licensed under MIT License
"""
from colorama import *
from bs4 import BeautifulSoup
import argparse
import json
import sys
import re
import requests
import time

# Colorama stuff
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream

# Begin timer when script starts
exec_start = time.time()

# Arg parse stuff for passing args on terminal
parser = argparse.ArgumentParser(description="Scrape drawing stats from FA")
parser.add_argument('-p', '--pages', type=int, metavar="<pages>", help="Specify the number of pages to scrape")
parser.add_argument('-nv', '--no-verbose', action="store_true", help="Keep the output minimal")
args = parser.parse_args()

user_agent = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)'
                             'AppleWebKit/537.36 (KHTML, like Gecko)'
                             'Chrome/45.0.2454.101 Safari/537.36'),
              'referer': 'https://furaffinity.net/'}

"""
NOTE: The `total_pages` variable is used to keep track of the number of 
pages that are going to be scraped. But it's important to know that it
can be really confusing to have the *actual* number of pages scraped.

Because passing `-p 1` will terminate the script immediately, and the only
workaround is it had to be increased by one due to a for loop range, but
decremented by one on print statements. 
"""
total_pages = 0
paco_db = []
page_requests = requests.get(f"https://furaffinity.net/gallery/pacopanda/{total_pages}/?", headers=user_agent, timeout=30)

def save_json():
    with open("paco-fa-database.json", 'w', encoding="utf-8") as paco_db_append:
        json.dump({"database": paco_db}, paco_db_append, ensure_ascii=False)

try:
    if args.pages:
        total_pages = args.pages + 1
        print(f"{Back.YELLOW}{Fore.LIGHTWHITE_EX}{Style.BRIGHT} Assigned pages - {total_pages - 1} {Style.RESET_ALL}")

    else:
        print(
            f"{Back.YELLOW}{Fore.LIGHTWHITE_EX}{Style.BRIGHT} --pages flag was not used, finding all pages available {Style.RESET_ALL}")

        parse_pages = BeautifulSoup(page_requests.text, 'html.parser')
        parse_pages = parse_pages.find('button', {'type': 'submit'}).get_text("Next")

        while parse_pages:
            total_pages += 1
            page_requests = requests.get(f"https://furaffinity.net/gallery/pacopanda/{total_pages}/?", headers=user_agent, timeout=30)
            parse_pages = BeautifulSoup(page_requests.text, 'html.parser')
            parse_pages = parse_pages.find('form', {'method': 'get', 'action': f'/gallery/pacopanda/{total_pages + 1}/'})
            """
            The code above throws an error when the "Next" button is not found (the last page)
            If this error was thrown, break the loop and we'll have the number of `total_pages` collected!
            """
            if parse_pages is None:
                break

            parse_pages = parse_pages.find(
                'button', {'type': 'submit'}).get_text("Next")

            print(f"\rFound page {total_pages} - took {round(page_requests.elapsed.total_seconds(), 3)}s")

        print(f"{total_pages} pages found!")

    """
    Get 48 artworks through a for loop in each pages
    """
    for page in range(1, total_pages):
        find_art = requests.get(f"https://furaffinity.net/gallery/pacopanda/{page}/?", headers=user_agent, timeout=30)
        parse_art = BeautifulSoup(find_art.text, 'html.parser')
        parse_art = parse_art.find_all('figure', {'id': re.compile("sid-*")})

        for art_id in parse_art:
            if 'id' in art_id.attrs:
                art_id_concat = re.sub('sid-', '', art_id['id'])
                page_requests_art = requests.get(f"https://furaffinity.net/view/{art_id_concat}/?", headers=user_agent, timeout=30)
                find_art_secs = page_requests_art.elapsed.total_seconds()
                parse_art_id = BeautifulSoup(page_requests_art.text, 'html.parser')

                # Get title
                find_title = parse_art_id.find('div', class_='submission-title')
                art_title = find_title.find('p').get_text()

                # Get image
                detect_img = parse_art_id.find('div', class_='aligncenter submission-area')

                if detect_img.find('img'):
                    art_image_get = parse_art_id.find('img', id='submissionImg')['src']
                    art_image = f'https:{art_image_get}'

                # If no image is detected (i.e. video or flash content); then return null
                else:
                    art_image = 'Null, item requested is anything other than an image.'

                # Get date and remove the timestamp via regex
                art_date_get = parse_art_id.find('span', class_='popup_date')['title']
                art_date = re.sub(" (\d?\d:\d?\d) ([AP]?M)", "", str(art_date_get))

                # Get tags
                tags_array = set()
                art_tags = parse_art_id.find_all('span', class_='tags')

                for tags in art_tags:
                    art_tag = tags.find(
                        'a', {'href': re.compile('/search/*')}).get_text()
                    tags_array.add(art_tag)

                # Get description
                art_desc = parse_art_id.find(
                    'div', class_='submission-description user-submitted-links').get_text().strip()

                # Attach to a JSON file
                paco_db.append({
                    'name': art_title,
                    "description": art_desc,
                    "date": str(art_date),
                    'link': art_image,
                    "tags": list(tags_array),
                })

            percentage = f"{(page / total_pages * 100):.2f}%"
            exec_stop = time.time()

            if args.no_verbose:
                print(f"{page}/{total_pages} page(s) ({percentage}) | Found \"{art_title}\"")

            else:
                print(f"\nCurrently on page(s) {page} of {total_pages} ({percentage})")
                print(f"Added \"{art_title}\"")
                print(f"{exec_stop - exec_start:.1f}s")

                if find_art_secs > 10:
                    print(f"{Fore.RED}{Style.BRIGHT}Took {find_art_secs}s{Style.RESET_ALL}")
                elif find_art_secs > 5:
                    print(f"{Fore.YELLOW}{Style.BRIGHT}Took {find_art_secs}s{Style.RESET_ALL}")
                else:
                    print(f"{Fore.GREEN}{Style.BRIGHT}Took {find_art_secs}s{Style.RESET_ALL}")

        print(f"\n{Fore.GREEN}{Style.BRIGHT}Finished on page {page}{Style.RESET_ALL}")
        save_json()

    print(f"{Fore.LIGHTWHITE_EX}{Back.GREEN}{Style.BRIGHT} === DONE! === {Back.RESET}")
    exec_stop = time.time()
    print(f"Script took {exec_stop - exec_start:.2f}(s) to run.")
    
except KeyboardInterrupt:
    exec_stop = time.time()
    print(f"Stopped by user! - script took {exec_stop - exec_start:.2f}(s) to run.")