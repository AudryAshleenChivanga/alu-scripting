#!/usr/bin/python3
"""
Module to query Reddit API for the top ten hot posts of a subreddit
"""
import requests
import sys

def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Python/3.7'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    try:
        posts = response.json().get('data').get('children')
        for post in posts:
            print(post.get('data').get('title'))
    except Exception:
        print(None)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
        