"""TSURIS: Movies Intent

This module gets information about movies.

Example:
    The execute the default functionality, one can run:

        $ python -m intents.moviesintent

"""

import logging
import requests
from decouple import config
from speaker import speak
from listener import take_user_input

TMDB_API_KEY = config("TMDB_API_KEY")

def get_intent_results():
    """Gets the results of the default intent.

    Returns:
        str: Returns the top trending movies.
    """
    trending_movies = []
    
    url = f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}"
    response = requests.get(url).json()
        
    print(response)
    
    results = response["results"]
    for r in results:
        trending_movies.append(f'{r["original_title"]}') # - {r["overview"]}')
    return trending_movies[:5]

def handle_intent(query):
    movies = get_intent_results()
    print(f'TSURIS >> Trending movies...')
    for movie in movies:
        print(f' - {movie}')
    speak(f"Some of the trending movies are: {movies}")