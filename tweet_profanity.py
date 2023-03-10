'''#Assumptions:
- The dataset which is used in this program has various columns, in which there is a column named tweets which consists of tweets by users
- slurs is the list that consists of racial slurs
- df[tweet] has been cleaned i.e. stopword removal, punctuation removal
'''

import pandas as pd
import numpy as np

df=pd.read_csv('--load the dataset here--')

slurs=['--list of slurs--']

def prof_score(tweet):
    score = 0
    words = tweet.split()
    for word in words:
        if word in slurs:
            score += 1
    return score

p_s=[prof_score(i) for i in df[tweets]]
df['profanity_score']=p_s

df['word_count']=0
for i in range(len(df)):
  df['word_count'][i]=len(df['tweets'][i].split())

df['percent_prof_score']=df['profanity_score']/df['word_count']
