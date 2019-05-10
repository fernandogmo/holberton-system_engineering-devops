#!/usr/bin/python3
''' TODO '''
import requests


def top_ten(subreddit):
    ''' TODO '''
    URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    custom_agent = {'User-Agent': 'fernando@api'}
    response = requests.get(URL, headers=custom_agent, allow_redirects=False)
    if response.status_code == 200:
        try:
            for t in response.json().get('data').get('children')[:10]:
                print(t.get('data').get('title'))
        except Exception as e:
            print("None")
    else:
        print("None")
