# -*- coding: utf-8 -*-

import json

import requests
from bs4 import BeautifulSoup

url = "http://api.weatherstack.com/current"
key = "99341742f0082f84f0501274714b5582"


def parse(par):
    try:
        return parse_wc(par)
    except:
        querystring = {"access_key": "99341742f0082f84f0501274714b5582", "query": str(par)}
        response = requests.request("GET", url, params=querystring)

        json_ser = json.loads(response.text)

        location = "{0}, {1}".format(json_ser['location']['name'], json_ser['location']['country'])
        weather = (json_ser['current']['temperature'], json_ser['current']['weather_descriptions'][0].lower())

        weather_int = int(weather[0])
        rel = "Ну, прям лееето! Каеф!!!)"
        if weather_int < 0:
            rel = "Прохлаадно)) Оденьтесь потеплее!"
        elif weather_int < 18:
            rel = "Ну, так себе погодка) Оденьтесь по-весенне-осеннему!"

        return "В {0} сейчас {1} градусов по цельсию, {2}. {3} ".format(location, weather[0], weather[1], rel)


def parse_wc(params):
    response = str(requests.get("https://weather.com/ru-RU/weather/today/l/{0}".format(params)).content.decode())
    html = response[2:len(response) - 1]

    soup = BeautifulSoup(html, features='html.parser')

    weather_div_class = "today_nowcard-temp"
    weather_div = soup.find('div', class_=weather_div_class)
    weather_div_str = str(weather_div)
    weather_cut_left = weather_div_str[47:]
    weather_cut = weather_cut_left[:weather_cut_left.index('<')]

    location_h1_class = "h4 today_nowcard-location"
    location_h1 = soup.find('h1', class_=location_h1_class)
    location_h1_str = str(location_h1)
    location_cut_left = location_h1_str[location_h1_str.index('>') + 1:]
    location_cut = location_cut_left[:location_cut_left.index('<')]

    phrase_div_class = "today_nowcard-phrase"
    phrase_div = soup.find('div', class_=phrase_div_class)
    phrase_div_str = str(phrase_div)
    phrase_cut_left = phrase_div_str[phrase_div_str.index('>') + 1:]
    phrase_cut = phrase_cut_left[:phrase_cut_left.index('<')]

    weather_int = int(weather_cut)
    rel = "Ну, прям лееето! Каеф!!!)"
    if weather_int < 0:
        rel = "Прохлаадно)) Оденьтесь потеплее!"
    elif weather_int < 16:
        rel = "Ну, так себе погодка) Оденьтесь по-весенне-осеннему!"

    return "В {0} сейчас {1} градусов по цельсию, {2}. {3} ".format(location_cut, weather_cut, phrase_cut.lower(), rel)


if __name__ == "__main__":
    print(parse("-15.81,-47.86"))
