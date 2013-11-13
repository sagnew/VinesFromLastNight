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
        return "No results"

def get_vines():
    return search_tweets('vine.co')
