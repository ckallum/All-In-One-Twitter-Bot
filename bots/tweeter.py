import tweepy

from bots.streamlistenerbase import StreamListenerBase


class TweetBot(StreamListenerBase):
    def __init__(self, api, logger):
        super().__init__(api, logger)
        self.receiver = ""
        self.message = ""