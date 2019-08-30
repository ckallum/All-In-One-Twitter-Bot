# All in One Command Line Twitter Bot

This is a command line application that creates a Twitter bot
using the Tweepy API with the following functionalities:
1. Follow/Unfollow specified users.
2. Automatically like and retweet all new tweets from specified users
3. Automatically reply to messages sent to the bot with a default message.
4. Tweet from the command line using the bot account.

----------------------------
# Setup:
 - Tweepy package installed and a version of Python 3.+
 - Make sure you have a [Twitter Dev Account](develepor.twitter.com)
 - Fill in bot details in 'bots.json' manually or through running 'main.py' and
   adding the details in through the command line.
   - These are linked to and retrieved through your Twitter Dev Account
   ````
     {
        "twitter_handle": "",
        "consumer_key": "",
        "consumer_secret": "",
        "access_token": "",
        "access_token_secret": ""
      }
   
   ````
 - If using the reply-bot, you can change the default SCRIPTED_MSG in replier.py to 
   whatever message you want. This can also be done in the command line when running the program.
   
# How to Run
- ```python3 main.py```
- Follow the on-screen instructions.
   
    
   

