import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
# Import Libraries
from bs4 import BeautifulSoup
from googlesearch import search
import config
import requests
import json

# Configure Browser Header and URL
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
URL = ''

# Return weather data
api_key = config.open_weather_api_key
base_url = "http: // api.openweathermap.org/data/2.5/weather?"


def check_weather(city_name):
    full_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(full_url)
    X = response.json()

    if X["cod"] != "404":
        y = X["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = X["weather"]
        weather_description = z[0]["description"]

        # convert temperature to celsius from kelvin
        print("Temperature in celsius:" + str(current_temprature-273.15))

        print("Humidity as a percentage:" + str(current__humidity))
        print(str(weather_description))

    else:
        print("City not found")


# Internet Search


def google_query(query):
    link = []
    for j in search(query, tld="ca", num=10, stop=10, pause=2):
        link.append(j)
    return link

# Check Price of Stock
    

def return_stock_price():
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


def check_price():
    query = "MSFT" + " Yahoo Finance"
    URL = google_query(query)[0]
    if check_price() == False:
        return "Error"
    else:
        currency, title, price = check_price()
        return title, currency, price


print(check_price())
