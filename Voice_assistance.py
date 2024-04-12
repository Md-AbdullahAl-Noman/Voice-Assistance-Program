import os
import pyttsx3 
import speech_recognition as sr
import webbrowser as browser
import datetime
import pyjokes
import time

def speech_to_text():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening for speech...")
            audio = recognizer.listen(source)
            try:
                print("Recognizing speech...")
                text = recognizer.recognize_google(audio)
                print("You said: " + text)
                return text
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError:
                print("Could not request results; check your network connection")
    except OSError as e:
        print("No default input device available. Please check your microphone settings.")
        print("System Error Message:", e)


# speechtotext()

def text_to_speech(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate', 120)
    engine.say(x)
    engine.runAndWait()
# text_to_speech("Hello Noman welcome here")


if __name__ == '__main__':
    
    data=speech_to_text().lower()
    
    if "hello noman" in data :
        while True:    
                if "your name" in data:
                        name = "my name is noman"
                        text_to_speech(name)
                elif "how old are you" in data:
                    age="I just born for you now"
                    text_to_speech(age)
                    
                elif "time" in data:
                    time=datetime.datetime.now().strftime("%I:%M%p")
                    text_to_speech(time)
                elif "open youtube" in data:
                    msg="Opening youtube for you"
                    text_to_speech(msg)
                    browser.open("https://www.youtube.com/")
                    
                elif "open github" in data:
                    msg="Opening github for you"
                    text_to_speech(msg)
                    browser.open("https://github.com/Md-AbdullahAl-Noman")
                elif "joke" in data:
                    joke_to_speak=pyjokes.get_joke(language="en",category="neutral")
                    text_to_speech(joke_to_speak)
                elif "open google" in data:
                    msg="Opening google for you"
                    text_to_speech(msg)
                    browser.open("https://www.google.com/")
                elif "open microsoft store" in data:
                    msg = "Opening Microsoft Store for you"
                    text_to_speech(msg)
                    os.system("start ms-windows-store:")
                elif "exit" in data:
                    speech_to_text("Thank you")
                    break
                time.sleep(8)
        
    else:
        print("Thanks noman")