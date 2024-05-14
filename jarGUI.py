from JARVISUI import Ui_jarvisUI
from PyQt5 import QtCore , QtWidgets , QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr

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



class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self
    
    def takeCommand(self):
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
        