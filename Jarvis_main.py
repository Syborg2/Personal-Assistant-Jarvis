# Speek Function
import datetime
import pyttsx3
import speech_recognition
import requests
import os
from bs4 import BeautifulSoup
import pyautogui
import webbrowser
import random
import speedtest
import json

from INTRO import play_gif
play_gif
#paste this just below the password function

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

#Alarm

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

# Greet Me Function

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can call me anytime !!")
                    break

# Conversations

                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")

# Fully control on Youtube

                elif "pause" in query:
                 pyautogui.press("k")
                 speak("video paused")
                elif "play" in query:
                 pyautogui.press("k")
                 speak("video played")
                elif "mute" in query:
                 pyautogui.press("m")
                 speak("video muted")
# Volume up/down

                elif "volume up" in query:
                 from keyboard import volumeup
                 speak("Turning volume up,sir")
                 volumeup()
                elif "volume down" in query:
                  from keyboard import volumedown
                  speak("Turning volume down, sir")
                  volumedown()

# open/close
                elif "open" in query:
                 from Dictapp import openappweb
                 openappweb(query)

                elif "close" in query:
                 from Dictapp import closeappweb
                 closeappweb(query)

# Internet Speed Function

                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")

# Google/Youtube Search

                elif "google" in query:
                   from SearchNow import searchGoogle
                   searchGoogle(query)
                elif "youtube" in query:
                   from SearchNow import searchYoutube
                   searchYoutube(query)
                elif "wikipedia" in query:
                   from SearchNow import searchWikipedia
                   searchWikipedia(query)

  #Temperature
                # # elif "temperature" in query:
                #    search = "temperature in kolkata"
                #    url = f"https://www.google.com/search?q={search}"
                #    r  = requests.get(url)
                #    data = BeautifulSoup(r.text,"html.parser")
                #    temp = data.find("div", class_ = "BNeawe").text
                #    speak(f"current{search} is {temp}")

                elif "temperature" in query:
                    def get_weather(api_key, location="Kolkata"):
                        try:
                        # Construct the API URL
                            base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
                            url = f"{base_url}{location}/today?unitGroup=metric&include=current&key={api_key}"

                        # Send the request
                            response = requests.get(url)
                            response.raise_for_status()  # Check for HTTP errors

                        # Parse JSON response
                            data = response.json()

                         # Extract current temperature
                            current_temp = data["currentConditions"]["temp"]
                            return current_temp

                        except requests.exceptions.HTTPError as e:
                            print(f"HTTP Error: {e}")
                            return None
                        except KeyError:
                            print("Error: Invalid API response format.")
                            return None
                        except Exception as e:
                            print(f"Error: {e}")
                            return None
                    # Usage
                    API_KEY = "BKQYWAR96KHVWVGZ3346EFHQZ"
                    temperature = get_weather(API_KEY, "Kolkata")

                    if temperature is not None:
                        speak(f"Current temperature in Kolkata: {temperature}°C")
                    else:
                        speak("Failed to fetch temperature.")


                # elif "temperature" in query:
                #     try:
                #         search = "temperature in kolkata"
                #         url = f"https://www.google.com/search?q={search}"

                #  # Add headers to mimic a real browser
                #         headers = {
                #          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
                #          }

                #         r = requests.get(url, headers=headers)
                #         r.raise_for_status()  # Check for HTTP errors

                #         data = BeautifulSoup(r.text, "html.parser")

                #   # Updated class name (Google frequently changes this)
                #         temp_element = data.find("div", class_="BNeawe iBp4i AP7Wnd")

                #         if temp_element:
                #                           temp = temp_element.text.split("\n")[0]  # Extract temperature value
                #                           speak(f"Current {search} is {temp}")
                #         else:
                #               speak("Sorry, I couldn't fetch the temperature right now.")

                #     except Exception as e:
                #           print(f"Error: {e}")
                #           speak("There was an error fetching the temperature.")

    #Alarm
                elif "set an alarm" in query:
                  print("input time example:- 10 and 10 and 10")
                  speak("Set the time")
                  a = input("Please tell the time :- ")
                  alarm(a)
                  speak("Done,sir")
#Time
                elif "the time" in query:
                  strTime = datetime.datetime.now().strftime("%H:%M")
                  speak(f"Sir, the time is {strTime}")

                elif "finally sleep" in query:
                  speak("Going to sleep,sir")
                  exit()

 # Remember
                elif "remember that" in query:
                 rememberMessage = query.replace("remember that","")
                 rememberMessage = query.replace("jarvis","")
                 speak("You told me to "+rememberMessage)
                 remember = open("Remember.txt","a")
                 remember.write(rememberMessage)
                 remember.close()

                elif "what do you remember" in query:
                 remember = open("Remember.txt","r")
                 speak("You told me to " + remember.read())

# Personalized Playlist

                elif "tired" in query:
                 speak("Playing your favourite songs, sir")
                 a = (1,2,3) # You can choose any number of songs (I have only choosen 3)
                 b = random.choice(a)
                 if b==1:
                  webbrowser.open("https://www.youtube.com/live/gzf7zkOVXmg?si=qpeiht144ixhxrME") #Here put the link of your video
                 elif b==2:
                    webbrowser.open("https://youtu.be/O5gwxm3NxFU?si=bN7180CePmssMf88")
                 elif b==3:
                    webbrowser.open("https://youtu.be/UkvCII0s2Fg?si=Ca3M5mNi9czH60-3")

# News Function

                elif "news" in query:
                 from NewsRead import latestnews
                 latestnews()

# Calculator
                elif "calculate" in query:
                 from Calculatenumbers import WolfRamAlpha
                 from Calculatenumbers import Calc
                 query = query.replace("calculate","")
                 query = query.replace("jarvis","")
                 Calc(query)

# Whatsapp automation

                elif "whatsapp" in query:
                 from Whatsapp import sendMessage
                 sendMessage()

 # Shutdown system

                elif "shutdown the system" in query:
                 speak("Are You sure you want to shutdown")
                 shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                 if shutdown == "yes":
                    os.system("shutdown /s /t 1")

                 elif shutdown == "no":
                   break

# Play a game
                elif "start game" in query:
                   from game import game1_p
                   game1_p()

# SCREENSHOT FUNCTION

                elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")

# CAMERA FUNCTION

                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE SIR !!")
                    pyautogui.press("enter")

 # TRANSLATOR FUNCTION

                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("jarvis","")
                    query = query.replace("translate","")
                    translategl(query)