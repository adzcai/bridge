# Import Libraries
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from bs4 import BeautifulSoup
from googlesearch import search
import math
import config
import requests
import json

# Configure Browser Header and URL
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
URL = ''

# Fetch Weather Data


def check_weather(city_name):
    api_key = config.open_weather_api_key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    full_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(full_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        z = x["weather"]
        weather_description = z[0]["description"]
        current_temperature -= -273.15
        return math.floor(current_temperature), weather_description

    else:
        return "City not found"


# Internet Search
def google_query(query):
    link = []
    for j in search(query, tld="ca", num=10, stop=10, pause=2):
        link.append(j)
    return link

# Check Price of Stock


def return_stock_price(URL):
    try:
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        price = soup.find(
            class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').get_text()
        title = soup.find(class_='D(ib) Fz(18px)').get_text()
        currency = soup.find(class_='C($tertiaryColor) Fz(12px)').get_text()
        currency = currency[-3:]
    except AttributeError as e:
        return "Error"
    return currency, title, price


def check_price(query):
    query += query + " Yahoo Finance"
    URL = google_query(query)[0]
    if return_stock_price(URL) == "Error":
        return "Error"
    else:
        currency, title, price = return_stock_price(URL)
        return title, price, currency


print(check_weather("Toronto"))
