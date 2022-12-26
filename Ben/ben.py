import subprocess
import wolframalpha
import pyttsx3
import json
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import feedparser
import time
import requests
import shutil
from bs4 import BeautifulSoup

class Ben:
    def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)

        self.app_id = "Wolframalpha api id"
        self.client = wolframalpha.Client(self.app_id)

        self.wishMe()
        self.username()

    def speak(audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def wishMe():
        self.hour = int(datetime.datetime.now().hour)
        if self.hour>= 0 and hour<12:
            speak("Good Morning Sir !")

        elif self.hour>= 12 and hour<18:
            speak("Good Afternoon Sir !")

        else:
            speak("Good Evening Sir !")

        self.ben = "Ben"
        speak("I am your Assistant")
        speak(self.ben)
        
    def username():
        speak("What should i call you sir")
        self.uname = takeCommand()
        speak("Welcome Mister")
        speak(self.uname)
        self.columns = shutil.get_terminal_size().columns
        
        print("#####################".center(self.columns))
        print("Welcome Mr.", self.uname.center(self.columns))
        print("#####################".center(self.columns))
        
        speak("How can I help you, Sir")

    def takeCommand():
        
        self.r = sr.Recognizer()
        
        with sr.Microphone() as source:
            
            print("Listening...")
            self.r.pause_threshold = 1
            audio = self.r.listen(source)

        try:
            print("Recognizing...")
            self.query = self.r.recognize_google(audio, language ='en-in')
            print(f"User said: {self.query}\n")

        except Exception as e:
            print(e)
            print("Unable to Recognize your voice.")
            return "None"
        
        return self.query

    def main(self):
        self.query = takeCommand().lower()
        
        if "Ben" in self.query and "wikipedia" in self.query:
            speak('Searching Wikipedia...')
            self.query = self.query.replace("wikipedia", "")
            self.results = wikipedia.summary(self.query, sentences = 3)
            speak("According to Wikipedia")
            print(self.results)
            speak(self.results)

        elif 'Ben' in self.query and "youtube" in self.query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif "Ben" in self.query and "time" in self.query:
            self.strTime = datetime.datetime.now().strftime("% H:% M:% S")
            speak(f"Sir, the time is {self.strTime}")
           
        elif "Ben" in self.query and "joke" in self.query:
            speak(pyjokes.get_joke())            

        elif "Ben" in self.query and "News" in self.query:
            pass
            # not done
            #except Exception as e:
            #    print(str(e))

        elif "Ben where is" in self.query:
            self.query = self.query.replace("where is", "")
            self.location = self.query
            speak("User asked to Locate")
            speak(self.location)
            webbrowser.open("https://www.google.nl / maps / place/" + self.location + "")

        elif "Ben write a note" in self.query:
            speak("What should i write, sir")
            self.note = takeCommand()
            self.file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            self.snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                self.strTime = datetime.datetime.now().strftime("% H:% M:% S")
                self.file.write(self.strTime)
                self.file.write(" :- ")
                self.file.write(self.note)
            else:
                self.file.write(self.note)
        
        elif "Ben" in self.query and "show note" in self.query:
            speak("Showing Notes")
            self.file = open("jarvis.txt", "r")
            print(self.file.read())
            speak(self.file.read(6))

        elif "Ben" in self.query and "weather" in self.query:
            
            # Google Open weather website
            # to get API of Open weather
            api_key = "Api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()
            
            if x["code"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
            
            else:
                speak(" City Not Found ")
            
        elif "send message " in self.query:
                # You need to create an account on Twilio to use this service
                account_sid = 'Account Sid key'
                auth_token = 'Auth token'
                client = Client(account_sid, auth_token)

                message = client.messages \
                                .create(
                                    body = takeCommand(),
                                    from_='Sender No',
                                    to ='Receiver No'
                                )

                print(message.sid)

        elif "i love you" in self.query:
            speak("that's kind of gay not going to lie")

        elif "what is" in self.query or "who is" in self.query:
            self.res = client.self.query(self.query)
            
            try:
                print (next(self.res.results).text)
                speak (next(self.res.results).text)
            except StopIteration:
                print ("No results")

        elif "Ben calculate" in self.query:
            self.indx = self.query.lower().split().index('calculate')
            self.query = self.query.split()[self.indx + 1:]
            self.res = self.client.self.query(' '.join(self.query))
            self.answer = next(self.res.results).text
            print("The answer is " + self.answer)
            speak("The answer is " + self.answer)
