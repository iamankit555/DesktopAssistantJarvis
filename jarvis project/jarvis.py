import speech_recognition as sr
import pyttsx3
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

# Text to speak
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout = 1, phrase_time_limit = 5)
    
    try:
        print("Recognising....")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}") 
    except Exception as e:
        speak("Say that again please....")
        return "none"
    return query

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >=0 and hour <=11.59:
        speak("Good Morning sir")
    elif hour >=12 and hour <= 18:
        speak("good afternoon sir")
    else:
        speak("Good Evening sir")
    speak("i am jarvis sir . please tell me how can i help you...")


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',535)
    server.ehlo()
    server.starttls()
    server.login('krankit343@gmail.com','ankitmama1')
    server.sendmail('krankit343@gmail.com',to,content)
    server.close()



if __name__ == "__main__":
    wish()
    while True:

        query = takecommand().lower()

        # logic building for tasks

        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
        
        elif "open google chrome" in query:
            npath = "C:\\Users\\dell\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(npath)
        
        elif "open command prompt" in query:
            os.system("start cmd")
        
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "Music"
            song = os.listdir(music_dir)
            rd = random.choice(song)
            os.startfile(os.path.join(music_dir,rd))
        
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your id address is {ip}")
        
        elif "wikipedia" in query:
            speak("Searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)
        
        elif "open facebook" in query:
            webbrowser.open("https://www.facebook.com")
        
        elif "open ums" in query:
            webbrowser.open("https://ums.lpu.in/lpuums")
        
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
        
        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
        
        elif "send message" in query:
            kit.sendwhatmsg("+918294215591","This Message is sent by jarvis, my sir wants to know why u are chutiya",11,44)
        
        elif "search on youtube" in query:
            speak("what should i search on youtube")
            content = takecommand().lower()
            kit.playonyt(content)
        
        elif "send email to ankit" in query:
            try:
                speak("what should i send?")
                content = takecommand().lower()
                to = "ankitkumar0038973@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent to avi")
            except Exception as e:
                print(e)
                speak("sorry sir , i am not able to send email")
        
        elif "close notepad" in query:
            speak("ok sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "close google chrome" in query:
            speak("ok sir, closing google chrome")
            os.system("taskkill /f /im chrome.exe")
        
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn==22:
                music_dir = "Music"
                song = os.listdir(music_dir)
                rd = random.choice(song)
                os.startfile(os.path.join(music_dir,rd))
        
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")
        
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")
        
        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")




        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day")
            sys.exit()

        speak("sir , do you have any other work")
        

        


        
