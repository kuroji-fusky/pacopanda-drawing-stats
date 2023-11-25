import sys
import argparse
import parinton as paco

parser = argparse.ArgumentParser(description="The Paco Scraper")

# TODO consolidate these into values instead of args
parser.add_argument("--furaffinity", action="store_true")
parser.add_argument("--weasyl", action="store_true")
parser.add_argument("--inkbunny", action="store_true")
parser.add_argument("--deviantart", action="store_true")
parser.add_argument("--tumblr", action="store_true")


def main():
    # TODO Check cache for iterated pages, continue otherwise
    fa_art = paco.iterate_pages(
        entry_url='https://www.furaffinity.net/gallery/pacopanda',
        next_selector='.submission-list .aligncenter .inline:last-child form')


if __name__ == "__main__":
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    main()
