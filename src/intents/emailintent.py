"""TSURIS: Email Intent

This module performs email operations.

Example:
    The execute the default functionality, one can run:

        $ python -m intents.emailintent

"""

import logging
from decouple import config
from email.message import EmailMessage
import smtplib
from speaker import speak
from listener import take_user_input

EMAIL_ACCOUNT = config("EMAIL_ACCOUNT")
EMAIL_PASSWORD = config("EMAIL_PASSWORD")

def get_intent_results(receiver_address, subject, message):
    """Gets the results of the default intent.

    Returns:
        str: Returns the public-facing IPv4 address for this computer.
    """
    
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email["Subject"] = subject
        email['From'] = EMAIL_ACCOUNT
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False

def handle_intent(query):
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
        return
    print(f'  >> Email: {receiver_address}')
    
    print("TSURIS>> What should be the subject?")
    speak("What should be the subject?")
    subject = take_user_input().capitalize()
    
    if subject.lower() == 'cancel':
        print(f'Cancelling...')
        speak('Cancelling.')
        return
    print(f'  >> Subject: {subject}')
    
    print("TSURIS>> What is the message?")
    speak("What is the message?")
    message = take_user_input().capitalize()
    if message.lower() == 'cancel':
        print(f'Cancelling...')
        speak('Cancelling.')
        return
    
    confirm = ''
    while 'yes' not in confirm or 'confirmed' not in confirm:
        print("TSURIS>> Are you sure you want to send this? ")
        speak("Are you sure you want to send this?")
        confirm = take_user_input().lower()
        
        if 'cancel' in confirm or \
            'exit' in confirm or \
            'no' in confirm:
            print(f'Cancelling...')
            speak('Cancelling.')
            return
    
    
    if get_intent_results(receiver_address, subject, message):
        speak("I've sent the email.")
    else:
        speak("Daggum! Something went wrong while I was sending the mail. Please check the console for more information.")

class EmailIntentError(Exception):
    """TSURIS: EmailIntentError

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
    print(f'NOTE: There is no default functionality for this intent. Please use from an import.')


if __name__ == '__main__':
    main()