#!/usr/bin/python3
"""A recursive funct that queries Reddit API, returns list of hot articles"""

import requests
import sys


def add_title(lists, posts):
    """ Appends item to a list """
    if len(posts) == 0:
        return
    lists.append(posts[0]['data']['title'])
    posts.pop(0)
    add_title(lists, posts)


def recurse(subreddit, lists=[], after=None):
    """ Queries to Reddit API """
    agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': agent
    }

    params = {
        'after': after
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)

    if res.status_code != 200:
        return None

    dic = res.json()
    posts = dic['data']['children']
    add_title(lists, posts)
    after = dic['data']['after']
    if not after:
        return lists
    return recurse(subreddit, lists=lists, after=after)
