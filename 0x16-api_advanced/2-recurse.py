#!/usr/bin/python3
"""
module that gets the top 10 hot posts in a subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    returns a list containing the titles of all articles for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'api-request by Namasaka'}
    params = {'after': after, 'limit': 100}
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code == 200:
        res = res.json()
        posts = res['data']['children']
        # print the first 10 items
        hot_list = [post['data']['title'] for post in posts]
        after = res['data']['after']
        if after is not None:
            hot_list += recurse(subreddit, after=after)
        return (hot_list)
    return (None)
