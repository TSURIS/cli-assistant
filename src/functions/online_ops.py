import requests
# import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config
import math
import datetime

NEWS_API_KEY = config("NEWS_API_KEY")
TMDB_API_KEY = config("TMDB_API_KEY")

def play_on_youtube(video):
    kit.playonyt(video)


def search_on_google(query):
    kit.search(query)


def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)

def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']
