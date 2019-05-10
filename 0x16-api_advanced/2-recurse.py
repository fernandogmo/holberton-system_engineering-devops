#!/usr/bin/python3
"""
This module has one function: recurse(subreddit, hot_list=[], after=None).
"""
import requests
import sys


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries a subreddit and returns a list of the
    titles of all hot articles of that subreddit.
    """
    # URL and headers to make API requests from
    url = 'https://reddit.com/r'

    # Subscriber count information
    hot = requests.get('{}/{}/hot/.json?after={}'
                       .format(url, subreddit, after),
                       headers={'User-Agent': 'Mozilla/5.0'})\
        .json().get('data')

    if not hot:
        return None

    hot_children = hot.get('children')
    hot_list += [value.get('data').get('title') for value in hot_children]

    if not hot.get('after'):
        return hot_list

    if hot.get('after'):
        return recurse(subreddit, hot_list, hot.get('after'))
