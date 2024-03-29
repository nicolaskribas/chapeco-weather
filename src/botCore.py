import schedule
import time
import tweepy
import requests
import json
from conf.settings import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, API_ACCU_KEY, CITY_KEY

language = "pt-br"
details = "true"
metric = "true"
url = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/"+CITY_KEY+"?apikey="+API_ACCU_KEY+"%20&language="+language+"&details="+details+"&metric="+metric
def getForecast():
    r = requests.get(url).json()

    phraseDay = r["DailyForecasts"][0]["Day"]["LongPhrase"].lower()
    phraseNight = r["DailyForecasts"][0]["Night"]["LongPhrase"].lower()
    rainProbabilityDay = round(r["DailyForecasts"][0]["Day"]["RainProbability"])
    rainProbabilityNight = round(r["DailyForecasts"][0]["Night"]["RainProbability"])
    rainVolumeDay = round(r["DailyForecasts"][0]["Day"]["Rain"]["Value"])
    rainVolumeNight = round(r["DailyForecasts"][0]["Night"]["Rain"]["Value"])
    min = round(r["DailyForecasts"][0]["Temperature"]["Minimum"]["Value"])
    max = round(r["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"])
    minFeel = round(r["DailyForecasts"][0]["RealFeelTemperature"]["Minimum"]["Value"])
    maxFeel = round(r["DailyForecasts"][0]["RealFeelTemperature"]["Maximum"]["Value"])
    difMin = min - minFeel
    difMax = maxFeel - max

    if difMin >= difMax and difMin >= 2:
        temperature = "Temperaturas entre "+str(min)+"°C e "+str(max)+"°C, sensação termica de até "+str(minFeel)+"°C.\n"
    elif difMax >= difMin and difMax >= 2:
        temperature = "Temperaturas entre "+str(min)+"°C e "+str(max)+"°C, sensação termica de até "+str(maxFeel)+"°C.\n"
    else:
        temperature = "Temperaturas entre "+str(min)+"°C e "+str(max)+"°C.\n"

    if rainProbabilityDay != 0 and rainVolumeDay != 0:
        rainDay = " com "+str(rainProbabilityDay)+"% de chance de chuva e um volume de "+str(rainVolumeDay)+"mm.\n"
    else:
        rainDay = ".\n"

    if rainProbabilityNight != 0 and rainVolumeNight != 0:
        rainNight = " com "+str(rainProbabilityNight)+"% de chance de chuva e um volume de "+str(rainVolumeNight)+"mm."
    else:
        rainNight = "."

    forecastDay = "Durante o dia: "+phraseDay+rainDay
    forecastNight = "À noite: "+phraseNight+rainNight

    return temperature+forecastDay+forecastNight

def tweet(api):
    forecast = getForecast()
    api.update_status(forecast)

def main():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    schedule.every().day.at("06:00").do(tweet, api)
    while True:
        schedule.run_pending()
        time.sleep(1)

main()
