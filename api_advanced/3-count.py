#!/usr/bin/python3
""" 3-count.py """
import json
import requests

def count_words(subreddit, word_list, after="", count=None):
    """ prints a sorted count of given keywords """
    if count is None:
        count = {word.lower(): 0 for word in word_list}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        for topic in data['data']['children']:
            title_words = topic['data']['title'].lower().split()
            for word in word_list:
                count[word.lower()] += title_words.count(word.lower())

        after = data['data']['after']
        if after is not None:
            return count_words(subreddit, word_list, after, count)

    sorted_counts = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        if count > 0:
            print("{}: {}".format(word, count))
