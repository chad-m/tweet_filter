"""
Simple module with functions for filtering unwanted sub strings from a tweet.

Filter functions available:
- hyperlinks_filter
- usernames_filter
- hashtags_filter
- stopwords_filter
- punctuation_filter
- tweet_filter: runs specified list of other filter functions.

Example use:
tweet = tweet_filter(tweet, filters=[
    hyperlinks_filter,
    hashtags_filter,
    stopwords_filter,
    punctuation_filter])

"""

# Imports
import re

# Stop words list
stop_words = "i me my myself we our ours ourselves you your yours yourself yourselves he him his himself she her hers herself it its itself they them their theirs themselves what which who whom this that these those am is are was were be been being have has had having do does did doing a an the and but if or because as until while of at by for with about against between into through during before after above below to from up down in out on off over under again further then once here there when where why how all any both each few more most other some such no nor not only own same so than too very s t can will just don should now".split()


def hyperlinks_filter(tweet):
    # Removes hyperlinks from a given tweet
    hyperlink_pattern = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    t = re.sub(hyperlink_pattern, "", tweet)
    return t


def usernames_filter(tweet):
    # Removes usernames from a given tweet
    username_pattern = '(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z_]+[A-Za-z0-9_]+)'
    t = re.sub(username_pattern, "", tweet)
    return t


def hashtags_filter(tweet):
    # Removes hashtags from a given tweet
    hashtag_pattern = '(?<=^|(?<=[^a-zA-Z0-9-\.]))#([A-Za-z0-9_]+[A-Za-z0-9_]+)'
    t = re.sub(hashtag_pattern, "", tweet)
    return t


def stopwords_filter(tweet, sw=stop_words):
    # Removes stopwords from a given tweet
    t = "".join([w for w in tweet.split() if w not in sw])
    return t


def punctuation_filter(tweet):
    # Removes punctuation from a given tweet
    t = re.sub("[^\w']", " ", tweet)
    return t


def tweet_filter(tweet, filters=None):
    # Applies specified list of filter functions to a given tweet
    for _ in filters:
        tweet = _(tweet)
    return tweet
