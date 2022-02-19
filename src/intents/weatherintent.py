# -*- coding: utf-8 -*-
"""TSURIS: Weather Intent

This module performs a weather lookup to get current conditions of the current location.

Example:
    The execute the default functionality, one can run:

        $ python -m intents.weatherintent

    You will be prompted for a location.
"""

import requests
import math
import datetime
from decouple import config

OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")

def get_intent_results(location):
    """Gets the results of the default intent.

    Args:
        location (str): The location of the weather to retrieve.

    Returns:
        tuple: Returns a tuple of: current_conditions, temperature, feels_like, low, high, humidity, sunrise, sunset
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHER_APP_ID}&units=imperial"
    res = requests.get(url).json()
    #print(res)
    
    current_conditions = res["weather"][0]["description"]
    temperature = math.trunc(res["main"]["temp"])
    feels_like = math.trunc(res["main"]["feels_like"])
    low = math.trunc(res["main"]["temp_min"])
    high = math.trunc(res["main"]["temp_max"])
    humidity = str(math.trunc(res["main"]["humidity"])) + ' percent'
    sunrise = datetime.datetime.fromtimestamp(res["sys"]["sunrise"]).strftime('%I:%M %p')
    sunset = datetime.datetime.fromtimestamp(res["sys"]["sunset"]).strftime('%I:%M %p')

    return current_conditions, temperature, feels_like, low, high, humidity, sunrise, sunset

class WeatherIntentError(Exception):
    """TSURIS: WeatherIntentError

    This is an exception for errors that might occur within this intent.

    Args:
        msg (str): Human readable string describing the exception.
        code (:obj:`int`, optional): Error code.

    Attributes:
        msg (str): Human readable string describing the exception.
        code (int): Exception error code.

    """

    def __init__(self, msg, code):
        self.msg = msg
        self.code = code

def main():
    """The main entrypoint for this module, when running from the command-line."""
    location = input('Enter Weather Location> ')
    print(get_intent_results(location))


if __name__ == '__main__':
    main()