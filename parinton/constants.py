"""
Constants

Copyright 2022-2023 Kerby Keith Aquino; MIT license
"""
from datetime import datetime

current_date = datetime.now()

base_url: dict[str, str] = {
	"furaffinity": "https://www.furaffinity.net",
	"weasyl": "https://www.weasyl.com",
	"inkbunny": "https://inkbunny.net"
}

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
