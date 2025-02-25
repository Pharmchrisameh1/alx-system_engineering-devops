#!/usr/bin/python3
"""This moduled defines function returns the number
of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """ This function returns the number of subscribers
    for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if (res.status_code != 200):
        return (0)
    obj = res.json()
    return (obj['data']['subscribers'])
