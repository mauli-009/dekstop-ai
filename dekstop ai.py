import win32com.client
import wikipedia
import webbrowser
import os
import smtplib
import datetime
import speech_recognition as sr
import  pandas as pd

def speak(a):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.speak(a)

def wishme():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("goood night")
    speak("hello mauli,how can i help you?")

def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("recogninzing...")
        query=r.recognize_google(audio,language='en-in')

        print(f'user said: {query} ')
    except Exception as e:
        speak("i cannot got it .please say it again.")
        return "None"
    return query
if __name__== "__main__":
    wishme()
    while True:
        query = takecommand().lower()

        sites=[["youtube",'https://www.youtube.com/'],["google","https://www.google.co.in/"],["wikipedia",'https://www.wikipedia.org/']]

        for site in sites:
            if site[0].lower() in query .lower():
                print(f"opening {site[0]}")
                webbrowser.open(site[1])

            if 'open music ' in query:
                musicpath=r"C:\Users\Mauli Dudhat\Downloads\O Mahi O Mahi_192(PagalWorld.com.pe.mp3"

                os.startfile(musicpath)


#this is incomplete you can add more functionalities in this ai.





