from audioop import add
import os
import tkinter as tk
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
from itertools import count
import subprocess
import webbrowser
import wmi
from ctypes import windll


def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
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
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def killExplorer():
    name = 'explorer.exe'
    f = wmi.WMI()
    for process in f.Win32_Process():
        if process.name == name:
            process.Terminate()
        else:
            pass


def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    letter = ord('a')
    while bitmask > 0:
        if bitmask & 1:
            drives.append(chr(letter))
        bitmask >>= 1
        letter += 1

    return drives


if __name__ == "__main__":
    #takeCommand()
    while True:
        speak("Hi! My Dear Friend. I am ready for your order.")
        query = takeCommand().lower()
        # query = input("Please enter the operation name: ")
        if query == "open my pc":
            i = 0
            for i in count():
                # try:
                    speak("Which Directory You Want to Open?")
                    # # Variable tv is use for taking value for Opening My Computer
                    tv = takeCommand().lower()
                    # tv = input("Please Enter your directory name: ")
                    # tv = tv.replace('Open ', '')
                    print(tv)
                            
                    dbs = '\\'
                    if tv == 'close':
                        break

                    get_drives()

                    if tv in get_drives():
                        # dr variable using for storing directory link.
                        dr = f'{tv}:'
                        print("The if directory is: ", dr)
                        ndr = os.listdir(dr)
                        
                        print(f'This is the if condition result {dr}')
                        print(ndr)
                        webbrowser.open(dr)
                        tv = ''
                        for j in count():
                            speak("Do you want to open file? Please give answer yes or no.")
                            fileOpen = takeCommand().lower()
                            # fileOpen = input("Enter Your file opening condition 'Yes or no': ")
                            if fileOpen == 'yes':
                                speak("Which folder you want to open?")
                                tv1 = takeCommand().lower()
                                # tv1 = input("Enter Your Folder name: ")
                                nndr = []
                                def asb():
                                    for i in range(len(ndr)):
                                        nndr.append(ndr[i].lower())
                                    return nndr

                                print(asb())

                                if tv1 in asb():
                                    asb().clear()
                                    print(asb())
                                    dr = f'{dr}{dbs}{tv1}'
                                    print(f'The Directory is {dr}')
                                    ndr = os.listdir(dr)
                                    print(f"The ndr is {ndr}")
                                    killExplorer()
                                    webbrowser.open(dr)
                                    tv1 = ''
                            elif fileOpen == 'no':
                                break

                            else:
                                pass
                                # speak("Your folder name does not match in this directory.")
                                # break
                                # print("Your Folder name does not match...")
                                # break

                    else:
                        speak("Your Directory is not valid. if you want to stop. Please answer Stop.")
                        dtcom = takeCommand().lower()
                        if dtcom == "stop":
                            break
                        else:
                            continue

        elif "open software" in query:
            pass


        else:
            speak("Do you want to continue this Program? Please Answer Yes yo No.")
            jtp = takeCommand().lower()
            # jtp = input("Enter Your type. :")
            if jtp == "yes" :
                speak("Your Job Type deos not matching. Try again.")

            elif jtp == 'no':
                exit()

