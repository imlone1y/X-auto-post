from requests_oauthlib import OAuth1Session
import os
import json
import random

from youtube_title import youtube_titles
from news_title import news_titles

# In your terminal please set your environment variables by running the following lines of code.
consumer_key = 'X-consumer_key'
consumer_secret = 'X-consumer_secret'

# 自行調整發文內容

# 生成隨機數字
text = '幸運數字 - ' + str(random.randint(0,100))

# 抓取 youtube 前20個發燒影片標題
# text = youtube_titles()

# 抓取聯合新聞網前三個新聞標題 
# text = news_titles()

payload = {"text": str(text)}

# Get request token
request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

try:
    fetch_response = oauth.fetch_request_token(request_token_url)
except ValueError:
    print(
        "There may have been an issue with the consumer_key or consumer_secret you entered."
    )

resource_owner_key = fetch_response.get("oauth_token")
resource_owner_secret = fetch_response.get("oauth_token_secret")
print("Got OAuth token: %s" % resource_owner_key)

# Get authorization
base_authorization_url = "https://api.twitter.com/oauth/authorize"
authorization_url = oauth.authorization_url(base_authorization_url)

# 手動輸入
print("Please go here and authorize: %s" % authorization_url)
verifier = input("Paste the PIN here: ")

# 利用selenium抓取認證碼
# from selenium_test import get_PIN
# verifier = get_PIN(authorization_url)

# Get the access token
access_token_url = "https://api.twitter.com/oauth/access_token"
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    verifier=verifier,
)
oauth_tokens = oauth.fetch_access_token(access_token_url)

access_token = oauth_tokens["oauth_token"]
access_token_secret = oauth_tokens["oauth_token_secret"]

# Make the request
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

# Making the request
response = oauth.post(
    "https://api.twitter.com/2/tweets",
    json=payload,
)

if response.status_code != 201:
    raise Exception(
        "Request returned an error: {} {}".format(response.status_code, response.text)
    )

print("Response code: {}".format(response.status_code))

# Saving the response as JSON
json_response = response.json()
print(json.dumps(json_response, indent=4, sort_keys=True))
