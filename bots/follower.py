import tweepy
import json

from bots.streamlistenerbase import StreamListenerBase


class FollowBot(StreamListenerBase):
    def __init__(self, api, logger):
        super().__init__(api, logger)
        self.json_file = "autoflow/users.json"

    def follow_users(self):
        self.logger.info("Following users")
        for user in self.users:
            if not user["following"]:
                self.logger.info("Following {}".format(user["handle"]))
                user["following"] = True
                self.api.create_friendship(user["id"])

    def unfollow_users(self):
        pass

    def start(self):
        pass
