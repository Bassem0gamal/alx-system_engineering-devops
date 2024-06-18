#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns a list containing the titles of all hot articles."""

import requests

def recurse(subreddit, hot_list=[]):
    """recursive function that queries the Reddit API and returns a list containing the titles of all hot articles."""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get('data')
    children = data.get('children')

    for child in children:
        hot_list.append(child.get('data').get('title'))

    after = data.get('after')
    if after is None:
        return hot_list

    return recurse(subreddit, hot_list)