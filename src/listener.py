import logging
import speech_recognition as sr
from datetime import datetime
from speaker import speak,play_sound_file

def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""
    query = None
    print('Monitoring.... ', end='', flush=True)
    while query is None:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            #print('Monitoring.... ', end='', flush=True)
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            #print('Thinking...', end='', flush=True)
            query = r.recognize_google(audio, language='en-us')
            play_sound_file('assets/correct.wav')
            print (f"Heard: {query}")
            if  'exit' in query or 'stop' in query:
                hour = datetime.now().hour
                if hour >= 21 and hour < 6:
                    speak("Good night!")
                else:
                    speak('Have a good day!')
                exit()
            else:
                return query.lower()
        except sr.UnknownValueError as exception:
            logging.info(f"Google could not understand or translate voice sample. {exception}")
            query = None
        except sr.RequestError as exception:
            logging.error(f"Error connecting to Google to translate voice sample. {exception}")
            query = None
        finally:
            pass

def main():
    print ("No Default Functionality-Import From An Existing script.")
    
    
if __name__ == "__main__":
    main()