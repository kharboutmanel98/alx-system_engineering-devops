#!/usr/bin/python3
""" A function that queries Reddit API, prints 10 hot post title"""

import requests
import sys


def top_ten(subreddit):
    """ Queries to Reddit API """
    agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': agent
    }

    params = {
        'limit': 10
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)
    if res.status_code != 200:
        print(None)
        return
    dic = res.json()
    posts = dic['data']['children']
    if len(posts) == 0:
        print(None)
    else:
        for post in posts:
            print(post['data']['title'])
