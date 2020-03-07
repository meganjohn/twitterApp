from requests_oauthlib import OAuth1Session
from dotenv import load_dotenv
load_dotenv()

import os

consumer_key = os.getenv('API_key')
consumer_secret = os.getenv('API_secret_key')
access_token = os.getenv('oauth1_access_token')
access_token_secret = os.getenv('oauth1_access_token_secret')

oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

hashtag = "thisgirlcan"
response = oauth.get("https://api.twitter.com/1.1/search/tweets.json?q=%23" + hashtag)
print(response)
print("Response status: %s" % response.status_code)
print("Body: %s" % response.text)