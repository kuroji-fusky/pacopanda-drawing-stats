import sys
import argparse

parser = argparse.ArgumentParser(description="The Paco Scraper")

PLATFORMS = ['furaffinity', 'weasyl', 'inkbunny', 'deviantart', 'tumblr']

parser.add_argument(
    "--platform",
    default=PLATFORMS[0],
    const=PLATFORMS[0],
    nargs='?',
    choices=PLATFORMS,
    type=str,
    help='Fetches data from a specific platform, the default is %(default)s')

args = parser.parse_args()


def main():
    print(args.platform)
    # TODO Check cache for iterated pages, continue otherwise
    # fa_art = paco.iterate_pages(
    #     entry_url='https://www.furaffinity.net/gallery/pacopanda',
    #     next_selector='.submission-list .aligncenter .inline:last-child form')
    ...


if __name__ == "__main__":
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    main()
