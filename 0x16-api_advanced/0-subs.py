#!/usr/bin/python3
"""Module to query the Reddit API and returns the number of subscribers"""
import requests

def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        number_of_subscriber = data['data']['subscribers']
        return number_of_subscriber
    else:
        return 0

