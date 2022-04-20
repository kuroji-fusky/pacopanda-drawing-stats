# ==============================================================================
# This script scraps Paco's gallery from FurAfinity and saves it to a JSON file.
# ==============================================================================

import json
import codecs
import re
import requests
from bs4 import BeautifulSoup

total_pages = 1

HEADERS = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)' 
                          'AppleWebKit/537.36 (KHTML, like Gecko)'
                          'Chrome/45.0.2454.101 Safari/537.36'),
                          'referer': 'https://furaffinity.net/'}

paco_db = {}

# Save to JSON
def save_json():
  with open("paco-fa-database.json", 'w', encoding="utf-8") as paco_db_append:
    json.dump(paco_db, paco_db_append, ensure_ascii=False)

# Get 48 artworks through a for loop in each pages
for page in range(1, total_pages + 1):
  paco_db.update({page: []})
  find_art = requests.get(f"https://furaffinity.net/gallery/pacopanda/{page}/?", headers=HEADERS, timeout=5)
  parse_art = BeautifulSoup(find_art.text, 'html.parser')
  parse_art = parse_art.find_all('figure', {'id': re.compile("sid-*")})

  for sid in parse_art:
    if 'id' in sid.attrs:
      sid_concat = re.sub('sid-', '', sid['id'])
      find_art_id = requests.get(f"https://furaffinity.net/view/{sid_concat}/", headers=HEADERS, timeout=5)
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
      
      print("=====")
      print(f"Appended \"{art_title}\" - {art_date}")
      print("=====")
      print(f"Took {find_art_id_secs} seconds to load.")
      print(f"More info: Currently on page {page} of {total_pages}, with {len(paco_db[page])} artworks.")
      save_json()
  
  print("=====")
  print("Appended page to the JSON file!")    
  print("=====")

print("=====")
print("DONE!")
print("=====")
