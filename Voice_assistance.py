import os
import pyttsx3 
import speech_recognition as sr
import datetime
import pyjokes
import webbrowser

def speech_to_text():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening for speech...")
            audio = recognizer.listen(source)
            print("Recognizing speech...")
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
            return text.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError:
        print("Could not request results; check your network connection")
    except OSError as e:
        print("No default input device available. Please check your microphone settings.")
        print("System Error Message:", e)
    return None

def text_to_speech(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate', 120)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    
    while True:
        input_text = speech_to_text()
        if input_text is not None:
            if "hello noman" in input_text:
                text_to_speech("Hello, how can I assist you?")
                while True: 
                    data = speech_to_text()
                    if data:
                        if "your name" in data:
                            text_to_speech("My name is Noman")
                        elif "how old are you" in data:
                            text_to_speech("I just born for you now")
                        elif "time" in data:
                            time_now = datetime.datetime.now().strftime("%I:%M%p")
                            text_to_speech("The current time is " + time_now)
                        elif "open youtube" in data:
                            text_to_speech("Opening youtube for you")
                            webbrowser.open("https://www.youtube.com/")
                        elif "open github" in data:
                            text_to_speech("Opening github for you")
                            webbrowser.open("https://github.com/Md-AbdullahAl-Noman")
                        elif "joke" in data:
                            joke = pyjokes.get_joke(language="en", category="neutral")
                            text_to_speech(joke)
                        elif "open google" in data:
                            webbrowser.open( "https://www.google.com/")
                            text_to_speech("Opening google for you")
                            
                        elif "open microsoft store" in data:
                            text_to_speech("Opening Microsoft Store for you")
                            webbrowser.open("ms-windows-store:")
                        elif "exit" in data:
                            text_to_speech("Thank you")
                            break
                    # time.sleep(5)
            else:
                print("Thanks Noman")
                break
