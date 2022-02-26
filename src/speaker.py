"""TSURIS: Speaker

This module performs sound operations such as speaking and playing wav/mp3 files.

Example:
    The execute the default functionality, one can run:

        $ python -m speaker

"""

from wave import WAVE_FORMAT_PCM
import pyttsx3
from decouple import config
from datetime import datetime
from playsound import playsound

USERNAME = config('USERNAME')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    """Used to speak whatever text is passed to it"""

    engine.say(text)
    engine.runAndWait()

def play_sound_file(file_name):
    """Plays a sound."""
    playsound(file_name)

def greet_user():
    """Greets the user according to the time"""
    
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    print(f"I am {BOTNAME}. How may I assist you?")
    print('-' * 70)
    speak(f"I am {BOTNAME}. How may I assist you?")

def main():
    print ("No Default Functionality-Import From An Existing script.")   
    
if __name__ == "__main__":
    main()