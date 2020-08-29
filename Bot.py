import tweepy
import urllib
import json
import requests
from datetime import datetime
import arrow
import os
from dotenv import load_dotenv
load_dotenv()

# page_url.replace(u'\ufeff', '')
# 8e9e14c7-323f-4755-88d7-8bd51ab9f094
# API_KEY = os.getenv('URL_API_KEY')
url = "https://www.londonprayertimes.com/api/times/?format=json&key=8e9e14c7-323f-4755-88d7-8bd51ab9f094&year=2020&month=august"
r = requests.get(url)
print(r)
# r = requests.get(
#     f"https://www.londonprayertimes.com/api/times/?format=json&key={API_KEY}&year=2020&month=august")
text_json = json.loads(r.text)
print(text_json)
today = arrow.now().format('YYYY-MM-DD')

time = datetime.now().strftime('%I:%M')

print(text_json["times"][today]["fajr"])
fajr = text_json["times"][today]["fajr"]
dhuhr = text_json["times"][today]["dhuhr"]
asr = text_json["times"][today]["asr"]
magrib = text_json["times"][today]["magrib"]
isha = text_json["times"][today]["isha"]


print(text_json["times"][today]["fajr"])


consumer_key = os.getenv('CONSUMER_KEY')

consumer_secret = os.getenv('CONSUMER_SECRET')


key = os.getenv('PTKEY')
secret = os.getenv('PTSECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
if time == fajr:
    api.update_status(text_json["times"][today]["fajr"])


if time == dhuhr:
    api.update_status(text_json["times"][today]["dhuhr"])


if time == asr:
    api.update_status(text_json["times"][today]["asr"])


if time == magrib:
    api.update_status(text_json["times"][today]["margib"])


if time == isha:
    api.update_status(text_json["times"][today]["isha"])
