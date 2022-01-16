import os
import socket
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
from itertools import count
import webbrowser
import wmi
from ctypes import windll


def check_internet():
    try:
        socket.create_connection(("google.com", 80))
        return True

    except OSError:
        return False


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
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        speak("Sorry! Please Say Again Please....")
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
        if check_internet() is True:
            speak("Hi! My Dear Friend. I am ready for your order. Do you want to open your Computer Drive? Please Answer Yes or No.")
            query = takeCommand().lower()
            print(query)
            # query = input("Please enter the operation name: ")
            if query == "yes":
                i = 0
                for i in count():
                    # try:
                        speak("Which Directory You Want to Open?")
                        # Variable tv is use for taking value for Opening My Computer
                        tv = takeCommand().lower()
                        # print(tv)
                                
                        dbs = '\\'
                        if tv == 'close':
                            break

                        get_drives()

                        if tv in get_drives():
                            # dr variable using for storing directory link.
                            dr = f'{tv}:'
                            print("The if directory is: ", dr)
                            ndr = os.listdir(dr)
                            
                            # print(f'This is the if condition result {dr}')
                            # print(ndr)
                            webbrowser.open(dr)
                            speak(f"{tv} Directory is Open.")
                            tv = ''
                            for j in count():
                                speak("Do you want to open Folder? Please give answer yes or no.")
                                foldOpen = takeCommand().lower()
                                # fileOpen = input("Enter Your file opening condition 'Yes or no': ")
                                if foldOpen == 'yes':
                                    speak("Which folder you want to open?")
                                    tv1 = takeCommand().lower()
                                    # tv1 = input("Enter Your Folder name: ")
                                    nndr = []
                                    def asb():
                                        for i in range(len(ndr)):
                                            nndr.append(ndr[i].lower())
                                        return nndr

                                    # print(asb())

                                    if tv1 in asb():
                                        asb().clear()
                                        # print(asb())
                                        dr = f'{dr}{dbs}{tv1}'
                                        # print(f'The Directory is {dr}')
                                        ndr = os.listdir(dr)
                                        # print(f"The ndr is {ndr}")
                                        killExplorer()
                                        webbrowser.open(dr)
                                        speak(f"{tv1} Folder is Open.")
                                        tv1 = ''
                                elif foldOpen == 'no':
                                    speak("Thank You.")
                                    break

                                else:
                                    continue
                                

                        else:
                            speak("Your Directory is not valid. if you want to stop. Please answer Stop.")
                            dtcom = takeCommand().lower()
                            if dtcom == "stop":
                                speak("Thank You.")
                                break
                            else:
                                continue

            elif query =="no":
                speak("Thank You.")
                exit()


            else:
                speak("Do you want to continue this Program? Please Answer Yes yo No.")
                jtp = takeCommand().lower()
                # jtp = input("Enter Your type. :")
                if jtp == "yes" :
                    speak("Your Job Type deos not matching. Try again.")
                    continue

                elif jtp == 'no':
                    speak("Thank You My Dear Friend. I am going to sleep.")
                    exit()

                else:
                    speak("Thank You My Dear Friend. I am going to sleep.")
                    exit()
        else:
            speak("Your Internet Connection is Lost. Please Confirm Your Internet Connection.")
            exit()
