"""
Paco Panda DeviantArt Drafts scraper

Another test script since DeviantArt heavily relies on JavaScript to serve
HTML to the browser thanks to React as their frontend.
"""

import time
from concurrent.futures import ThreadPoolExecutor

exec_start = time.perf_counter()

user_agent = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)"
        "AppleWebKit/537.36 (KHTML, like Gecko)"
        "Chrome/50.0.2661.102 Safari/537.36"
    ),
    "referer": "https://www.deviantart.com/",
}

paco_db = []

def main():
    url = "https://deviantart.com/pacopanda/gallery/scraps"

with ThreadPoolExecutor(max_workers=55) as executor:
    executor.map(main, range(155))
    
if __name__ == "__main__":
    main()