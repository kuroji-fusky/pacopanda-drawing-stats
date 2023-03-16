"""
Panda Paco Utils

Copyright 2022-2023 Kerby Keith Aquino; MIT license
"""
import requests
from datetime import datetime

BASE_FA = "https://www.furaffinity.net"
BASE_WS = "https://www.weasyl.com"
BASE_IB = "https://inkbunny.net"

rs = requests.Session()
current_date = datetime.now()
