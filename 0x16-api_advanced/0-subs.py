#!/usr/bin/python3
"""Function that queries the Reddit API and returns the number of subscribers."""
import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {
        "User-Agent": "0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0