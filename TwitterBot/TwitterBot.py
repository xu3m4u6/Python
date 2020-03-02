import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# search tweets with specific keyword, like, and retweet them

search_string = 'Science'
numbersOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
	try:
		tweet.favorite()
		print('I liked the tweet')
		tweet.retweet()
		print('Retweeted the tweet')
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break

