from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write 
import webbrowser
from time import sleep

def WhatsappMsg(name,massage):
    webbrowser.open("https://web.whatsapp.com/")

    sleep(20)

    click(x=313 , y=259)

    sleep(1)

    write(name)
     
    sleep(1)

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

    webbrowser.open("https://www.instagram.com/")

    sleep(5)

    click(x=89, y=558)

def instagramNotf():

    sleep(2)

    click(x=44, y=640)



