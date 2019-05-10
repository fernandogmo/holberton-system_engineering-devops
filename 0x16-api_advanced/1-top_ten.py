#!/usr/bin/python3
''' TODO '''
import requests


def top_ten(subreddit):
    ''' TODO '''
    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    custom_agent = {'User-Agent': 'fernando@api'}
    response = requests.get(URL, headers=custom_agent, allow_redirects=False)
    if response.status_code == 200:
        try:
            top = response.json().get('data').get('children')
            for t in top:
                print(t.get('data').get('title'))
        except Exception as e:
            print('None')
    else:
        print("None")
