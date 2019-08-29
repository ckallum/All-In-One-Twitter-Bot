import time
import tweepy
import json
import logging


class FollowBot(object):
    def __init__(self, api):
        pass

    def follow_users(self, users, api):
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger()
        logger.info("Following users")
        for user in users:
            if not user["following"]:
                logger.info("Following {}".format(user["handle"]))
                user["following"] = True
                api.create_friendship(user["id"])

    def create(self):
        pass
