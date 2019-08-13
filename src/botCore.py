import schedule
import time
import tweepy
import requests
import json
from conf.settings import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, API_ACCU_KEY, CITY_KEY, URL_ACCU

def tweet():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    resp = requests.get(URL_ACCU)
    previsao = resp.json()
    tweet = "Hoje o dia estará "+str(previsao["DailyForecasts"][0]["Day"]["IconPhrase"])
    api.update_status(tweet)

schedule.every().day.at("06:00").do(tweet)
tweet()
while True:
    schedule.run_pending()
    time.sleep(50)
