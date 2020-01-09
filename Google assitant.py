#from gtts import gTTS
import speech_recognition as sr
import pyttsx3
#import playsound
import os
import webbrowser


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()
    '''output = gTTS(text=text,lang='en',slow=False)
    filename = "output.mp3"
    output.save(filename)
    os.system('apg123 output.mp3')
#    playsound.playsound(filename)
#    os.remove(filename)'''
#speak("text to speech recognition ")
def takeCommand():
    
    sr.Microphone(device_index=1)
    
    
    r=sr.Recognizer()
    r.energy_threshold=5000
    with sr.Microphone() as source:
        print("speak")
#        r.pause_threshold= 1
        audio= r.listen(source)
    try:
        text=r.recognize_google(audio)
        print(text)
    except:
        speak("Sorry,i couldn't understand what you just said.")
        return "None"
    return text

c=0
while c<10:
    f=takeCommand().lower()
    if "open chrome" in f:
        speak("opening google chrome")
        os.system("start Chrome")
    if "open excel" in f:
        speak("opening excel")
        os.system("start Excel ")
    if "open youtube" in f:
        speak("opening youtube")
        webbrowser.open_new_tab("https://www.youtube.com")
    if "open paint" in f:
        speak("opening paint")
        os.system("start Paint")
    if "stop" in f:
        speak("okay , i am now shutting down")
        break
    
    
    elif "search" in f:
        f1=f.strip("search")
        url="https://www.google.com/search?q="
        search=url+str(f1)
        speak("i a seraching the web for results")
        webbrowser.open_new(search)
    c+=0    
    