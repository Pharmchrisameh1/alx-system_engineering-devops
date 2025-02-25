#!/usr/bin/python3
"""This module defines the function recurse
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """This function returns a list containing
    the titles of all host articles for a given
    subreddit
    Args:
        subreddit (str): the string of the subreddit being
            queried
        hot_list (list): list of all titles of a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if (res.status_code != 200):
        return None
    obj = res.json()
    for hot_post in obj['data']['children']:
        hot_list.append(hot_post['data']['title'])
    after = obj['data']['after']
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
