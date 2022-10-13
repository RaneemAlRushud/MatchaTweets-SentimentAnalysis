#!/usr/bin/env python
# coding: utf-8

# In[37]:


#Libraries

import pandas as pd
import re 
import string

# Display the tweet fully using:
pd.set_option('display.max_colwidth', None)
pd.set_option('max_colwidth', None)


# In[5]:


df = pd.read_csv('Matcha#Dataset.csv')
df2 = pd.read_csv('Matcha#DatasetTest.csv')


# In[6]:


# to return columns' names of the dataset
df.columns


# In[7]:


# to return each column with the corresponding non-null values count and its data type
df.info()


# In[8]:


# to return the count of non-null values in each column
df.count()


# In[9]:


# to return the total number of rows
len(df)


# In[10]:


# to return statistical calculations
df.describe()


# In[11]:


df.head()


# In[12]:


df.shape


# Data Issues:

# In[13]:


# NORMALIZATION PROBLEM

# It's been noticed that some Twitter users use 'Matcha' and sometimes 'Macha' while referring to the same drink.
# Therefore, it will be normalized to 'Matcha' in all tweets.

#This method takes the tweet as the parameter, normalizes the drink's spelling, then returns it.
def normalize(tweet):
    text = re.sub("macha","matcha", tweet)
    return tweet


# In[14]:


df['Tweet'] = df['Tweet'].apply(normalize)


# In[15]:


#Return a sample of the dataset
df.sample(5)


# In[16]:


# To check if 'macha' has been replaced with 'matcha', an attempt to return any tweet that contains the word 'macha' is made
# However, the dataframe returned is empty, which means there aren't any tweets with the word 'macha', and our normalization
# is successful!

df[df['Tweet'].str.contains('macha')]


# In[17]:


# Here, all of the tweets in the sample contain 'matcha' and not 'macha'
df[df['Tweet'].str.contains('matcha')].sample(10)


# In[ ]:





# In[18]:


# Find duplicated rows that have the same value in 'Tweet' column
df[df.duplicated(subset='Tweet')].head()


# In[19]:


# duplicates count
df.duplicated(subset='Tweet').sum()


# In[20]:


# remving rows that have "RT" in the begining of the tweet
df = df[df["Tweet"].str.contains("RT") == False]


# In[21]:


# check if rows that "RT" in the begining of the tweet have been removed
df[df["Tweet"].str.contains("RT")]
# empty dataframe means no tweet exists with such keyword


# In[22]:


# check if duplicates were removed
df.duplicated(subset='Tweet').sum()


# In[23]:


# Display duplicated rows
duplicateRowsDF = df[df.duplicated(subset='Tweet')]
duplicateRowsDF.head(4)


# In[24]:


# remove duplicates
df.drop_duplicates(subset='Tweet', inplace=True)


# In[25]:


# check if duplicates were removed
df.duplicated(subset='Tweet').sum()


# In[26]:


# check total number of rows in df
df.shape


# In[27]:


#Display tweets contain hyperlinks
df2[df2['Tweet'].str.contains('http\S')].count()


# In[28]:


#Which .head(5) brings the 1st five rows tweets contain hyperlinks
#As shouwn; it brings rows contain Hyperlinks before manipulating 
df2[df2['Tweet'].str.contains('http\S')].head(5)


# In[29]:


#This function removes hyperlinks from the tweets
def remove_URL(tweet):
    """Remove URLs from a sample string"""
    return re.sub(r"http\S+", "", tweet)

#Apply remove_URL method
df['Tweet'] = df['Tweet'].apply(remove_URL)


# In[30]:


#To make sure 'Tweet' Column doesn't contain hyperlinks [I]
df[df['Tweet'].str.contains('http\S')].count()


# In[31]:


#To make sure 'Tweet' Column doesn't contain hyperlinks [II]
#Which .head(5) brings the 1st five rows tweets contain hyperlinks
#As shouwn; it doesn't bring any row
df[df['Tweet'].str.contains('http\S')].head(5)


# In[32]:


#To make sure 'Tweet' Column doesn't contain punctuations (comma as an example)
df[df['Tweet'].str.contains(',')].count()


# In[33]:


df[df['Tweet'].str.contains(',')].head(5)


# In[39]:


#This function removes punctuations from the tweets

def remove_punctuations(tweets):
    translator=str.maketrans('','',string.punctuation)
    newTweets=tweets.translate(translator)
    newTweets=''.join(c for c in newTweets.split())
    return newTweets

#Apply remove_punctuations method
df['Tweet'] = df['Tweet'].apply(remove_punctuations)


# In[40]:


#To make sure 'Tweet' Column doesn't contain punctuations (comma as an example)
df[df['Tweet'].str.contains(',')].count()


# In[41]:


df[df['Tweet'].str.contains(',')].head(5)


# In[26]:


#This function removes # ,@ and new lines from tweets

def remove_hashtags(tweet):
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    tweet = re.sub(r'\n','. ', tweet)
    
    #Replace @username with empty string
    tweet = re.sub('@[^\s]+', ' ', tweet)
    
    #Replace new lines with white space
    tweet = tweet.replace('\n',' ')
    tweet = tweet.replace('\t',' ')
    tweet = tweet.replace('_',' ')
    tweet = tweet.replace('\r',' ')
    
    return tweet

