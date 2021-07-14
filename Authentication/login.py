import os
from tweepy.auth import OAuthHandler
BOT_KEY = os.environ['BOT_KEY']
USER_SECRET = os.environ['USER_SECRET']
SESSION_TOKEN = os.environ['SESSION_TOKEN']
SESSION_SECRET = os.environ['SESSION_SECRET']
logList = []
def loginFunction():
    try:
        authenticate = OAuthHandler(BOT_KEY,USER_SECRET)
        authenticate.set_access_token(SESSION_TOKEN, SESSION_SECRET)
    except:
        logList.append("Check login.py in loginFunction. Error with OAuthHandler.")
        logList.append("Check login.py in loginFunction. Error with setting access token.")
    return authenticate

