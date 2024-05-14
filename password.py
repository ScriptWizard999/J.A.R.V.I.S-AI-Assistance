import speech_recognition as sr
import pyttsx3
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',170)


def speak(audio):
    print("   ")
    print(f": {audio}")
    engine.say(audio)
    print("    ")
    engine.runAndWait()

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
        print(e)    
        print("Say that again please...")  
        return "None"
    return query

def Pass(pass_inp):

    password = "naruto"
    passs = str(password)
    if passs==str(pass_inp):
       speak("access granted")
       import jarvis

    else:
        speak("access not granted")
