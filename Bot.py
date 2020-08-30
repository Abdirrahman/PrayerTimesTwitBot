import tweepy
import urllib
import json
import requests
from datetime import datetime
import arrow
import threading
import os
from dotenv import load_dotenv
load_dotenv()


url = "https://www.londonprayertimes.com/api/times/?format=json&key=8e9e14c7-323f-4755-88d7-8bd51ab9f094&year=2020&month=august"
r = requests.get(url)


text_json = json.loads(r.text)

today = arrow.now().format('YYYY-MM-DD')
timed = datetime.now().strftime('%I:%M')


fajr = text_json["times"][today]["fajr"]
dhuhr = text_json["times"][today]["dhuhr"]
asr = text_json["times"][today]["asr"]
magrib = "08:35"
isha = text_json["times"][today]["isha"]

print(isha)
print(timed)
consumer_key = os.getenv('CONSUMER_KEY')

consumer_secret = os.getenv('CONSUMER_SECRET')


key = os.getenv('PTKEY')
secret = os.getenv('PTSECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

print(text_json["times"][today]["isha"])
print(timed)


def check_fajr():
    threading.Timer(60.0, check_fajr).start()
    if timed == fajr:
        api.update_status(text_json["times"][today]["fajr"])
    else:
        print("f")


def check_dhuhr():
    threading.Timer(60.0, check_dhuhr).start()
    if timed == dhuhr:
        api.update_status(text_json["times"][today]["dhuhr"])
    else:
        print("d")


def check_asr():
    threading.Timer(60.0, check_asr).start()
    if timed == asr:
        api.update_status(text_json["times"][today]["asr"])
    else:
        print("a")


def check_magrib():
    threading.Timer(60.0, check_magrib).start()
    if timed == magrib:
        api.update_status(text_json["times"][today]["margib"])
    else:
        print("m")


def check_isha():
    threading.Timer(60.0, check_isha).start()
    if timed == isha:
        api.update_status(text_json["times"][today]["isha"])
        print(text_json["times"][today]["isha"])
    else:
        print("yo")


threading.Thread(target=check_fajr).start()

threading.Thread(target=check_dhuhr).start()

threading.Thread(target=check_asr).start()

threading.Thread(target=check_magrib).start()

threading.Thread(target=check_isha).start()
