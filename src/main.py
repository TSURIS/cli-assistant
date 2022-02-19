import requests
import sys
from functions.online_ops import *
import pyttsx3
import speech_recognition as sr
from decouple import config
from datetime import datetime
from functions.os_ops import open_calculator, open_camera, open_cmd, open_notepad, open_discord
from random import choice
from utils import opening_text
from pprint import pprint

from intents import myipintent, newsintent, weatherintent,whattimeintent,wikipediaintent

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 220)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# Text to Speech Conversion
def speak(text):
    """Used to speak whatever text is passed to it"""

    engine.say(text)
    engine.runAndWait()


# Greet the user
def greet_user():
    """Greets the user according to the time"""
    
    greeting = ""
    message = ""
    hour = datetime.now().hour
    if (hour >= 0) and (hour < 12):
        greeting = f"Good Morning {USERNAME}!"
    elif (hour >= 12) and (hour < 16):
        greeting = f"Good afternoon {USERNAME}!"
    elif (hour >= 16):
        greeting = f"Good Evening {USERNAME}!"
    message = f"{greeting} I am {BOTNAME}. How may I assist you?"
    
    print(message)
    speak(message)


# Takes Input from User
def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('** Listening....', end=' ', flush=True)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...', end=' ', flush=True)
        query = r.recognize_google(audio, language='en-us')
        print(f'Heard: "{query}".')        
        
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night!")
            else:
                speak('Have a good day!')
            exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    
    print(f'Heard: "{query}".')
    return query

def main():
    greet_user()
    print('-' * 70)
    try:
        while True:
            query = take_user_input().lower()

            if 'open notepad' in query:
                open_notepad()

            elif 'open discord' in query:
                open_discord()

            elif 'open command prompt' in query or 'open cmd' in query:
                open_cmd()

            elif 'open camera' in query:
                open_camera()

            elif 'open calculator' in query:
                open_calculator()

            elif 'ip address' in query:
                ip_address = myipintent.get_intent_results()
                speak(f'Your IP Address is {ip_address}.')
                print(f'Your IP Address is {ip_address}')

            elif 'wikipedia' in query:
                speak('What do you want to search on Wikipedia?')
                search_query = take_user_input().lower()
                results = wikipediaintent.get_intent_results(search_query)
                print(f'TSURIS>> {results}')
                speak(f"According to Wikipedia, {results}")

            elif 'youtube' in query:
                speak('What do you want to play on Youtube, sir?')
                video = take_user_input().lower()
                play_on_youtube(video)

            elif 'search on google' in query:
                speak('What do you want to search on Google, sir?')
                query = take_user_input().lower()
                search_on_google(query)

            elif "send whatsapp message" in query:
                speak('On what number should I send the message sir? Please enter in the console: ')
                number = input("Enter the number: ")
                speak("What is the message sir?")
                message = take_user_input().lower()
                send_whatsapp_message(number, message)
                speak("I've sent the message sir.")

            elif "send email" in query:
                print("TSURIS>> What is the e-mail adddress: ")
                speak("What is the e-mail adddress: ")
                receiver_address = take_user_input() \
                                    .replace('at sign','@') \
                                    .replace('ampersand','@') \
                                    .replace('at','@') \
                                    .replace('dot','.') \
                                    .replace(' ','')
                if receiver_address.lower() == 'me' or receiver_address.lower() == 'myself':
                    receiver_address = config('USER_EMAIL')
                if receiver_address.lower() == 'cancel':
                    print(f'Cancelling...')
                    speak('Cancelling.')
                    break
                print(f'  >> Email: {receiver_address}')
                
                print("TSURIS>> What should be the subject?")
                speak("What should be the subject?")
                subject = take_user_input().capitalize()
                
                if subject.lower() == 'cancel':
                    print(f'Cancelling...')
                    speak('Cancelling.')
                    break
                print(f'  >> Subject: {subject}')
                
                print("TSURIS>> What is the message?")
                speak("What is the message?")
                message = take_user_input().capitalize()
                if message.lower() == 'cancel':
                    print(f'Cancelling...')
                    speak('Cancelling.')
                    break
                
                if send_email(receiver_address, subject, message):
                    speak("I've sent the email.")
                else:
                    speak("Daggum! Something went wrong while I was sending the mail. Please check the console for more information.")

            elif 'joke' in query:
                joke = get_random_joke()
                speak(joke)
                pprint(joke)

            elif "advice" in query:
                advice = get_random_advice()
                speak(advice)
                pprint(advice)

            elif "trending movies" in query:
                movies = get_trending_movies()
                print(f'TSURIS >> Trending movies...')
                for movie in movies:
                    print(f' - {movie}')
                speak(f"Some of the trending movies are: {movies}")

            elif 'news' in query:
                headlines = newsintent.get_intent_results()
                print(f'TSURIS >> Latest News')
                for headline in headlines:
                    print(f' - {headline}')
                speak(f"Here are the top 5 news headlines:")
                speak(headlines)
                
            elif 'what time is it' in query:
                the_time = whattimeintent.get_intent_results()
                print(f'TSURIS >> {the_time}')
                speak(the_time)

            elif 'weather' in query:
                ip_address = myipintent.get_intent_results()
                location = myipintent.get_location_from_ip(ip_address)
                print(f'TSURIS >> Weather')
                speak(f"Getting weather report for {location}")

                current_conditions, temperature, feels_like, low, high, humidity, sunrise, sunset = weatherintent.get_intent_results(location)
                
                report = f'Current conditions in {location} are {current_conditions} with a temperature of {temperature} and humidity at {humidity}. It feels like {feels_like}. Todays low is {low} and the high is {high}. Sunrise is {sunrise} and sunset is {sunset} today.'
                print(f'TSURIS >> {report}')
                speak(report)
                
    except (KeyboardInterrupt):
        print('\nGoodbye.')
        sys.exit()
    except Exception as e:
        print("woopsy daisy")
        exc_type, exc_value, exc_tranceback = sys.exe_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback,
                                  limit=2,
                                  file=sys.stdout)
        sys.exit()

if __name__ == '__main__':
    main()