# -*- coding: utf-8 -*-
"""TSURIS: Get Time Intent

This module returns the current date and time.

Example:
    To execute the default functionality, one can run:

        $ python -m intents.whattimeintent
"""

from datetime import datetime, time

def get_intent_results():
    """Gets the results of the default intent.

    Returns:
        str: A formatted statement specifying the current time, and then date.
    """
    current_time = datetime.now()
    formatted = current_time.strftime('%I:%M %p, on %A, %b %d %Y')
    return f'The current time is {formatted}'

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
    print(get_intent_results())


if __name__ == '__main__':
    main()