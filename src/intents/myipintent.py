# -*- coding: utf-8 -*-
"""TSURIS: My IP Intent

This module performs a lookup to get the current public IP address of this computer.

Example:
    The execute the default functionality, one can run:

        $ python -m intents.myipintent

"""

import logging
import requests
from speaker import speak

def get_intent_results():
    """Gets the results of the default intent.

    Returns:
        str: Returns the public-facing IPv4 address for this computer.
    """
    response = requests.get('https://api64.ipify.org?format=json').json()
    #print(response)
    return response["ip"]

def handle_intent(query):
    ip_address = get_intent_results()
    print(f'Your IP Address is {ip_address}.')
    speak(f'Your IP Address is {ip_address}.')

def get_location_from_ip(ip_address):
    """Gets a city location from a public IP address.

    Args:
        ip_address (str): A public-facing, non-private-range IP address.

    Returns:
        str: The closest city/metropolis related to the ip_address.
    """
    url = f"https://ipapi.co/{ip_address}/city/"
    response = requests.get(url)
    
    logging.debug(f"IPAPI response: { response.text }")
    
    location = response.text
    
    logging.info(f"IPAPI location: { location }")
    
    return location

class MyIPIntentError(Exception):
    """TSURIS: MyIPIntentError

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
    print(f'Current IP address: {get_intent_results()}')


if __name__ == '__main__':
    main()