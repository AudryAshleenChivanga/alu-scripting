         #!/usr/bin/python3
"""3-count.py"""
import requests


def count_words(subreddit, word_list, after="", words_count=None):
    """count words"""
    if words_count is None:
        words_count = {word.lower(): 0 for word in word_list}

    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    header = {'User-Agent': 'Mozilla/5.0'}
    param = {'after': after}
    response = requests.get(url, headers=header, params=param)

    if response.status_code != 200:
        return

    json_res = response.json()
    after = json_res.get('data').get('after')
    has_next = after is not None

    hot_articles = json_res.get('data').get('children')
    hot_titles = [article.get('data').get('title').lower() for article in hot_articles]

    for title in hot_titles:
        title_words = title.split()
        for word in words_count.keys():
            words_count[word] += title_words.count(word)

    if has_next:
        return count_words(subreddit, word_list, after, words_count)
    else:
        words_count = {k: v for k, v in words_count.items() if v != 0}
        for word, count in sorted(words_count.items(), key=lambda item: item[1], reverse=True):
            print("{}: {}".format(word, count))


if __name__ == "__main__":
    # Test code (if needed)
    pass
                                                                        