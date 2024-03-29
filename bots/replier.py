import tweepy
from bots.streamlistenerbase import StreamListenerBase

SCRIPTED_MSG = "Thanks for messaging KE-BOT, Message courtesy of KE-BOT"


class ReplyBot(StreamListenerBase):
    def __init__(self, api, logger):
        super().__init__(api, logger)
        self.json_file = "json/autoreply/users.json"

    def on_connect(self):
        if not self.tracking_ids:
            self.logger.info("Tracking and replying to all messages sent to bot.")
        else:
            self.logger.info("Bot connected, tracking {}".format([user["handle"] for user in self.users]))

    def on_status(self, status):
        if self.tracking_ids:
            if status.user.id_str in self.tracking_ids:
                if not status.user.following:
                    self.api.create_friendship(status.user.id_str)
                self.logger.info("Tweeted at tracked user{}".format(status.user.screen_name))
                self.api.update_status("@{} {}".format(status.user.screen_name, SCRIPTED_MSG))
        else:
            if not status.user.following:
                self.api.create_friendship(status.user.id_str)
            self.logger.info("Tweeted at non-tracked user{}".format(status.user.screen_name))
            self.api.update_status("@{} {}".format(status.user.screen_name, SCRIPTED_MSG))

    def run_bot(self):
        global SCRIPTED_MSG
        msg_choice = input("Would you like to change the scripted message?(Y/N)\n")
        if msg_choice == 'Y':
            SCRIPTED_MSG = input("Type your message \n ")
        try:
            while True:
                stream = tweepy.Stream(self.api.auth, self)
                stream.filter(track="@{}".format(self.api.get_user(self.me.id).screen_name), languages=["en"], is_async=True)
                self.logger.info("Searching tweets. press CTRL-C to quit")
        except KeyboardInterrupt:
            self.logger.info("Exiting app")
            pass


