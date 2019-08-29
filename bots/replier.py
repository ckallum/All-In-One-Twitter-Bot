import tweepy
import json

SCRIPTED_MSG = "Thanks for messaging KE-BOT, Message courtesy of KE-BOT"


class ReplyBot(tweepy.StreamListener):
    def __init__(self, api, logger):
        super().__init__()
        self.users = {}
        self.tracking = [user["id"] for user in self.users]
        self.me = api.me()
        self.logger = logger
        self.api = api

    def on_connect(self):
        print("Bot connected, tracking {}".format([user["handle"] for user in self.tracking]))

    def on_status(self, status):
        if status.user.id_str in self.tracking:
            if not status.user.following:
                self.user.follow(status.user.id_str)
            print("Tweeted at {}".format(status.user.id_str))
            self.api.update_status("@{} {}".format(status.user.id_str, SCRIPTED_MSG))

    def add_users(self):
        pass

    def remove_users(self):
        pass

    def choose(self):
        with open("messages/option_messages/bot1.txt", "r") as option:
            choice = input(option.read())
        if choice == 1:
            self.add_users()
        elif choice == 2:
            self.remove_users()
        else:
            pass

    def start(self):
        pass
