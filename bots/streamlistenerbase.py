import tweepy as tweepy
import simplejson as json
import tweepy


class StreamListenerBase(tweepy.StreamListener):
    def __init__(self, api, logger):
        super().__init__()
        self.users = {}
        self.tracking = [user["id"] for user in self.users]
        self.me = api.me()
        self.api = api
        self.logger = logger
        self.json_file = ""

    def on_connect(self):
        if not self.tracking:
            raise Exception("No users being tracked")
        else:
            self.logger.info("Bot connected, tracking {}".format([user["handle"] for user in self.tracking]))

    def on_status(self, status):
        pass

    def add_users(self):
        handles = input("Enter the handles of the users")
        if not handles:
            self.logger.info("No handles entered")
            self.add_users()
        else:
            handles = handles.strip()
            for handle in handles:
                user_id = self.api.lookup_users(screen_names=handle)
                self.tracking.append(user_id)
                self.users[handle] = {"id": user_id}

    def remove_users(self):
        pass

    def choose(self):
        with open("messages/option_messages/bot2.txt", "r") as option:
            choice = input(option.read())
        if choice == 1:
            self.add_users()
        elif choice == 2:
            self.remove_users()
        else:
            self.run_bot()

    def run_bot(self):
        pass

    def start(self):
        pass
