#!/usr/bin/python3
"""
Returntop10postsofasubreddit.
"""

importjson
importrequests


deftop_ten(subreddit):
url='https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
headers={'User-Agent':'Mozilla/5.0'}
response=requests.get(url,headers=headers)

ifresponse.status_code==200:
data=json.loads(response.text)
forpostindata['data']['children']:
title=post['data']['title']
print(title)
else:
print(None)