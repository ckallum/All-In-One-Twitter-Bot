from bots.streamlistenerbase import StreamListenerBase


class TweetBot(StreamListenerBase):
    def __init__(self, api, logger):
        super().__init__(api, logger)
        self.receiver = ""
        self.message = ""

    def on_error(self, status_code):
        self.logger.info("Error detected")

    def create_tweet(self):
        self.api.update_status("@" + self.receiver + " " + self.message)
        self.logger.info("Message sent")

    def start(self):
        self.receiver = input("Which handle would you like to tweet @? \n ")
        self.message = input("Enter the message \n ")
        while len(self.message) > 280:
            self.logger.info("Message too long")
            self.message = input("Enter the message \n ")
        self.create_tweet()
