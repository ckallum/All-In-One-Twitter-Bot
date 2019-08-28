import time

import tweepy
import json

import logging


def get_bot():
    with open("json/bot.json", "r") as auth:
        bot_data = json.load(auth)
        return bot_data


def get_users():
    with open("json/users.json", "r") as users:
        users = json.load(users)
        return users


def create_api(bot_auth):
    logger = logging.getLogger()
    auth = tweepy.OAuthHandler(bot_auth["consumer_key"], bot_auth["consumer_secret"])
    auth.access_token = bot_auth["access_token"]
    auth.access_token_secret = bot_auth["access_token_secret"]
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API")
        raise e
    logger.info("API created")
    return api


def follow_users(users, api):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()
    logger.info("Following users")
    for user in users:
        if not user["following"]:
            logger.info("Following {}".format(user["handle"]))
            user["following"] = True
            api.create_friendship(user["id"])


def start_process(users, bot_auth):
    api = create_api(bot_auth)
    while True:
        follow_users(users, api)
        time.sleep(60)


def main():
    users = get_users()
    bot_auth = get_bot()
    if not users:
        print("No users given")
    if not bot_auth:
        print("No bot given")

    start_process(users, bot_auth)


if __name__ == '__main__':
    main()
