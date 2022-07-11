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

# Genrous Bot 
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    print(follower.name)
    if follower.name == 'berkalgl':
        follower.follow()
        break