from paco_utils.constants import BASE_FA, BASE_WS, BASE_IB
from paco_utils.parsers import IterateGallery


def main():
	fa_page = f"{BASE_FA}/gallery/pacopanda/"
	ws_page = f"{BASE_WS}/submissions/pandapaco"
	ib_page = f"{BASE_IB}/gallery/pandapaco/"

	# for gl_page in [fa_gallery_page, ws_gallery_page, ib_gallery_page]:
	# 	IterateGallery(gl_page)

	IterateGallery(ws_page)

if __name__ == "__main__":
	main()
