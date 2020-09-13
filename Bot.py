import tweepy
import urllib
import json
import requests
from datetime import datetime
from time import sleep
import schedule
import time
import arrow
import os
from dotenv import load_dotenv
load_dotenv()


url = "https://www.londonprayertimes.com/api/times/?format=json&key=8e9e14c7-323f-4755-88d7-8bd51ab9f094&year=2020&month=september&24hours=true"
r = requests.get(url)


text_json = json.loads(r.text)

today = arrow.now().format('YYYY-MM-DD')
timed = datetime.now().strftime('%I:%M')

print(timed)

print(datetime.now().hour)

consumer_key = os.getenv('CONSUMER_KEY')

consumer_secret = os.getenv('CONSUMER_SECRET')


key = os.getenv('PTKEY')
secret = os.getenv('PTSECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)


def pray():
    try:
        if datetime.now().hour == "4" or "5":
            api.update_status("it is fajr now!")
        elif datetime.now().hour == "12" or "13":
            api.update_status("it is dhuhr now!")
        elif datetime.now().hour == "16" or "17" or "15":
            api.update_status("it is asr now!")
        elif datetime.now().hour == "18" or "19":
            api.update_status("it is maghrib now!")
        elif datetime.now().hour == "20" or "21":
            api.update_status("it is isha now!")
        else:
            api.update_status("time should be 12:30 -- test")
    except tweepy.TweepError:
        print("2")
        sleep(2)


schedule.every().day.at(text_json["times"][today]["fajr"]).do(pray)
schedule.every().day.at(text_json["times"][today]["dhuhr"]).do(pray)
schedule.every().day.at(text_json["times"][today]["asr"]).do(pray)
schedule.every().day.at(text_json["times"][today]["magrib"]).do(pray)
schedule.every().day.at(text_json["times"][today]["isha"]).do(pray)
schedule.every().day.at("15:30").do(pray)


while True:
    schedule.run_pending()
    time.sleep(1)
