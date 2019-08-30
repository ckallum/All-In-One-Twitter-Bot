import simplejson as json
import tweepy


class StreamListenerBase(tweepy.StreamListener):
    def __init__(self, api, logger):
        super().__init__()
        self.users = []
        self.tracking_ids = []
        self.me = api.me()
        self.api = api
        self.logger = logger
        self.json_file = ""
        self.action_handles = []

    def on_connect(self):
        if not self.tracking_ids:
            raise Exception("No users being tracked")
        else:
            self.logger.info("Bot connected, tracking {}".format([user["handle"] for user in self.tracking_ids]))

    def on_status(self, status):
        pass

    def add_users(self):
        for handle in self.action_handles:
            user = self.api.lookup_users(screen_names="{}".format(handle))
            self.tracking_ids.append(user.id)
            self.users.append({"id": user.id, "handle": handle})

    def remove_users(self):
        for handle in self.action_handles:
            if handle not in [user["handle"] for user in self.users]:
                self.logger.info("Invalid handle entered: {}, continuing..".format(handle))
                pass
            user = self.api.lookup_users(screen_names="{}".format(handle))
            self.tracking_ids.remove(user.id)
            self.users.remove({"id": user.id, "handle": handle})

    def update_json(self):
        with open(self.json_file, "w") as file:
            json.dump(file, self.users)

    def import_jsons(self):
        with open(self.json_file, "r") as file:
            self.users = list(json.load(file))
            self.tracking_ids = [user["id"] for user in self.users]

    def choose(self):
        with open("messages/option_messages/choice.txt", "r") as option:
            choice = int(input(option.read() + "\n"))
        handles = input("Enter the handles of the users\n")
        if not handles:
            self.logger.info("No handles entered")
        else:
            self.action_handles = (list(handles.split(" ")))
            print(self.action_handles)
        if choice == 1:
            self.add_users()
            self.logger.info("Users added, bot now running")
            self.run_bot()
        elif choice == 2:
            self.remove_users()
            self.logger.info("Users removed, bot now running")
            self.run_bot()
        elif choice == 3:
            self.logger.info("Bot running")
            self.run_bot()
        else:
            self.logger.info("Input error, please try again")
            self.choose()

    def run_bot(self):
        pass

    def start(self):
        self.import_jsons()
        self.choose()
        self.update_json()
