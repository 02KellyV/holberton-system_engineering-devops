#!/usr/bin/python3
"""Recursive function that queries the Reddit API
   Parses the title of all hot articles
   Prints a sorted count of given keywords:
       case-insensitive
       delimited by spaces
       Javascript should count as javascript
       but java should not
"""
from requests import get
from sys import argv


def count_words(subreddit, word_list, after="", counter={}, t=0):
    """count and print a sorted list"""
    if t == 0:
        for word in word_list:
            counter[word] = 0
    headers = {"User-Agent": "Custom"}
    json = get("https://api.reddit.com/r/{}/hot?after={}".
               format(subreddit, after), headers=headers).json()
    try:
        key = json['data']['after']
        parent = json['data']['children']
        for obj in parent:
            for word in counter:
                counter[word] += obj['data']['title'].lower().split(
                    ' ').count(word.lower())
        if key is not None:
            count_words(subreddit, word_list, key, counter, 1)
        else:
            res = sorted(counter.items(), key=lambda i: i[1], reverse=True)
            for key, value in res:
                if value != 0:
                    print('{}: {}'.format(key, value))
    except Exception:
        return None


