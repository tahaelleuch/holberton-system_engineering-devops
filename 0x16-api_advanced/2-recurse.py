#!/usr/bin/python3
"""number of hot articles"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """get number of hot with recursion"""
    ua = 'Mozilla/5.0 (X11; Ubuntu; Linux i686) Gecko/20100101 Firefox/15'
    link = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    url = link + "?after=" + after
    req = requests.get(url, headers={'User-Agent': ua},
                       allow_redirects=False)
    if (req.status_code != 200):
        return None
    about = req.json()
    if about["data"]["children"] == 0:
        return None
    for child in about["data"]["children"]:
        data2 = child["data"]
        hot_list.append(data2["title"])
    after = about["data"]["after"]
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
