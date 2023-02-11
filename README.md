# tweet_profanity
A Python Program to analyze the profanity of tweets.

# Problem Statement
Imagine there is a file full of Twitter tweets by various users and you are provided a set of words that indicates racial slurs. Write a program that can indicate the degree of profanity for each sentence in the file.

#Assumptions
- The assumed dataset which is used in this program has various columns, in which there is a column named tweets which consists of tweets by users
- slurs is a list that consists of racial slurs
- df[tweet] has been cleaned i.e. stopword removal, punctuation removal, link and numbers removal has been performed

# Approach
- After importing the neccessary packages and loading the data, a user defined function prof_score is created to calculate the profanity scores for the tweets. It adds "+1" to the score if the word in the tweet is also present in the slurs list( a list that contains of racial slurs).
- A new column profanity_scores is created and the scores are calculated for each tweet in the dataset using the prof_score user defined function.
- word_count column is created to list the number of words in the tweets after cleaning.
- Finally percentage of profanity score is calculated with the help of formula "word_count/profanity_score" and it is listed in the column "percent_prof_score".
