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


def send_message(name, contact_number):
    speak(f"now sir tell me your message for {name} ")
    # print(contact_number)
    message_get = takeCommand().lower()
    speak(f"your message is,{message_get} ")
    headers = {
        'Authorization': 'Bearer eb29fb86b6fd41039eb3fcbe3ffb5951',
    }
    json_data = {
        'from': '447520651830',
        'to': [
            contact_number,
        ],
        'body': message_get,
    }
    response = requests.post(
        'https://sms.api.sinch.com/xms/v1/619f7d1cd7744b65ad4bacee80e29d8f/batches', headers=headers, json=json_data)
    speak(f"Sir, message has been sent")


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()
        if 'send message to' in query:
            message = query
            # print(message)
            contact = message.split(" to ")
            f = open("./contact.txt", "r")
            text = f.read()
            contact_list = text.split("\n")
            # print(contact_list)
            for i in range(0, len(contact_list)):
                specific_contact = contact_list[i].split("|")
                if(contact[1] == specific_contact[0]):
                    speak(f"{contact[1]} present in yor contact")
                    print(specific_contact[1])
                    send_message(contact[1], specific_contact[1])
                    break
                elif i == len(contact_list)-1:
                    speak(
                        f"{contact[1]} is not present in your contact, please add {contact[1]} in your contact")
                    while True:
                        message = takeCommand().lower()
                        if ("ok" or contact[1]) in message:
                            while True:
                                try:
                                    speak(
                                        f"Enter the Mobile Number of {contact[1]}")
                                    number = int(
                                        input("* Enter Mobile Number: "))
                                    number = str(number)
                                    if len(number) != 10:
                                        speak("Wrong Number")
                                        continue
                                    else:
                                        break
                                except ValueError:
                                    speak("Enter only numbers")
                            number = "91"+number
                            information = ["\n", contact[1], "|", number]
                            f = open("./contact.txt", "a")
                            f.writelines(information)
                            f.close()
                            speak(f"{contact[1]} added in your contact")
                            send_message(contact[1], number)
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
