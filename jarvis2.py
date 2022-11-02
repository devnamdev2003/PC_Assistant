import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyjokes
import pywhatkit
from AppOpener import run
import ctypes
import os

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
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.7
        speak("Say somthing...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'search' in query:
            speak('Searching...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak("According to Wikipedia")
            speak(results)
        elif 'song' in query or 'on youtube' in query or 'videos' in query or 'play' in query:
            print(query)
            query = query.replace("play", "")
            query = query.replace("youtube", "")
            pywhatkit.playonyt(query)
        elif 'on google' in query:
            print(type(query))
            query = query.replace("search", "")
            comm = 'https://www.google.com/search?q='+query
            webbrowser.open(comm)

        elif 'joke' in query:
            My_joke = pyjokes.get_joke(language="en", category="all")
            print(My_joke)
            speak(f" {My_joke}")

        elif 'open' in query:
            query = query.replace("open", "")
            inp = query.strip()
            if input:
                run(inp)
                speak(f" opening {inp}")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'exit' in query:
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                speak("ok sir, have a nice day and, Good Morning")

            elif hour >= 12 and hour < 18:
                speak("ok sir, have a nice day and, Good Afternoon")

            else:
                speak("ok sir, have a nice day and, Good night")

            break
        elif "lock my pc" in query:
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                speak("ok sir, have a nice day and, Good Morning")
            elif hour >= 12 and hour < 18:
                speak("ok sir, have a nice day and, Good Afternoon")
            else:
                speak("ok sir, have a nice day and, Good night")
            ctypes.windll.user32.LockWorkStation()
            # os.system("shutdown /s /t 5")
            break
