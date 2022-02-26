# -*- coding: utf-8 -*-
"""TSURIS: Weather Intent

This module performs a weather lookup to get current conditions of the current location.

Example:
    The execute the default functionality, one can run:

        $ python -m intents.weatherintent

    You will be prompted for a location.
"""

import logging
import requests
import json
import math
import datetime
from decouple import config
import myipintent
from speaker import speak

OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")


def get_intent_results(location):
    """Gets the results of the default intent.

    Args:
        location (str): The location of the weather to retrieve.

    Returns:
        tuple: Returns a tuple of: current_conditions, temperature, feels_like, low, high, humidity, sunrise, sunset
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHER_APP_ID}&units=imperial"
    response = requests.get(url).json()
    logging.debug(f"OpenWeather JSON response: {json.dumps(response)}")

    current_conditions = response["weather"][0]["description"]
    temperature = math.trunc(response["main"]["temp"])
    feels_like = math.trunc(response["main"]["feels_like"])
    low = math.trunc(response["main"]["temp_min"])
    high = math.trunc(response["main"]["temp_max"])
    humidity = str(math.trunc(response["main"]["humidity"])) + ' percent'
    sunrise = datetime.datetime.fromtimestamp(
        response["sys"]["sunrise"]).strftime('%I:%M %p')
    sunset = datetime.datetime.fromtimestamp(
        response["sys"]["sunset"]).strftime('%I:%M %p')

    logging.info(f"OpenWeather Results:")
    logging.info(f" - current_conditions: { current_conditions }")
    logging.info(f" - temperature: { temperature }")
    logging.info(f" - feels_like: { feels_like }")
    logging.info(f" - low: { low }")
    logging.info(f" - high: { high }")
    logging.info(f" - humidity: { humidity }")
    logging.info(f" - sunrise: { sunrise }")
    logging.info(f" - sunset: { sunset }")

    return current_conditions, temperature, feels_like, low, high, humidity, sunrise, sunset

def handle_intent(query):
    ip_address = myipintent.get_intent_results()
    location = myipintent.get_location_from_ip(ip_address)
    print(f'TSURIS >> Weather')
    speak(f"Getting weather report for {location}")

    current_conditions, temperature, feels_like, low, high, humidity, sunrise, sunset = get_intent_results(location)

    report = f'Current conditions in {location} are {current_conditions} with a temperature of {temperature} and humidity at {humidity}. It feels like {feels_like}. Todays low is {low} and the high is {high}. Sunrise is {sunrise} and sunset is {sunset} today.'
    print(f'TSURIS >> {report}')
    speak(report)

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
