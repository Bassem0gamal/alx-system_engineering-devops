#!/usr/bin/python3
""""Function that queries the Reddit API and prints the titles of the first 10 hot posts"""
import requests

def top_ten(subreddit):
    """Print the titles of the first 10 hot posts listed for a given subreddit."""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }

    response = requests.get(url, headers=headers, allow_redirects=False, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        print("None")
        return
    posts = response.json().get("data")
    [print(c.get("data").get("title")) for c in posts.get("children")]
