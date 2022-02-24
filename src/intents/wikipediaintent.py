# -*- coding: utf-8 -*-
"""TSURIS: Get Wikipedia content.

This module performs a lookup on wikipedia and returns summary information about a topic.

Example:
    To execute the default functionality, one can run:

        $ python -m intents.wikipediaintent
        
    You will be prompted for a keyword to search.
"""

import logging
import wikipedia
from decouple import config

OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")

def get_intent_results(keyword):
    """Gets the results of the default intent.

    Args:
        keyword (str): The keyword or phrase to lookup on wikipedia.

    Returns:
        str: Returns the first 2 sentences of the matching article.
    """
    logging.debug(f"Attempting to get Wikipedia summary from keyword: {keyword}")
    results = wikipedia.summary(keyword, sentences=2)
    logging.info(f"Wikipedia results: {results}")
    return results

class WikipediaIntentError(Exception):
    """TSURIS: WikipediaIntentError

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
    # level = logging.DEBUG
    # format = '[%(levelname)s] %(asctime)s - %(message)s'
    # logging.basicConfig(level=level, format=format)
        
    topic = input('Enter Wikipedia topic> ')
    print(get_intent_results(topic))


if __name__ == '__main__':
    main()