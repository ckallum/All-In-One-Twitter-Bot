import tweepy
import json

from bots.streamlistenerbase import StreamListenerBase


class TweetBot(StreamListenerBase):
    def __init__(self, api, logger):
        super().__init__(api, logger)
