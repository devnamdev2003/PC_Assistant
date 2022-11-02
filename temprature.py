import requests
from bs4 import BeautifulSoup
from mss import mss
import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!,Dev ")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Dev")

    else:
        speak("Good Evening,Dev!")

    speak("I am your personal computer assistant sir. please let me know how I can help you")


def takeCommand():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 0.7
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            break
        except Exception as e:
            print(e)
            print("Say that again please...")
            speak("Say that again please...")
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'temperature' in query:
            message = query
            contact = message.split(" of ")
            place = contact[1]
            search = 'temperature in '+place
            url = f"https://www.google.com/search?q={search}"
            data = BeautifulSoup(requests.get(url).text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")
        elif "screenshot" in query:
            with mss() as sct:
                sct.shot()
            for filename in sct.save():
                print(filename)
            speak("done")
        elif 'exit' in query:
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                speak("ok sir, have a nice day and, Good Morning")
            elif hour >= 12 and hour < 18:
                speak("ok sir, have a nice day and, Good Afternoon")
            else:
                speak("ok sir, have a nice day and, Good night")
            break
