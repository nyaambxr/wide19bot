# I NEED A LOT OF LIBS SORRY
import tweepy
import logging
import time
import sys
import requests
import os
import json

image = "output.jpg"
secrets = open("secrets.json") #hehe 
data = json.load(secrets)
auth = tweepy.OAuthHandler(data["apikey"], data["apisecret"])
auth.set_access_token(data["accesstoken"], data["accesssecret"] )
api = tweepy.API(auth)
bot_id = int(api.me().id_str)
mention_id = 1
words = ["wide19", "the", "tweet", "@wide19bot", "@gusp3h"]
message = "tweet wide19'd @{}"

while True:
    mentions = api.mentions_timeline(since_id=mention_id) # Finding mention tweets
    # Iterating through each mention tweet
    for mention in mentions:
        print("Mention tweet found!")
        print(f"{mention.author.screen_name} - {mention.text}")
        mention_id = mention.id

        # Checking if the mention tweet is not a reply, we are not the author, and
        # that the mention tweet contains one of the words in our 'words' list
        # so that we can determine if the tweet might be a question.
        if mention.in_reply_to_status_id is None and mention.author.id != bot_id:
            if True in [word in mention.text.lower() for word in words]:
                try:
                    print("Attempting to reply...")
                    api.update_status(message.format(mention.author.screen_name), in_reply_to_status_id=mention.id_str)
                    print("Successfully replied :]")
                except Exception as exc:
                    print(exc)
    time.sleep(5) # The bot will only check for mentions every 5 seconds
