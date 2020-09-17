#!/usr/bin/python3
"""get number of follwers with reddit api"""

import requests
from fake_useragent import UserAgent

def number_of_subscribers(subreddit):
    """get the numbers"""
    ua = UserAgent()
    about = requests.get("https://www.reddit.com/r/" +
                        subreddit + "/about.json",
                         headers={'User-Agent': ua.random}).json()

    try:
        data = about["data"]
        return data["subscribers"]
    except KeyError:
        return 0
