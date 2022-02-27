"""TSURIS: Dispatcher of Intents.
"""

from functions.os_ops import open_calculator, open_camera, open_cmd, open_notepad, open_discord
from intents import myipintent,newsintent,weatherintent,whattimeintent,wikipediaintent,emailintent,moviesintent
from functions.online_ops import get_random_advice, get_random_joke, play_on_youtube, search_on_google, send_whatsapp_message
from speaker import speak
from listener import take_user_input

def dispatch(query):
    
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
    elif 'joke' in query:
        joke = get_random_joke()
        print(joke)
        speak(joke)
    elif "advice" in query:
        advice = get_random_advice()
        print(advice)
        speak(advice)

    elif 'ip address' in query:
        myipintent.handle_intent(query)
    elif "send email" in query:
        emailintent.handle_intent(query)
    elif "trending movies" in query:
        moviesintent.handle_intent(query)
    elif 'news' in query:
        newsintent.handle_intent(query)
    elif 'what time is it' in query \
            or 'what\'s today' in query \
            or 'what is today' in query:
        whattimeintent.handle_intent(query)
    elif 'weather' in query:
        weatherintent.handle_intent(query)

def main():
    print ("No Default Functionality-Import From An Existing script.")

if __name__ == '__main__':
    main()