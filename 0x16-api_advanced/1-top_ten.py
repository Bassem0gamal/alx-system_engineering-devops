#!/usr/bin/python3

import requests

def top_ten(subreddit):
    """Print the titles of the first 10 hot posts listed for a given subreddit."""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    {

    response = requests.get(url, headers=headers, allow_redirects=False, params=params)

    if response.status_code == 200:
        posts = response.json()['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
