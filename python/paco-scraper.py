from paco_utils import BASE_FA
from paco_utils.parsers import IterateGallery


def main():
	fa_gallery_page = f"{BASE_FA}/gallery/pacopanda/"

	IterateGallery(fa_gallery_page)


if __name__ == "__main__":
	main()
