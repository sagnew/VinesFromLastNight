from constants import *
from TwitterSearch import *

def search_tweets(query):
    try:
        tso = TwitterSearchOrder()
        tso.setKeywords([query])
        tso.setLanguage('en')
        tso.setCount(100)
        tso.setIncludeEntities(False)

        ts = TwitterSearch(
                consumer_key = consumer_key,
                consumer_secret = consumer_secret,
                access_token = access_token,
                access_token_secret = access_token_secret
                )

        tweets = []
        for tweet in ts.searchTweetsIterable(tso):
            tweets.append(tweet['text'])
        return tweets

    except TwitterSearchException as e:
        return []

def get_vines():
    return search_tweets('vine.co')

#Write a python function that returns a dictionary of vine urls relating to the tweets containing them
def get_vineURLS(tweets):
    vines = {}
    for string in tweets:
        for word  in string.split(" "):
            if "vine.co" in word:
                vines[word] = string
                print word + vines[word]

    return vines

get_vineURLS(get_vines())














