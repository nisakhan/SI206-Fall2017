import os
import requests
import json
import unittest
import itertools
import collections
import sqlite3
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go
import plotly
from plotly.graph_objs import *

CACHE_FNAME = 'cache_weather.json'
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    cache_file.close()
    CACHE_DICTION = json.loads(cache_contents)
except:
    CACHE_DICTION = {}

def getWithCaching(baseURL, params={}):
  req = requests.Request(method = 'GET', url =baseURL, params = sorted(params.items()))
  prepped = req.prepare()
  fullURL = prepped.url
  # if we haven't seen this URL before
  if fullURL not in CACHE_DICTION:
      # make the request and store the response
      response = requests.Session().send(prepped)
      CACHE_DICTION[fullURL] = response.text

      # write the updated cache file
      cache_file = open(CACHE_FNAME, 'w')
      cache_file.write(json.dumps(CACHE_DICTION))
      cache_file.close()

  # if fullURL WAS in the cache, CACHE_DICTION[fullURL] already had a value
  # if fullRUL was NOT in the cache, we just set it in the if block above, so it's there now
  return(CACHE_DICTION[fullURL])

#Getting the lat and long of a city
def getLatandLong(city):
    google_baseURL = "https://maps.googleapis.com/maps/api/geocode/json"
    google_apikey = "AIzaSyAkQyX_KkIRoHYE-qeat55sR1iziYU_e-o"
    google_url = "https://maps.googleapis.com/maps/api/geocode/"
    google_params = {"key": google_apikey, "address": city}
    response = getWithCaching(google_baseURL, google_params)
    data = json.loads(response)
    latitude = data['results'][0]['geometry']['location']['lat']
    longitude = data['results'][0]['geometry']['location']['lng']
    return(latitude,longitude)

#today's weather for the city
def get_weather(city):
    darksky_baseURL = "https://api.darksky.net/forecast/"
    darksky_apikey = "63d0cd6647f3827016d91988ca629600"
    w,x = getLatandLong(city)
    darksky_response = getWithCaching("https://api.darksky.net/forecast/{}/{},{}".format(darksky_apikey, w, x))
    darksky_load = json.loads(darksky_response)
    return(darksky_load)

#narrows it down to just temparature by indexing "currently" and "temparature"
def getCurrentWeather(city):
    weather = get_weather(city)
    return(weather["currently"]["temperature"])

connecting = sqlite3.connect('ProjectFour.sqlite')
cur = connecting.cursor()

cur.execute("DROP TABLE IF EXISTS Cities")
cur.execute("CREATE TABLE Cities (city TEXT, temparature TEXT, latitude_longitude TEXT )")
cities = ["Detroit", "Ann Arbor", "New York", "Los Angeles", "Atlanta", "Philadelphia", "Austin", "Houston", "Hershey",
          "Lansing", "Bethesda", "Annapolis", "Berkley", "San Francisco", "Ithaca", "Chicago", "Phoenix", "Dallas", "Memphis",
          "Indianapolis", "Jacksonville", "Columbus", "Charlotte", "Seattle", "Baltimore", "Denver", "Portland", "Kansas",
          "Oklahoma", "Milwaukee", "Omaha", "Oakland", "Sacramento", "East Lansing", "Bloomfield Hills", "Southfield",
          "Tulsa", "Minneapolis", "Cleveland", "Wichita", "Cleveland", "Arlington", "Birmingham", "Boise", "Irvine",
          "Reno", "Hialeah", "Harrisburg", "Glendale", "Lubbock", "Durham", "Buffalo", "Honolulu", "Tampa", "New Orleans",
          "Pittsburgh", "Newark", "Stockton", "Cincinnati", "Toledo", "Lincoln", "Fort Wayne", "Greensboro", "San Bernardino",
          "Chula Vista", "Grand Rapids", "Flint", "Kalamazoo", "Dearborn", "Saginaw", "Hell", "El Paso", "Garland", "Chandler",
          "Orlando", "St. Petersburg", "Greensboro", "Lancaster", "York", "Scranton", "Pawnee", "Anaheim", "Aurora", "Montgomery",
          "Santa Rosa", "Ontario", "Jackson", "McKinney", "Sioux Falls", "Springfield", "Hollywood", "Savannah", "Mesquite",
          "McAllen", "Bellevue", "Orange", "West Valley City", "Warren", "Midland", "Cedar Rapids",]
for r in cities:
    weatherdata = (r, str(getCurrentWeather(r)), str(getLatandLong(r)))
    cur.execute('INSERT INTO Cities VALUES (?,?,?)',weatherdata)
    connecting.commit()

data1 = []
for h in cities:
    data1.append(getCurrentWeather(h))

plotly.tools.set_credentials_file(username='Nisakhan', api_key='sRxZpERQXNPuIZuPOgE4')

data = [go.Bar(
            x = cities,
            y = data1
    )]

fig = go.Figure(data=data)
py.iplot(data, filename='basic-bar')
