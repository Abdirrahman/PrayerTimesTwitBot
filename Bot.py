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
timed = datetime.now().strftime('%H:%M')


print(timed)

print(datetime.now().hour)

consumer_key = os.getenv('CONSUMER_KEY')

consumer_secret = os.getenv('CONSUMER_SECRET')


key = os.getenv('PTKEY')
secret = os.getenv('PTSECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)


def prayfajr():
    try:
        if datetime.now().hour == "4" or "5":
            api.update_status("it is fajr now!")
        else:
            api.update_status("15;30?")
    except tweepy.TweepError:
        print("2")
        sleep(2)


def praydhuhr():
    try:
        if datetime.now().hour == "12" or "13" or "01":
            api.update_status("dhuhr now!")
        else:
            api.update_status("else dhuhr")
    except tweepy.TweepError:
        print("2")
        sleep(2)


def prayasr():
    try:
        if datetime.now().hour == "15" or "16" or "17":
            api.update_status("asr now!")
        else:
            api.update_status("asr else")
    except tweepy.TweepError:
        print("2")
        sleep(2)


def praymagrib():
    try:
        if datetime.now().hour == "18" or "19" or "20":
            api.update_status("maghrib now!")
        else:
            api.update_status("maghrib else")
    except tweepy.TweepError:
        print("2")
        sleep(2)


def prayisha():
    try:
        if datetime.now().hour == "20" or "21" or "22":
            api.update_status("isha now!")
        else:
            api.update_status(timed)
    except tweepy.TweepError:
        print("2")
        sleep(2)


schedule.every().day.at(text_json["times"][today]["fajr"]).do(prayfajr)
schedule.every().day.at(text_json["times"][today]["dhuhr"]).do(praydhuhr)
schedule.every().day.at(text_json["times"][today]["asr"]).do(prayasr)
schedule.every().day.at(text_json["times"][today]["magrib"]).do(praymagrib)
schedule.every().day.at(text_json["times"][today]["isha"]).do(prayisha)
schedule.every().day.at("15:30").do(prayfajr)


while True:
    schedule.run_pending()
    time.sleep(1)
