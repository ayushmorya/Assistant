import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import cv2
import random
import requests
import wikipedia
import pywhatkit as kit
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

#text to speech function
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# Function to take command from user and convert it into text
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=4, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
    except Exception as e:
        speak("Sorry, I couldn't understand you. Please try again.")
        return "None"
    return query


#to wish
def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak("Good Morning Boss!")
        elif hour >= 12 and hour < 18:
            speak("Good Afternoon Boss!")
        else:
            speak("Good Evening Boss!")
        speak("so...what are you looking for ?")

#to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()  # connect to the server
    server.starttls()
    server.login("your_email_id", "your_password")
    server.sendmail("your_email_id", to, content)





if __name__ == "__main__":
    wishMe()
    while True:
    

        query = take_command().lower()

        #logic building for tasks
        if 'open notepad' in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
            speak("Notepad is opened.")
        elif 'open word' in query:
            wpath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(wpath)
            speak("Word is opened.")
        elif 'open chrome' in query:
            cpath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(cpath)
            speak("sir...Chrome is opened.")
        elif 'open command prompt' in query:
            os.system('start cmd')
            speak("Command prompt is opened sir.")
        elif 'open calculator' in query:
            os.system('calc')
            speak("Calculator is opened.")
        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                _, img = cap.read()
                cv2.imshow('Camera', img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()
            speak("Here You Goo sir.")
        elif 'open PowerPoint' in query:
            ppath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(ppath)
            speak("sir.....PowerPoint is opened.")
        elif 'open spotify' in query:
            spotify_path = "C:\Program Files\WindowsApps\SpotifyAB.SpotifyMusic_1.249.439.0_x64__zpdnekdrzrea0"
            os.startfile(spotify_path)
            speak("Spotify is opened.")
        elif "play music" in query:
            music_dir = "D:\\Music"
            songs = os.listdir(music_dir)
            #rd = random.choice(songs)
            for song in songs:
                if song.endswith(".mp3"):
                    os.startfile(os.path.join(music_dir, song))
            # os.startfile(os.path.join(music_dir, rd))
            speak("Enjoy your music sir...")
        elif "ip address" in query:
            from requests import get
            ip = get('https://api.ipify.org').text
            speak(f"sir...Your IP address is {ip}")
        elif "wikipedia" in query:
            speak("searching in Wikipedia...")
            search_term = query.replace("wikipedia search ", "")
            result = wikipedia.summary(search_term, sentences=3)
            speak(f"Sir, According to wikipedia {search_term}")
            speak(result)
            print(result)
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/")
            speak("sir...Youtube is opened.")
        elif "open instagram" in query:
            webbrowser.open("https://www.instagram.com/")
            speak("sir...Instagram is opened.")
        elif "open facebook" in query:
            webbrowser.open("https://www.facebook.com/")
            speak("sir...Facebook is opened.")
        elif "open gmail" in query:
            webbrowser.open("https://www.gmail.com/")
            speak("sir...Gmail is opened.")
        elif "open ChatGPT" in query:
            webbrowser.open("https://chat.openai.com/")
            speak("sir...ChatGPT is opened.")
        elif "open google" in query:
            speak("sir, what would you like to search on Google?")
            search_term = take_command().lower()
            webbrowser.open(f"https://www.google.com/search?q={search_term}")
        elif "send message" in query:
            kit.sendwhatmsg("+919457394988", "this is a test message", "19:30", "Eva")
            speak("Done sir")
        elif "Youtube music" in query:
            kit.playonyt("ghost by justin bieber")
        elif "email to ayush" in query:
            try:
                speak("what should I say?")
                content = take_command().lower()
                to = "ayushmorya1507@gmail.com"
                sendEmail(to, content)
                speak("sir, Email has been sent successfully.")

            except Exception as e:
                print(e)
                speak("Sorry, I am unable to send email at this moment.")
        elif "you can sleep now" in query:
            speak("Okay sir, have a great day!")
            sys.exit()

        speak("is there anything else I can help you with?")
