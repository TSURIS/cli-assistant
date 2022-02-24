import requests
# import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config
import math
import datetime

NEWS_API_KEY = config("NEWS_API_KEY")
# OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")
TMDB_API_KEY = config("TMDB_API_KEY")
EMAIL_ACCOUNT = config("EMAIL_ACCOUNT")
EMAIL_PASSWORD = config("EMAIL_PASSWORD")


# def find_my_ip():
#     ip_address = requests.get('https://api64.ipify.org?format=json').json()
#     return ip_address["ip"]


# def search_on_wikipedia(query):
#     results = wikipedia.summary(query, sentences=2)
#     return results


def play_on_youtube(video):
    kit.playonyt(video)


def search_on_google(query):
    kit.search(query)


def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)


def send_email(receiver_address, subject, message):
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


# def get_latest_news():
#     news_headlines = []
#     res = requests.get(
#         f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}&category=general").json()
#     #print(res)
#     articles = res["articles"]
#     for article in articles:
#         news_headlines.append(article["title"])
#     return news_headlines[:5]


# def get_weather_report(city):
#     res = requests.get(
#         f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=imperial").json()
#     #print(res)
    
#     current_conditions = res["weather"][0]["description"]
#     temperature = math.trunc(res["main"]["temp"])
#     feels_like = math.trunc(res["main"]["feels_like"])
#     low = math.trunc(res["main"]["temp_min"])
#     high = math.trunc(res["main"]["temp_max"])
#     humidity = str(math.trunc(res["main"]["humidity"])) + ' percent'
#     sunrise = datetime.datetime.fromtimestamp(res["sys"]["sunrise"]).strftime('%I:%M %p')
#     sunset = datetime.datetime.fromtimestamp(res["sys"]["sunset"]).strftime('%I:%M %p')

#     return current_conditions, temperature, feels_like, low, high, humidity, sunrise, sunset


def get_trending_movies():
    trending_movies = []
    
    url = f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}"
    response = requests.get(url).json()
        
    print(response)
    
    results = response["results"]
    for r in results:
        trending_movies.append(f'{r["original_title"]}') # - {r["overview"]}')
    return trending_movies[:5]


def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']
