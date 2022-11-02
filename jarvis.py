import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib
import pyjokes
import pywhatkit
from AppOpener import run

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
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'song' in query:
            print(query)
            query = query.replace("song", "")
            query = query.replace("play", "")
            pywhatkit.playonyt(query)
        elif 'youtube' in query:
            print(query)
            query = query.replace("youtube", "")
            pywhatkit.playonyt(query)

        elif 'search' in query:
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
