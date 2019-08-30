import tweepy

from bots.streamlistenerbase import StreamListenerBase


class LikeRetweetBot(StreamListenerBase):
    def __init__(self, api, logger):
        super().__init__(api, logger)
        self.json_file = "json/autoretweet/users.json"

    def on_status(self, status):
        if status.user.id_str in self.tracking_ids:
            status.favorite()
            status.retweet()
            self.logger.info("Re-tweeted and liked tweet from {}: {}".format(status.user.id_str, status.text))

    def run_bot(self):
        try:
            while True:
                stream = tweepy.Stream(self.api.auth, self)
                stream.filter(track=["@"+user["handle"] for user in self.users], languages=["en"], is_async=True)
                self.logger.info("Searching tweets. press CTRL-C to quit")
        except KeyboardInterrupt:
            self.logger.info("Exiting app")
            pass


