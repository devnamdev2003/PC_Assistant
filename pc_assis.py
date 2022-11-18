import os
import ctypes
import pyjokes
import pyttsx3
import datetime
import requests
import pywhatkit
import wikipedia
import webbrowser
from mss import mss
from AppOpener import run
import send_mail
import send_text_message
import send_whatsapp_message
from bs4 import BeautifulSoup
import speech_recognition as sr
from colorama import Fore

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning sir ")
        speak("Good Morning sir ")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir")
        print("Good Afternoon sir")

    else:
        print("Good Evening sir")
        speak("Good Evening sir")

    speak("I am your personal computer assistant sir. please let me know how I can help you")
    print("I am your personal computer assistant sir. please let me know how I can help you")


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

def main():
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'on wikipedia' in query:
            speak('Searching...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak("According to Wikipedia")
            speak(results)

        elif 'song' in query or 'on youtube' in query or 'videos' in query or 'video' in query or 'play' in query:
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

        elif 'temperature' in query:
            message = query
            contact = message.split(" of ")
            place = contact[1]
            search = 'temperature in '+place
            url = f"https://www.google.com/search?q={search}"
            data = BeautifulSoup(requests.get(url).text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            print(f"current {search} is {temp}")
            speak(f"current {search} is {temp}")

        elif "screenshot" in query:
            with mss() as sct:
                sct.shot()
            for filename in sct.save():
                print(filename)
            speak("done")

        elif "send mail to" in query:
            send_mail.main(query)

        elif "send text message to" in query:
            send_text_message.main(query)

        elif "send whatsapp message to" in query:
            send_whatsapp_message.main(query)

        elif 'exit' in query:
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                print("ok sir, have a nice day and, Good Morning")
                speak("ok sir, have a nice day and, Good Morning")

            elif hour >= 12 and hour < 18:
                print("ok sir, have a nice day and, Good Afternoon")
                speak("ok sir, have a nice day and, Good Afternoon")

            else:
                print("ok sir, have a nice day and, Good night")
                speak("ok sir, have a nice day and, Good night")

            break

        elif "lock my pc" in query:
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                print("ok sir, have a nice day and, Good Morning")
                speak("ok sir, have a nice day and, Good Morning")
            elif hour >= 12 and hour < 18:
                print("ok sir, have a nice day and, Good Afternoon")
                speak("ok sir, have a nice day and, Good Afternoon")
            else:
                print("ok sir, have a nice day and, Good night")
                speak("ok sir, have a nice day and, Good night")
            ctypes.windll.user32.LockWorkStation()
            # os.system("shutdown /s /t 5")
            break



pc=""" 
                                          |||||||    ||||||||
                                          ||    ||  ||       
                                          ||    ||  ||       
                                          |||||||   ||       
                                          ||        ||       
                                          ||         ||||||||"""
assistent="""
     //\\\\       ||||||||   ||||||||  ||||||||||   ||||||||  ||||||||||    //\\\\      ||\\\\     || ||||||||||
    //  \\\\     ||         ||             ||      ||             ||       //  \\\\     || \\\\    ||     ||    
   //    \\\\    ||______   ||______       ||      ||______       ||      //    \\\\    ||  \\\\   ||     ||    
  //------\\\\           ||         ||     ||              ||     ||     //------\\\\   ||   \\\\  ||     ||    
 //        \\\\          ||         ||     ||              ||     ||    //        \\\\  ||    \\\\ ||     ||    
//          \\\\ |||||||||  |||||||||  ||||||||||  |||||||||      ||   //          \\\\ ||     \\\\||     ||    
"""

print(Fore.RED,pc)
print(Fore.GREEN,assistent)

if __name__ == "__main__":
          main()
