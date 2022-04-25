import json
import sys
import re
import os
import requests
from colorama import *
from bs4 import BeautifulSoup

init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream

total_pages = 1

print(f"{Back.YELLOW}{Fore.LIGHTWHITE_EX}{Style.BRIGHT} Assigned pages - {total_pages} {Style.RESET_ALL}")

user_agent = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)' 
                          'AppleWebKit/537.36 (KHTML, like Gecko)'
                          'Chrome/45.0.2454.101 Safari/537.36'),
                          'referer': 'https://furaffinity.net/'}

paco_db = {}

def save_json():
  with open("paco-fa-database.json", 'w', encoding="utf-8") as paco_db_append:
    json.dump(paco_db, paco_db_append, ensure_ascii=False)
    
# def sanitize_json():
#   with open("paco-fa-database.json", 'r', encoding="utf-8") as paco_db_load:
#     paco_db = json.load(paco_db_load)
#     for key, value in paco_db.items():
#       paco_db[key] = re.sub(r'[^\x00-\x7F]+', '', value)
#     save_json()

# Get 48 artworks through a for loop in each pages
for page in range(1, total_pages + 1):
  paco_db.update({page: []})
  find_art = requests.get(f"https://furaffinity.net/gallery/pacopanda/{page}/?", headers=user_agent, timeout=None)
  parse_art = BeautifulSoup(find_art.text, 'html.parser')
  parse_art = parse_art.find_all('figure', {'id': re.compile("sid-*")})

  for sid in parse_art:
    if 'id' in sid.attrs:
      sid_concat = re.sub('sid-', '', sid['id'])
      find_art_id = requests.get(f"https://furaffinity.net/view/{sid_concat}/", headers=user_agent, timeout=None)
      find_art_id_secs = find_art_id.elapsed.total_seconds()
      parse_art_id = BeautifulSoup(find_art_id.text, 'html.parser')

      # Get title
      find_title = parse_art_id.find('div', {'class': 'submission-title'})
      art_title = find_title.find('p').get_text()

      # Get image
      detect_img = parse_art_id.find('div', {'class': 'aligncenter submission-area'})

      if detect_img.find('img'):
        art_image = parse_art_id.find('img', {'id': 'submissionImg'})['src']
        art_image = f'https:{art_image}'

      # If no image is detected (i.e. video or flash content); then return null
      else:
        art_image = 'Null, item requested is anything other than an image.'

      # Get date
      art_date = parse_art_id.find('span', {'class': 'popup_date'})['title']
      # print(art_date)

      # TODO: filter only date using regex
      # art_date = parse_art_id.find('span', {'title': re.compile(r" ([0-9]?[0-9]:[0-9]?[0-9]) ([AP]?M)")})

      # Get tags
      tags_array = set()
      art_tags = parse_art_id.find_all('span', {'class', 'tags'})
      
      for tags in art_tags:
        art_tag = tags.find('a', {'href': re.compile('/search/*')}).get_text()
        tags_array.add(art_tag)

      # Find description
      art_desc = parse_art_id.find(
          'div', {'class': 'submission-description user-submitted-links'}).get_text().strip()

      # Attach to a JSON file
      paco_db[page].append({
        'name': art_title,
        "description": art_desc,
        'date': art_date,
        'link': art_image,
        "tags": list(tags_array),
      })
      
      print('')
      print('===========')
      print('')
      print(f"Appended \"{art_title}\"!")
      if find_art_id_secs > 20:
        print(f"{Back.RED}{Fore.LIGHTWHITE_EX}{Style.BRIGHT}[⚠️] Took {find_art_id_secs} sec(s) to complete.{Style.RESET_ALL}")
        print(f"{Back.RED}{Fore.LIGHTWHITE_EX}{Style.BRIGHT}[⚠️] WARNING: If it's taking longer than 20 seconds to send a HTTP request {Style.RESET_ALL}\n{Back.RED}{Fore.LIGHTWHITE_EX}{Style.BRIGHT}[⚠️] then it would've been most likely due to slow or unstable connection. {Style.RESET_ALL}\n{Back.RED}{Fore.LIGHTWHITE_EX}{Style.BRIGHT}[⚠️] If this happens, it'll retry from the beginning due to {Style.RESET_ALL}\n{Back.RED}{Fore.LIGHTWHITE_EX}{Style.BRIGHT}[⚠️] a connection timeout. {Style.RESET_ALL}")
      elif find_art_id_secs > 10:
        print(f"{Back.YELLOW}{Fore.LIGHTWHITE_EX}{Style.BRIGHT}[⚠️] Took {find_art_id_secs} sec(s) to complete.{Style.RESET_ALL}")
      else:
        print(f"{Back.GREEN}{Fore.LIGHTWHITE_EX}{Style.BRIGHT}[✔️] Took {find_art_id_secs} sec(s) to complete.{Style.RESET_ALL}")

      print('')
      print(f"ID: {sid_concat}\nLink: {art_image}\nTags: {tags_array}")
      save_json()

# sanitize_json()
print(f"\n{Back.GREEN}{Style.BRIGHT} DONE! {Back.RESET}\n")
