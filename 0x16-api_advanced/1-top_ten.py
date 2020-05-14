#!/usr/bin/python3
"""Function that queries Reddit API
   prints titles: first 10 hot posts listed
"""
import requests


def top_ten(subreddit):
    """first 10 hot posts listed"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    agt = {"User-Agent": "linux:1:v1.1 (by /u/heimer_r)"}
    payload = {"limit": "10"}
    hot = requests.get(url, headers=agt, params=payload, allow_redirects=False)
    if hot.status_code != 200:
        print("None")
    else:
        hot_list = hot.json().get("data").get("children")
        hot_titles = [post.get("data").get("title") for post in hot_list]
        print(*hot_titles, sep='\n')
