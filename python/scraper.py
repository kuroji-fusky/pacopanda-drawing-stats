import parinton


def main():
    parinton.iterate_pages(
        entry_url='https://www.furaffinity.net/gallery/pacopanda',
        next_selector='.submission-list .aligncenter .inline:last-child form')


if __name__ == "__main__":
    main()
