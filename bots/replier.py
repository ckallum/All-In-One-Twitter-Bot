import tweepy
import json

from bots.streamlistenerbase import StreamListenerBase

SCRIPTED_MSG = "Thanks for messaging KE-BOT, Message courtesy of KE-BOT"


class ReplyBot(StreamListenerBase):
    def __init__(self, api, logger):
        super().__init__(api, logger)

    def on_connect(self):
        if not self.tracking:
            self.logger.info("Tracking and replying to all messages sent to bot.")
        else:
            self.logger.info("Bot connected, tracking {}".format([user["handle"] for user in self.tracking]))

    def on_status(self, status):
        if self.tracking:
            if status.user.id_str in self.tracking:
                if not status.user.following:
                    self.api.create_friendship(status.user.id_str)
                self.logger.info("Tweeted at tracked user{}".format(status.user.id_str))
                self.api.update_status("@{} {}".format(status.user.id_str, SCRIPTED_MSG))
        else:
            if not status.user.following:
                self.api.create_friendship(status.user.id_str)
            self.logger.info("Tweeted at non-tracked user{}".format(status.user.id_str))
            self.api.update_status("@{} {}".format(status.user.id_str, SCRIPTED_MSG))

    def run_bot(self):
        pass

    def start(self):
        pass
