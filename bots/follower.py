from bots.streamlistenerbase import StreamListenerBase


class FollowBot(StreamListenerBase):
    def __init__(self, api, logger):
        super().__init__(api, logger)

    def on_error(self, status_code):
        self.logger.info("Error detected")

    def follow_users(self):
        self.logger.info("Following users")
        for user in self.tracking_ids:
            if user not in self.api.followers_ids:
                self.logger.info("Following {}".format(self.api.get_user(user).screen_name))
                self.api.create_friendship(user)
            else:
                self.logger.info("Already following user {}".format(self.api.get_user(user).screen_name))
                pass

    def unfollow_users(self):
        self.logger.info("Following users")
        for user in self.tracking_ids:
            if user not in self.api.followers_ids:
                self.logger.info("Already following user {}".format(self.api.get_user(user).screen_name))
            else:
                self.logger.info("Unfollowing {}".format(self.api.get_user(user).screen_name))
                self.api.destroy_friendship(user["id"])
                pass

    def choose(self):
        choice = int(input("Would you like to follow or unfollow(1/2)\n"))
        users = list(input("Enter the handles \n").strip(" "))
        self.tracking_ids = [self.api.get_user(user).id for user in users]
        if choice == 1:
            self.logger.info("Users added to following list, bot now running")
            self.follow_users()
        elif choice == 2:
            self.logger.info("Users added to unfollow list, bot now running")
            self.unfollow_users()
        else:
            self.logger.info("Input error, please try again")
            self.choose()

    def start(self):
        self.choose()
