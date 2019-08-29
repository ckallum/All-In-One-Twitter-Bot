import json

import tweepy

with open("json/bots.json", "r") as bots:
    default_bot = json.load(bots)["Default"]

    auth = tweepy.OAuthHandler(default_bot["consumer_key"], default_bot["consumer_secret"])
    auth.set_access_token(default_bot["access_token"], default_bot["access_token_secret"])

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
        print("OK")
    except:
        print("Authentication Error")