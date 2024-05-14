from datetime import datetime
import pyttsx3

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


Sevento8 = '''
Time to wakeup sir ... your sleeping time is over... 
now you have to get ready for your works...
and dont forget to send a text msg about goodmorning to your girl...
have a good day sir...
'''
Nineto12 = '''
time for your study sir... if you need any kind of  help
just ask me ... 
'''

def time():
    hour = int(datetime.now().strftime("%H"))
    
    if hour>=7 and hour<8:
        speak(Sevento8)
        return Sevento8

    elif hour>=9 and hour<12:
        speak(Nineto12)
        return Nineto12

    else:
        speak("THERE IS NOTHING IN SCHEDULE")
        return '''THERE IS NOTHING IN SCHEDULE'''
