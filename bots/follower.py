import time
import tweepy
import json
import logging


class FollowBot(object):
    def __init__(self, api, logger):
        self.users = {}
        self.me = api.me()
        self.api = api
        self.logger = logger

    def follow_users(self):
        self.logger.info("Following users")
        for user in self.users:
            if not user["following"]:
                self.logger.info("Following {}".format(user["handle"]))
                user["following"] = True
                self.api.create_friendship(user["id"])

    def unfollow_users(self):
        pass

    def choose(self):
        pass

    def start(self):
        pass
