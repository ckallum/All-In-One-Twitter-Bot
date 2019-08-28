import bots
import json
import logging
import tweepy

with open("messages/welcome.txt", "r") as welcome:
    WELCOME_TEXT = welcome.read() + "\n"

with open("messages/createbot.txt", "r") as create:
    CREATE_BOT_TEXT = create.read() + "\n"


class BotApp(object):
    def __init__(self):
        self.bot = None
        self.api = None
        self.running = False
        self.bot_data = {}
        self.logger = logging.getLogger()
        self.mode = 0

    def upload_bot_data(self):
        with open("json/bots.json", "r") as auth:
            self.bot_data = json.load(auth)

    def export_bot_data(self):
        with open("json/bots.json", "w") as auth:
            json.dump(auth, self.bot_data)

    def set_specified_bot(self, specified_bot=""):
        if specified_bot:
            self.bot = self.bot_data[specified_bot]
        else:
            self.bot = self.bot_data["Default"]

    def create_bot(self, handle, ck, cs, at, ats):
        if handle in self.bot_data:
            raise Exception("Bot already exists")
        else:
            self.bot_data[handle].values = {handle, ck, cs, at, ats}
            self.set_specified_bot(handle)
            self.export_bot_data()

    def create_api(self):
        logger = logging.getLogger()
        auth = tweepy.OAuthHandler(self.bot["consumer_key"], self.bot["consumer_secret"])
        auth.access_token = self.bot["access_token"]

        auth.access_token_secret = self.bot["access_token_secret"]
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        try:
            api.verify_credentials()
        except Exception as e:
            logger.error("Error creating API")
            raise e
        logger.info("API created")
        logger.info("Current bot: {}".format(self.bot["handle"]))
        self.api = api

    def get_mode_from_user(self):
        mode = input("")

    def select(self, option):
        if option == 1:
            self.set_specified_bot()
        elif option == 2:
            bot_details = input("{}".format(CREATE_BOT_TEXT))
            bot_details = list(bot_details.strip().split(","))
            self.create_bot(bot_details[0], bot_details[1], bot_details[2], bot_details[3], bot_details[4])
        else:
            bot_handle = input("What is the bots handle?")
            self.set_specified_bot(bot_handle)
        self.create_api()

    def run(self):
        self.upload_bot_data()
        welcome_option = int(input("{}".format(WELCOME_TEXT)))
        self.select(welcome_option)
