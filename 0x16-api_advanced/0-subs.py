#!/usr/bin/python3
"""get number of follwers with reddit api"""

import requests


def number_of_subscribers(subreddit):
    """get the numbers"""
    ua = 'Mozilla/5.0 (X11; Ubuntu; Linux i686) Gecko/20100101 Firefox/15'
    about = requests.get("https://www.reddit.com/r/" +
                         subreddit + "/about.json",
                         headers={'User-Agent': ua}).json()
    try:
        data = about["data"]
        return data["subscribers"]
    except KeyError:
        return 0
