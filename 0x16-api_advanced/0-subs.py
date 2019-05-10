#!/usr/bin/python3
''' TODO '''
import requests


def number_of_subscribers(subreddit):
    ''' TODO '''
    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    custom_agent = {'User-Agent': 'fernando@api'}
    response = requests.get(URL, headers=custom_agent, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    else:
        return 0
