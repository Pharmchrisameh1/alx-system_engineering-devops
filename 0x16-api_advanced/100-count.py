#!/usr/bin/python3
"""This module defines the function count_words
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


def count_words(subreddit, word_list, after="", word_count={}):
    """This function parses the title of all hot articles,
    and prints a sorted count of given keywords
    Args:
        subreddit (str): the string of the subreddit being
            queried
        word_list (list): list of all words to count occurences in
        titles of a given subreddit.
    """
    for word in word_list:
        if word.lower() not in word_count:
            word_count[word.lower()] = 0
    titles = recurse(subreddit)
    if (titles is None):
        return None
    for title in titles:
        for word in word_list:
            if word.lower() in title.lower():
                word_count[word.lower()] += title.lower().count(word.lower())
    sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    for key, value in sorted_word_count:
        if value > 0:
            print("{}: {}".format(key, value))
