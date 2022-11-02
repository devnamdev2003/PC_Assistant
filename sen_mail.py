import pyttsx3
import speech_recognition as sr
import datetime
import requests

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


def send_mail(name, email_add):
    speak(f"now sir tell me your message for {name} ")
    print(email_add)
    message_get = takeCommand().lower()
    speak(f"your message is,{message_get} , now sir wait a minute")
    json_data = {
        'to': email_add,
        "from": "PersonalComputer@service.net",
        "subject": "PC Message",
        "message": message_get
    }
    response = requests.post(
        'https://www.proxynova.com/api/send-email', json=json_data)
    print(response.json())
    speak(f"Sir, mail has been sent")


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'send mail to' in query:
            message = query
            # print(message)
            contact = message.split(" to ")
            f = open("./mail_info.txt", "r")
            text = f.read()
            contact_list = text.split("\n")
            # print(contact_list)
            for i in range(0, len(contact_list)):
                specific_contact = contact_list[i].split("|")
                if(contact[1] == specific_contact[0]):
                    speak(f"{contact[1]} present in yor contact")
                    print(specific_contact[1])
                    send_mail(contact[1], specific_contact[1])
                    break
                elif i == len(contact_list)-1:
                    speak(
                        f"{contact[1]} is not present in your contact, please add {contact[1]} in your contact")
                    while True:
                        message = takeCommand().lower()
                        if ("ok" and contact[1]) in message:
                            while True:
                                speak(f"Enter {contact[1]}'s email address")
                                email = input("* Enter Email address: ")
                                if ("@." and ".com") not in email:
                                    speak("Wrong email")
                                    continue
                                else:
                                    break
                            information = ["\n", contact[1], "|", email]
                            f = open("./mail_info.txt", "a")
                            f.writelines(information)
                            f.close()
                            speak(f"{contact[1]} added in your contact")
                            send_mail(contact[1], email)
                            break
                        elif "no" in message:
                            speak(
                                f"ok sir {contact[1]} is not added in your contact")
                            break
                        else:
                            continue
        elif 'exit' in query:
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                speak("ok sir, have a nice day and, Good Morning")
            elif hour >= 12 and hour < 18:
                speak("ok sir, have a nice day and, Good Afternoon")
            else:
                speak("ok sir, have a nice day and, Good night")
            break
