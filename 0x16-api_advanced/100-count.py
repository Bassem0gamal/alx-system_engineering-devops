#!/usr/bin/python3
"""Function that count words in all hot posts of a given Reddit subreddit."""

import requests


def count_words(subreddit, word_list, after="", counts=None):
    if counts is None:
        counts = {word.lower(): 0 for word in word_list}

    headers = {"User-Agent": "my-app"}
    params = {"after": after}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()["data"]
    for article in data["children"]:
        title_words = article["data"]["title"].lower().split()
        for word in title_words:
            if word in counts:
                counts[word] += 1

    if data["after"] is not None:
        count_words(subreddit, word_list, data["after"], counts)
    elif after == "":
        for word, count in sorted(counts.items(),
                                  key=lambda item: (-item[1], item[0])):
            if count > 0:
                print(f"{word}: {count}")
