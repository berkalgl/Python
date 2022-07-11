import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.me()

# accessing the api with limit
# othwerwise twitter api blocks it.
def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)

# Narcist Bot 
search_query = 'python'
number_of_tweets = 2

for tweet in tweepy.Cursor(api.search, search_query).items(number_of_tweets):
    try:
        #like
        tweet.favorite()
        #retweet
        #tweet.retweet()
        print('I liked it')
    except tweepy.TweepError as err:
        print(err.reason)
    except StopIteration:
        break
