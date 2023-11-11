#!/usr/bin/python3
"""Modulefortop_tenfunction"""
importrequests


deftop_ten(subreddit):
"""FunctionthatqueriestheRedditAPI."""
url="https://www.reddit.com/r/{}/hot.json?limit=10"\
.format(subreddit)
headers={'User-Agent':'MyUserAgent1.0'}
response=requests.get(url,headers=headers)

ifresponse.status_code==200:
data=response.json().get('data').get('children')
forpostindata:
print(post.get('data').get('title'))
else:
print(None)