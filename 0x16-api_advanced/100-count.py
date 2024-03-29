#!/usr/bin/python3
"""
Module that queries reddit api and returns values
"""
import requests


def count_words(subreddit, word_list, after=None, sort=True):
    """
    counts the given keywords from the title of hot articles
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'after': after, 'limit': 100}
    headers = {'User-Agent': 'api query by Namasaka'}
    req = requests.get(url=url,
                       params=params, headers=headers, allow_redirects=False)
    if req.status_code == 200:
        response = req.json()
        titles = [child['data']['title']
                  for child in response['data']['children']]
        after = response['data']['after']
        if after is not None:
            titles += count_words(subreddit,
                                  word_list, after=after, sort=False)
        if sort is True:
            count = {k.lower(): 0 for k in word_list}
            for title in titles:
                count = {k: v + title.lower().split().count(k)
                         for k, v in count.items()}
            count = {k: v for k, v in count.items() if v > 0}
            if len(count):
                word_list = [w.lower() for w in word_list]
                count = {k: v * word_list.count(k)
                         for k, v in count.items()}
                count = sorted(count.items(), key=lambda kv: (-kv[1], kv[0]))
                [print("{}: {}".format(k, v)) for k, v in count]
        else:
            return titles
