#!/usr/bin/python3
"""This moduled defines top_ten function.
"""
import requests


def top_ten(subreddit):
    """This function prints the titles of the
    first 10 hot posts listed for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?count=10'.format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers, allow_redirects=False)

    if (res.status_code != 200):
        print('None')
    else:
        obj = res.json()
        for idx in range(10):
            if (idx >= len(obj['data']['children'])):
                break
            print(obj['data']['children'][idx]['data']['title'])
