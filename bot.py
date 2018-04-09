import tweepy

from secrets import *

#create an OAuthHandler instance 
#twitter requires all requests to use OAuth for Authentication

auth =tweepy.OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_token,access_secret)

#construct the API instance


api=tweepy.API(auth) #create an API object


# print(api)

public_tweets=api.home_timeline()

for tweet in public_tweets:
	print(tweet.text)