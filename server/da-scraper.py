# ==============================================================================
# This script scraps Paco's gallery from DeviantArt and saves it to a JSON file.
# ==============================================================================

import requests
import json
import codecs
# import pandas as pandapaco
import re
from bs4 import BeautifulSoup

total_pages = 1

HEADERS = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)' 
                          'AppleWebKit/537.36 (KHTML, like Gecko)'
                          'Chrome/45.0.2454.101 Safari/537.36'),
                          'referer': 'https://furaffinity.net/'}

paco_db = {}