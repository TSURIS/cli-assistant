# -*- coding: utf-8 -*-
"""TSURIS: Get News content.

This module performs a news lookup and returns the top stories.

Example:
    To execute the default functionality, one can run:

        $ python -m intents.newsintent
        
"""
import json
import logging
import requests
from decouple import config
from speaker import speak

NEWS_API_KEY = config("NEWS_API_KEY")

def get_intent_results():
    """Gets the results of the default intent.

    Returns:
        arr: Returns the first 5 top headlines.
    """

    news_headlines = []
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}&category=general"
    response = requests.get(url).json()
    
    logging.debug(f"NewsAPI JSON response: {json.dumps(response)}")
    
    articles = response["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    
    logging.info(f"NewsAPI top 5 headlines: { articles }")    
    
    return news_headlines[:5]

def handle_intent(query):
    headlines = get_intent_results()
    print(f'TSURIS >> Latest News')
    for headline in headlines:
        print(f' - {headline}')
    speak(f"Here are the top 5 news headlines:")
    speak(headlines)

class NewsIntentError(Exception):
    """TSURIS: NewsIntentError

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
    print(f'TOP HEADLINES')
    print('-' * 80)
    for headline in get_intent_results():
        print(f' - {headline}')


if __name__ == '__main__':
    main()