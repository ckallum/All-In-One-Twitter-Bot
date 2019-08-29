import tweepy
import json
import logging

SCRIPTED_MSG = "Thanks for messaging KE-BOT, Message courtesy of KE-BOT"


class ReplyBot(tweepy.StreamListener):
    def __init__(self, api):
        super().__init__()
        self.tracking = [user["id"] for user in users]
        self.user = api.me()
        self.api = api

    def on_connect(self):
        print("Bot connected, tracking {}".format([user["handle"] for user in self.tracking]))

    def on_status(self, status):
        if status.user.id_str in self.tracking:
            if not status.user.following:
                self.user.follow(status.user.id_str)
            print("Tweeted at {}".format(status.user.id_str))
            self.api.update_status("@{} {}".format(status.user.id_str, SCRIPTED_MSG))

    def create(self):
        pass
