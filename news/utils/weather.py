import requests, json, locale
from weather_parsing import pars

APPID = "56ebc3bf9da5d77b65f93ac161d8ac14"  # <-- Put your OpenWeatherMap appid here!
URL_BASE = "https://api.openweathermap.org/data/2.5/"


def weather(lat: float = 56.0184, lon: float = 92.8672, units='metric', lang='ru', appid: str = APPID) -> dict:
    """https://openweathermap.org/api/one-call-api"""
    return requests.get(URL_BASE + "weather", params=locals()).json()


if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))
    with open('weather.txt', 'w', encoding='utf-8') as file:
        json.dump(weather(), file,  indent=3, ensure_ascii=False)
    pars()








