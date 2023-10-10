#!/usr/bin/python3
"""
module that gets the top 10 hot posts in a subreddit
"""
import requests


def top_ten(subreddit):
    """
    gets the top ten hot posts from the subreddit passed as an argument
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'api-request by Namasaka'}
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        res = res.json()
        posts = res['data']['children']
        # print the first 10 items
        for i in range(10):
            print(posts[i]['data']['title'])
    else:
        print('None')
