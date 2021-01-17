# Import Libraries
import smtplib
from pygoogletranslation import Translator
from bs4 import BeautifulSoup
from googlesearch import search
# import config
import requests
import json
import imdb
# import os
# import sys
# currentdir = os.path.dirname(os.path.realpath(__file__))
# parentdir = os.path.dirname(currentdir)
# sys.path.append(parentdir)


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
        current_temperature -= 273.15
        return str(round(current_temperature)) + ", " + str(weather_description)

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

# Send email


def send_mail(subject, body, reciever):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(config.email, config.password)
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(config.email, reciever, msg)
    server.quit()

# Translate


def translate(word, language):
    translator = Translator()
    languages = translator.glanguage()
    keys = list(languages['sl'].keys())
    values = list(languages['sl'].values())
    location = -1
    for i in range(len(keys)):
        if language.lower() == keys[i].lower() or language.lower() == values[i].lower():
            location = i
    if location == -1:
        return('Language entered is not supported')
    else:
        translation = str(translator.translate(word, dest=keys[location]))
        translation = translation[translation.find(
            "text") + 5:translation.find(', p')]
        return(f'{word} in {values[location]} => {translation}')

# Find Movie
def find_movie(movie):
    x = requests.get(f'https://assistant-beta-app.herokuapp.com/movie/{movie}')
    result = x.json()
    return result