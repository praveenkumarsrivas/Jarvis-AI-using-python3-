import pyttsx3  #module to convert text to speech
import datetime  #module
import speech_recognition as sr
import wikipedia
from googlesearch import search

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome Back")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning Praveen!")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon Praveen")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening Praveen")
    else:
        speak("Goodnight Praveen")

    speak("Jarvis at your service, Please tell me how can i help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listing...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        #speak(query)
        #print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"

    return query


if __name__ == "__main__":
    wishme()
    while (True):
        query = takeCommand().lower()

        if ('time' in query):
            time()

        elif ('date' in query):
            date()

        elif ('wikipedia' in query or 'search' in query or 'what' in query
              or 'who' in query or 'when' in query or 'where' in query):
            speak("searching...")
            query = query.replace("wikipedia", "")
            query = query.replace("search", "")
            result = wikipedia.summary(query, sentences=2)
            print(query)
            print(result)
            speak(result)

        elif ('i am done' in query or 'bye bye jarvis' in query
              or 'nothing for now' in query or 'go offline jarvis' in query
              or 'bye' in query):
            speak("See you next time Bye")
            quit()
