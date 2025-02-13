import PyPDF2
import geocoder
import instaloader
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
import time
import pyjokes
import pyautogui
import pdfreader
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

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
        speak("Sorry, I didn't get it Boss")
        return "None"
    query = query.lower()
    return query

#to wish
def wishMe():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%H:%M")
    
    if hour >= 0 and hour < 12:
        speak(f"Good Morning Boss! It's {tt}.")
    elif hour >= 12 and hour < 18:
        speak(f"Good Afternoon Boss! It's {tt}.")
    else:
        speak(f"Good Evening Boss! It's {tt}.")
    speak("So...what are you looking for?")

#to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()  # connect to the server
    server.starttls()
    server.login('ayushmorya93@gmail.com', 'ayushsakshi@@20')
    server.sendmail('ayushmorya1507@gmail.com', to, content)
    server.close()

#news
def news():
    main_url = "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=aed16a79b07249b3ae60f2456a88b243"
    main_page = requests.get(main_url).json()
    #print(main_page.json())
    articles = main_page['articles']
    #print(articles)
    head = []
    day = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth"]
    for ar in articles:
        head.append(ar['title'])
    for i in range(len(day)):
        speak(f"{day[i]} headline: {head[i]}")

#pdf read
def pdf_reader():
    book = open('atomic.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total pages in the PDF: {pages}")
    speak("sir please enter the page number you want me to read")
    pg = int(input("Enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)
    
def call_mummy():
    mummy_number = ""  # Replace with your mother's actual phone number
    try:
        # Initiates a WhatsApp call; this may open the WhatsApp Web app with the number
        kit.sendwhatmsg_instantly(mummy_number, "Hi Mummy! Just wanted to say I love you!", 15, True, 5)
        print("Message sent and call initiated to Mummy!")
    except Exception as e:
        print("An error occurred:", e)
        
        
        
if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:

        query = take_command().lower()

        #logic building for tasks
        if 'open notepad' in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
            speak("Notepad is opened.")
        elif 'close notepad' in query:
            os.system('taskkill /F /IM notepad.exe')
            speak("Notepad is closed.")
        elif 'open word' in query:
            wpath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(wpath)
            speak("Word is opened sir.")
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
        elif 'hello' in query:
            speak("Hello, Sudhanshu!")
        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                _, img = cap.read()
                cv2.imshow('Camera', img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cap.release()
        
        elif "greets everyone" in query:
            speak("Hello everyone, I'm glad to see you all, Mr.Sudhanshu, How can i assist you today?")    
        elif 'open PowerPoint' in query:
            ppath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(ppath)
            speak("sir.....PowerPoint is opened.")
        elif 'open spotify' in query:
            spotify_path = "C:\Program Files\WindowsApps\SpotifyAB.SpotifyMusic_1.249.439.0_x64__zpdnekdrzrea0"
            os.startfile(spotify_path)
            speak("Spotify is opened.")
        elif "open vs code" in query:
            vs_code_path = "C:\\Users\\ayush\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            
            os.startfile(vs_code_path)
            speak("sir...VS Code is opened.")
        
        elif "call mummy" in query:
            call_mummy()
            speak("Sure, I've called Mummy!")
        elif "play music" in query:
            music_dir = "" #path dedena  
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
        elif "open Gmail" in query:
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
            kit.sendwhatmsg("+918445484836", "this is a test message", 12, 3)
            speak("sir, message has been sents")
        elif "play song in youtube" in query:
            kit.playonyt("ghost by justin bieber")
        # elif "email to friend" in query:
        #     try:
        #         speak("what should i say sir ?")
        
        #         content = take_command().lower()
        #         to = "ayushmorya1507@gmail.com"
        #         sendEmail(to, content)
        #         speak("sir, email has been sent successfully.")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry, I am unable to send email at this moment.")

        #to set alarm
        elif "set alarm" in query:
            nm = int(datetime.datetime.now().hour)
            if nm==17:
                music_dir = "D:\\Music"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
                speak("Sir, alarm set for 10 PM. Music is playing.")
        

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
        elif "shut down the system" in query:
            os.system("shutdown /s /t 1")
        elif "open whatsapp" in query:
            webbrowser.open("https://web.whatsapp.com/")
            speak("sir...Whatsapp is opened.")
        elif "restart the system" in query:
            os.system("shutdown /r /t 1")
        elif "what time is it" in query:
            now = datetime.datetime.now()
            time = now.strftime("%H:%M:%S")
            speak(f"Sir, the current time is {time}")
        elif "what date is it" in query:
            now = datetime.datetime.now()
            date = now.strftime("%d-%m-%Y")
            speak(f"Sir, the current date is {date}")
        elif "what is my name" in query or " Jarvis who am I ?" in query or "who am I" in query or "what's my name " in query:
            speak("Sir," " trying to play ?, are we? You’re the unforgettable Sudhanshu! Master of my circuits")
        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        elif "tell me the news" in query:
            speak("Sure sir, let me fetch some news headlines for you:")
            news()


        #################################################################################
        #################################################################################
        elif "send email" in query:
            speak("sir, what should I say?")
            query = take_command().lower()
            if "Send a file" in query:
                email = ""
                password = " "
                send_to_email = "ayushmorya1507@gmail.com"
                speak("Okay sir, and what is the subject for this email ?")
                query = take_command().lower()
                subject = query
                speak("and sir, what is the message ?")
                query2 = take_command().lower()
                message = query2
                speak("Sure, please enter the path of the file you want to send")
                file_location = input("Enter the path of the file: ")
                speak("please hold on sir")

                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = send_to_email
                msg['Subject'] = subject

                msg.attach(MIMEText(message, 'plain'))

                #setup the attachment
                filename = os.path.basename(file_location)
                attachment = open(file_location, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename=%s" % filename)

                #Attch the attachment to the MIMEMultipart object
                msg.attach(part)

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, send_to_email, text)
                server.quit()
                speak("Email has been sent successfully to Ayush!")

            else:
                email = ""
                password = ""
                send_to_email = ""
                message = query

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                server.sendmail(email, send_to_email, message)
                server.quit()
                speak("Email has been sent successfully to !")
        #################################################################################
        #################################################################################



        #----------------------To find the location using IP Address---------------------

        elif "where am I" in query or "what is my location" in query or "where I am" in query:
            speak("wait sir...")
            try:
                #getting GPS location
                g = geocoder.ip('me')
                latitude = g.latlng[0]
                longitude = g.latlng[1]
                
                #use reverse geocoding to get address
                reverse_geocode_url = f"https://api.bigdatacloud.net/data/reverse-geocode-client?latitude={latitude}&longitude={longitude}&localityLanguage=en"
                location_info = requests.get(reverse_geocode_url).json()
                
                city = location_info.get('city', 'Unknown city')
                country = location_info.get('countryName', 'Unknown country')
                
                speak(f"Sir, We are currently in {city}, {country}.")
            except Exception as e:
                speak("Sorry, I am unable to find your location at the moment.")
                
        #---------------------------------------------------------------------------------
        
        
        #--------------------------To check a instagram profile---------------------------
        elif "check instagram profile" in query or "profile on instagram" in query or "Instagram profile" in query:
            speak("sir, enter the username of the profile you want to check:")
            name = input("Enter the username: ")
            speak("here is the profile")
            webbrowser.open(f"www.instagram.com/{name}")
            time.sleep(5)
            speak("sir, would you like to download the profile picture?")
            condition = take_command().lower()
            if "yes please" in condition:
                mod = instaloader.Instaloader() #pip install instadownloader
                mod.download_profile(name, profile_pic_only=True)
                speak("Sir, the profile picture has been downloaded successfully.")
            else:
                pass

        #-----------------------------Take Screenshot------------------------------------
        elif "take a screenshot" in query or "screenshot" in query:
            speak("sir, please tell me the name for this screenshot file")
            name = take_command().lower()
            speak("taking the screenshot...please hold the screen")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("Sir, the screenshot has been saved successfully.")
            
            
        #-----------------------------Reading a PDF-------------------------------------
        elif"read a pdf" in query or "pdf" in query:
            pdf_reader()




        elif "you can sleep now" in query:
            speak("Okay sir, have a great day!")
            sys.exit()

        speak("is there anything else I can help you with?")
