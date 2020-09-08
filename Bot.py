import tweepy
import urllib
import json
import requests
from datetime import datetime
from time import sleep
import schedule
import time
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


consumer_key = os.getenv('CONSUMER_KEY')

consumer_secret = os.getenv('CONSUMER_SECRET')


key = os.getenv('PTKEY')
secret = os.getenv('PTSECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)


def pray():
    api.update_status("Its Time to Pray!")


schedule.every().day.at(text_json["times"][today]["fajr"]).do(pray)
schedule.every().day.at(text_json["times"][today]["dhuhr"]).do(pray)
schedule.every().day.at(text_json["times"][today]["asr"]).do(pray)
schedule.every().day.at(text_json["times"][today]["magrib"]).do(pray)
schedule.every().day.at(text_json["times"][today]["isha"]).do(pray)
schedule.every().day.at("19:27").do(pray)


while True:
    schedule.run_pending()
    time.sleep(1)
