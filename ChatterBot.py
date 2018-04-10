# Dependencies
import tweepy
import json
import time
from datetime import datetime

# Twitter API Keys
consumer_key = "b9ftuHzW8SuRZuTJwImuyfIkE"
consumer_secret = "FDSsfdQqgqiFHyWd9zT6g1rVjVSqU6CzWVMet7ZzQlkL3JfZaW"
access_token = "980981045506945024-wTSwJiTN4tN983ZpZlS93aMa7tdARjk"
access_token_secret = "rOfdz6lgOFP9wuLnb6cHlm2vyrn6Jdq8LGCdTkqM1nje4"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
while(True):
  api.update_status(f"Hello, world! {str(datetime.now())}")
  time.sleep(300)
# CODE GOES HERE
