#!/usr/bin/python3
"""3-count.py"""
importjson
importrequests


defcount_words(subreddit,word_list,after="",count=[]):
"""printsasortedcountofgivenkeywords"""

ifafter=="":
count=[0]*len(word_list)

url="https://www.reddit.com/r/{}/hot.json".format(subreddit)
request=requests.get(url,
params={'after':after},
allow_redirects=False,
headers={'User-Agent':'Mozilla/5.0'})

ifrequest.status_code==200:
data=request.json()

fortopicin(data['data']['children']):
forwordintopic['data']['title'].split():
foriinrange(len(word_list)):
ifword_list[i].lower()==word.lower():
count[i]+=1

after=data['data']['after']
ifafterisNone:
save=[]
foriinrange(len(word_list)):
forjinrange(i+1,len(word_list)):
ifword_list[i].lower()==word_list[j].lower():
save.append(j)
count[i]+=count[j]

foriinrange(len(word_list)):
forjinrange(i,len(word_list)):
if(count[j]>count[i]or
(word_list[i]>word_list[j]and
count[j]==count[i])):
aux=count[i]
count[i]=count[j]
count[j]=aux
aux=word_list[i]
word_list[i]=word_list[j]
word_list[j]=aux

foriinrange(len(word_list)):
if(count[i]>0)andinotinsave:
print("{}:{}".format(word_list[i].lower(),count[i]))
else:
count_words(subreddit,word_list,after,count)
