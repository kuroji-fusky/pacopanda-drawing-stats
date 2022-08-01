"""
Tag Finder - a script that finds the number of tags present from the entire JSON file
generated from the FurAffinity Scraper.

Licensed under MIT License
"""
import argparse
import json
from random import randint
from concurrent.futures import ThreadPoolExecutor

parser = argparse.ArgumentParser(
    description="Parses any tags from the generated JSON")
parser.add_argument("-t", "--tag", type=str,
                    metavar="<value>", help="Find a specific tags")

args = parser.parse_args()

def main():
    try:
        with open("paco-fa-database.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            tags = []

            for artworks in data["database"]:
                for tags_array in artworks["tags"]:
                    tags.append(tags_array)

            total_count = len(tags)
            results = tags.count(args.tag)

            if args.tag:
                if results == 0:
                    print(f"No results found for tag '{args.tag}'")
                else:
                    print(
                        f"'{args.tag}' returned {results} hits ({results / total_count * 100:.5f}% of {total_count})")
            else:
                random_tag = tags[randint(1, total_count)]
                results = tags.count(random_tag)
                print(
                    f"'{random_tag}' returned {results} hits ({results / total_count * 100:.5f}% of {total_count})")
    except FileNotFoundError:
        print("File not found: could it possibly be moved, deleted, or renamed?")
        exit(1)

with ThreadPoolExecutor(max_workers=50) as f:
    f.map(main, range(10000))
    f.shutdown(wait=True)

if __name__ == "__main__":
    main()