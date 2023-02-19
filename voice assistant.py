import pyttsx3 #having functions which possibles text to speech
import speech_recognition as sr # for speech rcognition
import webbrowser # for searching
import datetime # date time rel
import pyjokes # for jokes
import os
import time




def sptext():                     # fuction for speech to text conversion
    recognizer=sr.Recognizer() #class for catch the words spoken by us
    with sr.Microphone() as source: # taking the microphone a source(input)
        print("Hello buddy how can i help you")
        recognizer.adjust_for_ambient_noise(source) # func for remove unwanted noise of source
        audio = recognizer.listen(source)# function listning the source
        try:
            print("recoginizing...")
            data = recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print("sorry i don't get it please speak again")
def speechtx(x):
    engine = pyttsx3.init() # class that use for the functions and get  data and speak or given output through speaking
    voices = engine.getProperty("voices") # function that have voices properties
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate') # property for define the rate of voice
    engine.setProperty('rate',150)
    engine.say(x) # function for speaking the text
    engine.runAndWait()# whatever it speak this function run and wait it
if __name__ == "__main__":
    speechtx("Hello i am Friday sir how can i help you ")
    #sptext()
    while True:
        data1 = sptext().lower()
        if "your name" in data1:
            name = "my name is Friday sir"
            speechtx(name)
        elif "old are you" in data1:
            age = "i am just few days old"
            speechtx(age)
        elif "time" in data1:
            time = datetime.datetime.now().strftime("%I%M%p")
            speechtx(time)
        elif "youtube" in data1:
            webbrowser.open("https://www.youtube.com/")
        elif "spotify" in data1:
            webbrowser.open("https://open.spotify.com/")
        elif "joke" in data1:
            joke = pyjokes.get_joke(language="en",category="neutral")
            speechtx(joke)
        elif "play song" in data1:
            add = "D:\MUSIC\SpotiFlyer\Playlists\Priyanshu_s_playlist"
            listsong = os.listdir(add)
            
            os.startfile(os.path.join(add,listsong[31]))
        elif "exit" in data1:
            speechtx("Thankyou sir for interacting with us Have a great day ahead")
            break
        else:
            speechtx("sorry sir its out of my reach say anything else")
        time.sleep(5)