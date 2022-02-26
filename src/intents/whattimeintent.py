# -*- coding: utf-8 -*-
"""TSURIS: Get Time Intent

This module returns the current date and time.

Example:
    To execute the default functionality, one can run:

        $ python -m intents.whattimeintent
"""

import logging
from datetime import datetime, time
from speaker import speak

def get_intent_results():
    """Gets the results of the default intent.

    Returns:
        str: A formatted statement specifying the current time, and then date.
    """
    logging.debug(f"Retrieving time...")
    current_time = datetime.now()
    formatted = current_time.strftime('%I:%M %p, on %A, %b %d %Y')
    logging.info(f"Time retrieved: {formatted}")
    return f'The current time is {formatted}'

def handle_intent(query):
    the_time = get_intent_results()
    print(f'TSURIS >> {the_time}')
    speak(the_time)

class WhatTimeIntentError(Exception):
    """TSURIS: WhatTimeIntentError

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
    level = logging.WARNING
    format = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level=level, format=format)
    
    print(get_intent_results())


if __name__ == '__main__':
    main()