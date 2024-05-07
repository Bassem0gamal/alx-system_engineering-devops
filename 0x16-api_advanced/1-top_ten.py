#!/usr/bin/python3
"""Function that queries the Reddit API and print hot posts."""
import requests

def top_ten(subreddit):
    """Print the titles of the 10 hottest posts."""
    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    headers = {'user-agent': 'my-app/0.0.1'}
    response = get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 404:
        print("None")
        return None
    results = response.json().get("data")
    children = results.get("children")
    for child in children[:10]:
        post = child.get("data")
        print(post.get("title"))
