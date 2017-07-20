"""
Simple module with functions for cleaning and preparing tweet data for further analysis. Functions expect a string.

functions in module:
- remove_hyperlinks
- remove_usernames
- remove_hashtags
- remove_stopwords
- remove_punctuation
- scrub_tweet: runs all other cleaning functions as a general tweet clean.
"""

# Imports
import re

# Stop words list
stop_words = "i me my myself we our ours ourselves you your yours yourself yourselves he him his himself she her hers herself it its itself they them their theirs themselves what which who whom this that these those am is are was were be been being have has had having do does did doing a an the and but if or because as until while of at by for with about against between into through during before after above below to from up down in out on off over under again further then once here there when where why how all any both each few more most other some such no nor not only own same so than too very s t can will just don should now".split()


def remove_hyperlinks(tweet):
    hyperlink_pattern = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    t = re.sub(hyperlink_pattern, "", tweet)
    return t


def remove_usernames(tweet):
    username_pattern = '(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z_]+[A-Za-z0-9_]+)'
    t = re.sub(username_pattern, "", tweet)
    return t


def remove_hashtags(tweet):
    hashtag_pattern = '(?<=^|(?<=[^a-zA-Z0-9-\.]))#([A-Za-z0-9_]+[A-Za-z0-9_]+)'
    t = re.sub(hashtag_pattern, "", tweet)
    return t


def remove_stopwords(tweet):
    t = "".join([ for w in tweet.split() if w not in stop_words])
    return t


def remove_punctuation(tweet):
    t = re.sub("[^\w']", " ", tweet)
    return t


def scrub_tweet(tweet):
    t1 = tweet
    t2_links = remove_hyperlinks(t1)
    t3_usernames = remove_usernames(t2_links)
    t4_hashtags = remove_hashtags(t3_usernames)
    t5_stopwords = remove_stopwords(t4_hashtags)
    t6_punctuation = remove_punctuation(t5_stopwords)
    t7_strip = t6_punctuation.strip()
    return t7_strip
