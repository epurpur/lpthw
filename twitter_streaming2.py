## import the libraries
import tweepy, codecs
from aylienapiclient import textapi

## fill in your Twitter credentials
consumer_key = "iJGWsGU50hpgpHPufeqe7IoAq"
consumer_secret = "wj0YmifZhPH5TaY5iGCTDpQGp4rivmFq5DYkPOoegkOLAXsigD"
access_token = "968923461031747584-7VxWwIwEQdU1jEcxyjB3E5vpc2oFrQL"
access_token_secret = "urEMTbfqDLOO5eYXcCvcAtspXy4TV7PT0lDZrYy8Y7rzC"

## let Tweepy set up an instance of the REST API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

## fill in your search query and store your results in a variable
results = api.search(q = "adam ondra", lang = "en", result_type = "recent", count = 10)

## use the codecs library to write the text of the Tweets to a .txt file
file = codecs.open("tweetybird4.txt", "w", "utf-8")
for result in results:
	file.write(result.text)
	file.write("\n")
file.close()
