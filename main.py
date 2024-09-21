# import Necessary libraries

import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests 
from openai import OpenAI


recogniser = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "your_api_key_here"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(api_key = "Your_ApiKey_here") # enter your api key here

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual asssistant named jarvis skilled in general tasks like alexa and google cloud."},
        {
            "role": "user",
            "content": command
        }
    ]
    )
    return completion.choices[0].message.content

def processCommand(c):
    if "how are you" in c.lower():
        speak("Feeling Amazing")

    elif "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif "open ai" in c.lower():
        webbrowser.open("https://openai.com")

    elif c.lower().startswith("play"):
        songs = " ".join(c.lower().split(" ")[1:])
        link = musicLibrary.music[songs]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=jp&apiKey={newsapi}")
        if r.status_code == 200:
        # Parse the response JSON
            data = r.json() 
        
        # Extract and print the headlines
            articles = data.get('articles', [])
        
        if articles:
            for i, article in enumerate(articles[:10], start=1):
                speak(f"{i}. {article['title']}")
        else:
            speak("No articles found.")
    
    else:
        # OpenAI Handles the other requests
        output = aiProcess(c)
        speak(output)


# Main funtion here
if __name__ == "__main__":
    speak("...Initializing Jarvis.......")

    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone

        r = sr.Recognizer()

        # recognize speech using google
        print("Recognizing.......")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=2 , phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yeah")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))