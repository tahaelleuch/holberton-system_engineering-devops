#!/usr/bin/python3
"""get top 10 of a subreddit"""

import requests


def top_ten(subreddit):
    """top 10"""
    ua = 'Mozilla/5.0 (X11; Ubuntu; Linux i686) Gecko/20100101 Firefox/15'
    about = requests.get("https://www.reddit.com/r/" +
                         subreddit + "/hot.json?limit=10",
                         headers={'User-Agent': ua}).json()
    try:
        data = about["data"]
        childrens = data["children"]
        for child in childrens:
            data2 = child["data"]
            print(data2["title"])
    except KeyError:
        return None
