import pyttsx3
import os
import datetime
import speech_recognition as sr
import requests
from PIL import Image

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',190)


def speak(audio):
    print("   ")
    print(f": {audio}")
    engine.say(audio)
    print("    ")
    engine.runAndWait()

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
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

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

NasaNews('2000-01-09')