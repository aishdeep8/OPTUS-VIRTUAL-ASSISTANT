import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
import requests
from bs4 import BeautifulSoup
import subprocess


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello I am Optus. How may I help you")       

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

        

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":","-")+ "-note.txt"
    with open(file_name, "w")as f:
        f.write(text)
    subprocess.Popen(["notepad.exe", file_name])      

if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open google maps' in query:
            webbrowser.open("maps.google.com")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")  

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        
        elif 'open instagram' in query:
            webbrowser.open("instagram.com") 

        elif 'open twitter' in query:
            webbrowser.open("twitter.com")    

        elif 'open amazon' in query:
            webbrowser.open("amazon.com")

        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com") 
                      
        elif 'open erp' in query:
            webbrowser.open("student.gehu.ac.in")

        elif 'open yahoo' in query:
            webbrowser.open("yahoo.com")

        elif 'open whatapp' in query:
            webbrowser.open("web.whatsapp.com")  

        elif 'open netflix' in query:
            webbrowser.open("netflix.com") 

        elif 'open hotstar' in query:
            webbrowser.open("hotstar.com") 

        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com") 

        elif 'open quora' in query:
            webbrowser.open("quora.com") 

        elif 'open cricbuzz' in query:
            webbrowser.open("cricbuzz.com")                      

        elif 'the date' in query:
            strDate = datetime.datetime.today().strftime("%Y-%m-%d")
            speak(f"Sir, the date is {strDate}")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")    

        elif 'open code' in query:
            codePath = "C:\\Users\\hp\\Downloads\\VSCodeUserSetup-x64-1.65.0.exe"
            os.startfile(codePath)

        elif 'play music' in query:
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0])) 

        elif 'open teams' in query:
            codePath = "C:\\Users\\hp\Downloads\\Teams_windows_x64.exe"
            os.startfile(codePath)      

        elif 'open office' in query:
            codePath = "C:\\Program Files\\Microsoft Office 15\\ClientX64\\IntegratedOffice.exe"
            os.startfile(codePath)

        elif 'my name' in query: 
            speak("your name is Aishdeep Singh")

        elif 'wish me happy birthday' in query: 
            speak("Happy Birthday Aishdeep") 

        elif 'how are you' in query: 
            speak("I am fine and hope the same for you ") 

        elif 'What is your name' in query: 
            speak("My name is Optus") 

        elif 'are very helpful' in query: 
            speak("Thank you for the compliment")      

        elif 'search on google' in query:
            url='https://google.com/search?q='+query[query.find('googl')+5:]
            webbrowser.get().open(url)
            speak("Showing results of your search") 

        elif 'images of' in query:
            url="https://www.google.com/search?tbm=isch&q="+query[query.find('of')+3:]
            webbrowser.get().open(url)
            speak("Showing images")        

        elif  'temperature' in query:
            search = query
            url= f"http://www.google.com/search?q={search}" 
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current temperature of the given location is {temp}")

        elif 'make a note' in query:
            speak("what would you like me to write?")
            note_text = takeCommand().lower()
            note(note_text)
            speak("I've made a note of that.")

        elif 'my location' in query:
            url = "https://www.google.com/maps/search/My+location+?/"
            webbrowser.get().open(url)
            speak("Showing your current location on google maps...")
        
        elif 'find location of'in query:
            url='https://google.nl/maps/place/'+query[query.find('of')+3:]+'/&amp'
            webbrowser.get().open(url)

        elif 'exit' in query:
            speak('Thank you. Have a good day')  
            exit()  




