#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import tweepy 
from time import sleep
import pandas as pd
import numpy as np 
import csv 


# In[2]:


from credentiaals import * 

def TWITTER_SETUP():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Obtain authenticated API
    api = tweepy.API(auth,wait_on_rate_limit=True)
    return api


# In[3]:


api = TWITTER_SETUP()


# In[4]:


csvFile=open('FinalMatchaDatasett.csv','a')


# In[5]:


csvWriter=csv.writer(csvFile)


# In[7]:


for tweet in tweepy.Cursor(api.search_tweets,
                          q="matcha tea -filter:retweets",
                            count=5000,
                           lang= "en"
                        ).items(5000):
    print(tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.user.screen_name,tweet.text,tweet.id,tweet.retweet_count,tweet.favorite_count,tweet.source,tweet.user.location])


# In[ ]:




