from distutils.filelist import translate_pattern
from fnmatch import translate
import pyttsx3
import speech_recognition as sr
import webbrowser
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
import pywhatkit
import wikipedia
from googletrans import Translator
import os
import pyautogui
import psutil
from tkinter import Label
from tkinter import Entry
from tkinter import Button
import requests
from tkinter import Tk
from gtts import gTTS
from tkinter import StringVar
import PyPDF2
from pytube import YouTube
import datetime
from playsound import playsound
import keyboard
import pyjokes
from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write 
import webbrowser
from time import sleep
import random
import requests
from PIL import Image
from notifypy import notify
from WEEKEND import time
import geocoder
from geopy.geocoders import Nominatim
import bs4
from urllib.request import urlopen
import string
import json
import google.generativeai as genai
#from BRAIN import Brain
#import Chatbot

import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',170)

def speak(audio):
    print("   ")
    print(f": {audio}")
    engine.say(audio)
    print("    ")
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Wellcome HOME sir..!")  

    
    speak("Yo, what's up? I'm Jarvis, your virtual homie. I'm here to help you out with whatever you need, from setting alarms to telling you jokes. Just hit me up and I'll do my best to assist you.")

    
    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
    speak(f"the time is {strTime}")
    strDate = datetime.datetime.now().date()   
    speak(f"Today is {strDate}")

def takeCommand():
    #It takes microphone input from the user and returns string output

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
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


def TakeHindi():
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening......")
            command.pause_threshold = 1
            audio = command.listen(source)

            try:
                print("Recognizing.....")
                query = command.recognize_google(audio,language='hi')
                print(f"You Said : {query}")

            except:
                return "none"

            return query.lower()
        

def WhatsappMsg(name,massage):
    webbrowser.open("https://web.whatsapp.com/")
    sleep(15)
    click(x=313 , y=259)
    sleep(1)
    write(name)
    sleep(3)
    click(x=310 , y=408)
    sleep(1)
    click(x=973 , y=956)
    sleep(0.5)
    write(massage)
    press('enter')


def WhatsappChat(name):
    webbrowser.open("https://web.whatsapp.com/")
    sleep(20)
    click(x=313 , y=259)
    sleep(1)
    write(name)
    sleep(1)
    click(x=310 , y=408)

def instagramMsg():

    sleep(5)

    click(x=89, y=558)

def instagramNotf():

    sleep(2)

    click(x=44, y=640)

def NasaNews(Date):
    Api_Key = "ZitBhsYyay7n3jlQIqx47xGgZHNnmehOz2Tb5t58"
    speak("Extracting Data from Nasa...")
    url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_Key)
    Params ={'date':str(Date)} 
    r = requests.get(url,params=Params)
    data = r.json()
    Info = data['explanation']
    Title = data['title']
    Image_url = data['url']
    Image_r = requests.get(Image_url)
    filename = str(Date) + '.jpg'
    with open(filename,'wb') as f:
        f.write(Image_r.content)
    path_1 = "C:\\Users\\91707\\OneDrive\\Desktop\\J A R V I S\\" + str(filename)
    path_2 = "C:\\Users\\91707\\OneDrive\\Desktop\\J A R V I S\\NASA IMAGES\\" + str(filename)
    os.rename(path_1,path_2)
    img = Image.open(path_2)
    img.show
    speak(f"Title : {Title}")
    speak(f"According to Nasa : {Info}")



if __name__ == "__main__":

    wishMe()
    while True:

       query = takeCommand().lower()
       

        # Logic for executing tasks based on 
           
       if 'wikipedia' in query:
            speak("Searching Wikipedia.....")
            query = query.replace("jarvis","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            speak(f"According To Wikipedia : {wiki}")   

       elif 'jarvis are you there' in query:
            speak("AT YOUR SERVICE BRO...")

       elif 'how are you' in query:
            speak("I am always on.... no matter what!")
            speak("what about you sir?")

       elif 'fine' in query:
            speak("great to hear it sir")

       elif 'nothing special' in query:
            speak("just give me a hug..... and everything will be ok")    

       elif 'thank you' in query:
            speak("it's ok sir..") 

       elif 'you are so good' in query:
            speak("thank you sir .... it's my pleasure!")

       elif 'so get back to work' in query:
            speak("yes sir. so tell me how may i help you?")

       elif 'what are you doing' in query:
            speak("working with you sir...")

       elif 'you need a break' in query:
            speak("ok sir... you can call me anytime! ")
            speak("just say wake up jarvis")
            speak("And i will be back on ")
            break

       elif 'go to sleep' in query:
            speak("ok  sir ...good night.... sweet dreams...")
            break

       elif 'fuck you' in query:
            speak("fuck you too son of a bitch...")
            break

       elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
            speak("opening youtube for you...")

       elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")
            speak("opening instagram for you...")

       elif 'check new messages' in query:
            instagramMsg()
            speak("checking new messeges for you sir...")

       elif 'check notification also' in query:
            instagramNotf()
            speak("here is your notification sir...")

       elif 'open google' in  query:
            webbrowser.open("https://www.google.com/")
            speak("opening google for you...")

       elif 'open a new tab' in query:
            webbrowser.open("chrome://newtab/")
            speak("opening a new tab for you...")

       elif 'open whatsapp' in  query:
            webbrowser.open("https://web.whatsapp.com/")
            speak("opening whatsapp for you...")
        
       elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/")
            speak("opening facebook for you...")     

       elif 'show the weather report' in query:
            webbrowser.open("https://www.accuweather.com/en/in/bali-chak/191587/weather-forecast/191587")
            speak("here is your weather report sir...")   

       elif 'open my channel' in query:
            webbrowser.open("https://www.youtube.com/@user-iz8wm2oz2t/featured") 
            speak("opening EXORZ for you...") 

       elif 'check gmails' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            speak("checking mail...")

       elif 'check college mail' in query:
            webbrowser.open("https://mail.google.com/mail/u/3/#inbox")
            speak("checking your college mail...")       


       elif 'what is on my movie lists' in query:
            speak("here are some movies")
            movies_dir = 'D:\\HOLLYWOOD HOMIES'
            movies = os.listdir(movies_dir)
            print(movies)    
            os.startfile(os.path.join(movies_dir, movies[0]))

       elif 'play hangover' in query:
            speak("playing hangover...")
            hangover_dir = 'D:\\HOLLYWOOD HOMIES\\THE HANGOVER TRILOGY'
            hangover = os.listdir(hangover_dir)
            print(hangover)    
            os.startfile(os.path.join(hangover_dir, hangover[0])) 

       elif 'play john wick' in query:
            speak("playing Mr.john wick...")
            johnwick_dir = 'D:\\HOLLYWOOD HOMIES\\JOHN WICK SUPREMACY'
            johnwick = os.listdir(johnwick_dir)
            print(johnwick)    
            os.startfile(os.path.join(johnwick_dir, johnwick[0]))

       elif 'open college portal' in query:
            webbrowser.open("https://www.cemkolaghat.org/")    

       elif 'show me naruto wallpapers' in query:
            webbrowser.open("https://in.pinterest.com/search/pins/?rs=ac&len=2&q=naruto%20wallpaper&eq=naruto&etslf=6912") 

       elif 'show me pinterest' in query:
            webbrowser.open("https://in.pinterest.com/")   

       elif 'play some music' in query:
            speak("playing Music ...")
            Music_dir = 'D:\\MUSIC'
            songs = os.listdir(Music_dir)
            print(random.choice(songs))    
            os.startfile(os.path.join(Music_dir, random.choice(songs)))
 

       elif 'play carryminati' in query:
            webbrowser.open("https://www.youtube.com/watch?v=GOFQN8otiYs&list=PLObNowOPccbukgcAXAjzBnuLobtcjXit0")   
 


       elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

       elif 'the date' in query:
            strDate = datetime.datetime.now().date()   
            speak(f"Sir, the date is {strDate}")

       elif 'open map' in query:
            webbrowser.open("https://www.google.com/maps/@22.3613033,87.5562234,16z")
            speak("Opening Map for you ....")

       elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        #else: 
            #reply = Chatbot.ChatterBot(query)
            #speak(reply)
                
       elif 'temperature update' in query:
          search = "temperature in balichak"
          url = f"https://www.google.com/search?q=temperature+in+balichak{search}"
          r = requests.get(url)
          data = BeautifulSoup(r.text,"html.parser")
          temperature = data.find("div",class_ = "BNeawe").text
          speak(f"The Temperature Outside Is {temperature}")

          speak("Do I Have To Tell You Another Place Temperature ?")
          next = takeCommand()

          if 'yes' in next:
            speak("Tell Me The Name Of tHE Place ")
            name = takeCommand()
            search = f"temperature in {name}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_ = "BNeawe").text
            speak(f"The Temperature in {name} is {temperature}")

          else:
            speak("no problem sir")

#youtube comm::


       elif'pause' in query:
            keyboard.press('space bar')
            speak("Done Sir")

       elif 'restart' in query:
            keyboard.press('0')
            speak("Done Sir")

       elif 'mute' in query:
            keyboard.press('m')
            speak("Done Sir")

       elif 'skip' in query:
            keyboard.press('l')
            speak("Done Sir")

       elif 'back' in query:
            keyboard.press('j')
            speak("Done Sir")

       elif 'full screen' in query:
            keyboard.press('f')
            speak("Done Sir")
             
       elif 'film mode' in query:
            keyboard.press('t')
            speak("Done Sir")

    #whatsapp auto...
       elif 'open chat' in query:
            speak("with whome?")
            name = input(": Enter The name :")
            WhatsappChat(name)

       elif 'whatsapp message' in query:
            name =query.replace("whatsapp message", "")
            name = name.replace("send", "")
            name = name.replace("to", "")
            Name = str(name)
            speak(f"whats the message for{Name}")
            MSG = takeCommand()
            WhatsappMsg(name , MSG)


            #taskkill/exit

       if 'close youtube' in query:
            speak("Ok Sir , Wait A second!")
            os.system("TASKKILL /F /im Chrome.exe")
            speak("Your Command Has Been Succesfully Completed!")
            

       elif 'close chrome' in query:
            speak("Ok Sir , Wait A second!")
            os.system("TASKKILL /f /im Chrome.exe")
            speak("Your Command Has Been Succesfully Completed!")
            

       elif 'close telegram' in query:
            speak("Ok Sir , Wait A second!")
            os.system("TASKKILL /F /im Telegram.exe")
            speak("Your Command Has Been Succesfully Completed!")

       elif 'close instagram' in query:
            speak("Ok Sir , Wait A second!")
            os.system("TASKKILL /F /im chrome.exe")
            speak("Your Command Has Been Succesfully Completed!")

       elif'close whatsapp' in query:
            speak("Ok Sir , Wait A Second")
            os.system("TASKKILL /F /im Chrome.exe")
            speak("Your Command Has Been Succesfully Completed!")
            
       elif 'youtube search' in query:
            speak("OK sIR , This Is What I found For Your Search!")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            speak("Done Sir!")

       elif 'repeat my word' in query:
            speak("Speak Sir!")
            jj = takeCommand()
            speak(f"You Said : {jj}")

       #elif 'translator' in
            #speak("Tell Me The Line!")
            #line = TakeHindi()
            #traslate = Translator()
            #result = traslate.translate(line)
            #Text = result.text
            #speak(Text)

       elif 'tell me a joke' in query:
            get = pyjokes.get_joke()
            print(get)
            speak(get)

       elif 'remember that' in query:
            remeberMsg =query.replace("remember that","")
            remeberMsg = remeberMsg.replace("jarvis","")
            speak("You Tell Me To Remind You That :"+remeberMsg)
            remeber = open('data.txt','w')
            remeber.write(remeberMsg)
            remeber.close()

       elif 'what do you remember' in query:
            remeber = open('data.txt','r')
            speak("You Tell Me That" + remeber.read())

       elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            query = query.replace("google","")
            speak("This Is What I Found On The Web!")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query,2)
                speak(result)

            except:
                speak("No Speakable Data Available!")

       elif 'alarm' in query:
            speak("Enter The Time !")
            time = input(": Enter The Time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    speak("Time To Wake Up Sir!")
                    DRXX_dir = 'D:\\MUSIC'
                    DRXX = os.listdir(DRXX_dir)
                    print(DRXX)    
                    os.startfile(os.path.join(DRXX_dir, DRXX[0]))

                elif now>time:
                    break




       #elif 'talk to me' in query:
          #   speak("yes sir")
          #   os.startfile("BRAIN\Brain.py")
          #   break

       elif 'space news' in  query:
            speak("tell me which date's space news you want to know about... ")
            Date = input(":Enter the date:")
            NasaNews(Date)

       elif 'time table' in query:
            time()

       elif 'how to' in query:
            speak("Getting Data From The Internet !")
            op = query.replace("jarvis","")
            max_result = 1
            how_to_func = search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            speak(how_to_func[0].summary)  

       elif 'where are we' in query:
          
            geolocator = Nominatim(user_agent="geoapiExercises")
            location = geolocator.reverse(query="22.4257° N, 87.3199° E" , exactly_one=True)
            address = location.raw['address']
            city = address.get('city', '')
            state = address.get('state', '')
            country = address.get('country', '')
            speak(f"sir , We are now in {city, state, country}")
           

       elif 'headline' in query:
           url = "https://news.google.com/news/rss"
           client = urlopen(url)
           xml_page = client.read()
           client.close()
           page = bs4.BeautifulSoup(xml_page,"xml")
           news_list = page.findAll("item")
           headlines= ""
           for news in news_list:
            headlines+=news.title.text
           speak (f"sir {headlines} .")

       elif 'create a password' in query:
           lower = string.ascii_lowercase
           upper = string.ascii_uppercase
           num = string.digits
           all = lower + upper + num 
           temp = random.sample(all,10)
           password = "".join(temp)
           result=password
           print=(f"You can use {result} as your password")