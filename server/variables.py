def user_agent(ref: str = "https://furaffinity.net/"):
    global user_agent
    user_agent = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)"
            "AppleWebKit/537.36 (KHTML, like Gecko)"
            "Chrome/45.0.2454.101 Safari/537.36"
        ),
        "referer": ref
    }
