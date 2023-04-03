"""
P2DS - Constants

Copyright 2022-2023 Kerby Keith Aquino; MIT license
"""
import requests
from datetime import datetime

rs = requests.Session()
current_date = datetime.now()

# Base URLs
BASE_FA = "https://www.furaffinity.net"
BASE_WS = "https://www.weasyl.com"
BASE_IB = "https://inkbunny.net"

# Ignored Tags
# noinspection SpellCheckingInspection
__common = [
	"furry",
	"anthro",
	"cute",
	"lounge",
	"lounging",
	"summer",
	"music",
	"sky"
]

__species = [
	"fox",
	"dog",
	"wolf",
	"otter",
	"tiger",
	"bear"
]

ignored_tags: list[str] = [*__common, *__species]
