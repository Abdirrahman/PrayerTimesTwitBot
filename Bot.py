import tweepy
import urllib
import json
import requests
from datetime import datetime
import arrow
import sched
import time
import os
from dotenv import load_dotenv
load_dotenv()


url = "https://www.londonprayertimes.com/api/times/?format=json&key=8e9e14c7-323f-4755-88d7-8bd51ab9f094&year=2020&month=august"
r = requests.get(url)


text_json = json.loads(r.text)

today = arrow.now().format('YYYY-MM-DD')
timed = datetime.now().strftime('%I:%M')
s = sched.scheduler(time.time, time.sleep)


fajr = text_json["times"][today]["fajr"]
dhuhr = text_json["times"][today]["dhuhr"]
asr = text_json["times"][today]["asr"]
magrib = text_json["times"][today]["magrib"]
isha = text_json["times"][today]["isha"]


consumer_key = os.getenv('CONSUMER_KEY')

consumer_secret = os.getenv('CONSUMER_SECRET')


key = os.getenv('PTKEY')
secret = os.getenv('PTSECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)


def check_pt(sc):
    if timed == fajr:
        api.update_status(text_json["times"][today]["fajr"])
    elif timed == dhuhr:
        api.update_status(text_json["times"][today]["dhuhr"])
    elif timed == asr:
        api.update_status(text_json["times"][today]["asr"])
    elif timed == magrib:
        api.update_status(text_json["times"][today]["margib"])
    elif timed == isha:
        api.update_status(text_json["times"][today]["isha"])
    s.enter(60, 1, check_pt, (s,))


s.enter(60, 1, check_pt, (s,))
s.run()
