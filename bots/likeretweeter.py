import time

import tweepy
import json


class LikeRetweetBot(tweepy.StreamListener):
    def __init__(self, api, logger):
        super().__init__()
        self.users = {}
        self.tracking = [user["id"] for user in self.users]
        self.me = api.me()
        self.api = api
        self.logger = logger

    def on_connect(self):
        self.logger.info("Bot connected, tracking {}".format([user["handle"] for user in self.tracking]))

    def on_status(self, status):
        if status.user.id_str in self.tracking:
            status.favorite()
            status.retweet()
            self.logger.info("Retweeted tweet from {}: {}".format(status.user.id_str, status.text))

    def add_users(self):
        pass

    def remove_users(self):
        pass

    def retweet_and_like_users(self):
        while True:
            stream = tweepy.Stream(self.api.auth)
            stream.filter(track="@CKrome_", follow=users, languages=["en"])
            self.logger.info("Searching tweets")
            time.sleep(60)

    def choose(self):
        with open("messages/option_messages/bot2.txt", "r") as option:
            choice = input(option.read())
        if choice == 1:
            self.add_users()
        elif choice == 2:
            self.remove_users()
        else:
            self.retweet_and_like_users()

    def start(self):
        pass
