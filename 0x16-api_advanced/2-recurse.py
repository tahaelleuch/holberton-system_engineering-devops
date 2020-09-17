#!/usr/bin/python3
"""number of hot articles"""

import requests

def recurse(subreddit, hot_list=[], after=""):
    """get number of hot with recursion"""
    ua = 'Mozilla/5.0 (X11; Ubuntu; Linux i686) Gecko/20100101 Firefox/15'
    link = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    if after:
        url = link + "?after=" + after
    else:
        url = link
    about = requests.get(url, headers={'User-Agent': ua}).json()
    data = about["data"]
    try:
        data = about["data"]
        childrens = data["children"]
        for child in childrens:
            data2 = child["data"]
            hot_list.append(data2["title"])
    except IndexError:
        pass
    after = about["data"]["after"]
    print (after)
    if after:
        recurse(subreddit, hot_list, after)
    return hot_list