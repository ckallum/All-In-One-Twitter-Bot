import json
import logging
import tweepy

from bots.follower import FollowBot
from bots.likeretweeter import LikeRetweetBot
from bots.replier import ReplyBot
from bots.tweeter import TweetBot

with open("messages/app_messages/welcome.txt", "r") as welcome:
    WELCOME_TEXT = welcome.read() + "\n"

with open("messages/app_messages/createbot.txt", "r") as create:
    CREATE_BOT_TEXT = create.read() + "\n"

with open("messages/app_messages/mode.txt", "r") as mode:
    MODE_TEXT = mode.read() + "\n"


class BotApp(object):
    def __init__(self):
        self.bot_json = None
        self.api = None
        self.running = False
        self.bot_data_jsons = {}
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger()

    def upload_bot_data(self):
        with open("json/bots.json", "r") as auth:
            self.bot_data_jsons = json.load(auth)

    def export_bot_data(self):
        with open("json/bots.json", "w") as auth:
            json.dump(auth, self.bot_data_jsons)

    def set_specified_bot(self, specified_bot=""):
        if specified_bot:
            try:
                self.bot_json = self.bot_data_jsons[specified_bot]
            except KeyError as e:
                self.logger.log("Bot does not exist, try again!", e.args)
                retry = input("Type handle \n")
                self.set_specified_bot(retry)
        else:
            self.bot_json = self.bot_data_jsons["Default"]

    def create_bot(self, handle, ck, cs, at, ats):
        if handle in self.bot_data_jsons:
            raise Exception("Bot already exists")
        else:
            self.bot_data_jsons[handle] = {"handle": handle, "consumer_key": ck, "consumer_secret": cs,
                                           "access_token": at, "access_token_secret": ats}
            self.set_specified_bot(handle)
            self.export_bot_data()

    def create_api(self):
        auth = tweepy.OAuthHandler(self.bot_json["consumer_key"], self.bot_json["consumer_secret"])
        auth.access_token = self.bot_json["access_token"]

        auth.access_token_secret = self.bot_json["access_token_secret"]
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        try:
            api.verify_credentials()
        except Exception as e:
            self.logger.error("Error creating API")
            raise e
        self.logger.info("API created")
        self.api = api

    def get_mode_from_user(self):
        state = input(MODE_TEXT)
        if state == 1:
            bot = ReplyBot(self.api, self.logger)
        elif state == 2:
            bot = LikeRetweetBot(self.api, self.logger)
        elif state == 3:
            bot = FollowBot(self.api, self.logger)
        else:
            bot = TweetBot(self.api, self.logger)
        return bot

    def select(self, option):
        if option == 1:
            self.set_specified_bot()
        elif option == 2:
            bot_details = input("{} \n".format(CREATE_BOT_TEXT))
            bot_details = list(bot_details.strip().split(","))
            self.create_bot(bot_details[0], bot_details[1], bot_details[2], bot_details[3], bot_details[4])
        else:
            bot_handle = input("What is the bots handle?\n")
            self.set_specified_bot(bot_handle)
        self.create_api()

    def run(self):
        self.upload_bot_data()
        welcome_option = int(input("{}\n".format(WELCOME_TEXT)))
        self.select(welcome_option)
        bot = self.get_mode_from_user()
        bot.start()
