import time

import tweepy
import json

import logging


class LikeRetweetBot(tweepy.StreamListener):
    def __init__(self, api):
        super().__init__()
        self.tracking = [user["id"] for user in users]
        self.user = api.me()

    def on_connect(self):
        print("Bot connected, tracking {}".format([user["handle"] for user in self.tracking]))

    def on_status(self, status):
        if status.user.id_str in self.tracking:
            status.favorite()
            status.retweet()
            print("Retweeted tweet from {}: {}".format(status.user.id_str, status.text))

    def retweet_and_like_users(self, bot, api, users):
        while True:
            stream = tweepy.Stream(api.auth, bot)
            stream.filter(track="@CKrome_", follow=users, languages=["en"])
            print("Searching tweets")
            time.sleep(60)
