#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Libraries

import pandas as pd
import re 

# Display the tweet fully using:
pd.set_option('display.max_colwidth', None)
pd.set_option('max_colwidth', None)


# In[4]:


df = pd.read_csv('Matcha#Dataset.csv')


# In[5]:


# to return columns' names of the dataset
df.columns


# In[6]:


# to return each column with the corresponding non-null values count and its data type
df.info()


# In[7]:


# to return the count of non-null values in each column
df.count()


# In[8]:


# to return the total number of rows
len(df)


# In[9]:


# to return statistical calculations
df.describe()


# In[10]:


df.head()


# In[11]:


df.shape


# Data Issues:

# In[12]:


# NORMALIZATION PROBLEM

# It's been noticed that some Twitter users use 'Matcha' and sometimes 'Macha' while referring to the same drink.
# Therefore, it will be normalized to 'Matcha' in all tweets.

#This method takes the tweet as the parameter, normalizes the drink's spelling, then returns it.
def normalize(tweet):
    text = re.sub("macha","matcha", tweet)
    return tweet


# In[13]:


df['Tweet'] = df['Tweet'].apply(normalize)


# In[14]:


#Return a sample of the dataset
df.sample(5)


# In[15]:


# To check if 'macha' has been replaced with 'matcha', an attempt to return any tweet that contains the word 'macha' is made
# However, the dataframe returned is empty, which means there aren't any tweets with the word 'macha', and our normalization
# is successful!

df[df['Tweet'].str.contains('macha')]


# In[16]:


# Here, all of the tweets in the sample contain 'matcha' and not 'macha'
df[df['Tweet'].str.contains('matcha')].sample(10)


# In[ ]:





# In[17]:


# Find duplicated rows that have the same value in 'Tweet' column
df[df.duplicated(subset='Tweet')].head()


# In[18]:


# duplicates count
df.duplicated(subset='Tweet').sum()


# In[19]:


# remving rows that have "RT" in the begining of the tweet
df = df[df["Tweet"].str.contains("RT") == False]


# In[20]:


# check if rows that "RT" in the begining of the tweet have been removed
df[df["Tweet"].str.contains("RT")]
# empty dataframe means no tweet exists with such keyword


# In[21]:


# check if duplicates were removed
df.duplicated(subset='Tweet').sum()


# In[22]:


# Display duplicated rows
duplicateRowsDF = df[df.duplicated(subset='Tweet')]
duplicateRowsDF.head(4)


# In[23]:


# remove duplicates
df.drop_duplicates(subset='Tweet', inplace=True)


# In[24]:


# check if duplicates were removed
df.duplicated(subset='Tweet').sum()


# In[25]:


# check total number of rows in df
df.shape


# In[ ]:




