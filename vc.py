import speech_recognition as sr

import pyttsx3
import calc

def talk():
    with sr.Microphone() as source:
        msg = "what is your query?"
        engine.say(msg)
        engine.runAndWait()
        print(msg)
        print("please speak now")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    convert(audio)


def convert(audio):
    try:
        
        text = r.recognize_google(audio)
        print("test1")
        ans = calc.calc(text)
        print("test2")
        print(ans)
        reply(ans, text)
    except:
        msg = "Sorry, we did not get please try again"
        # engine.say(msg)
        print(msg)
        # engine.runAndWait()
    
def reply(ans, text):
    msg="The answer for your query"+text+" is "+ans
    engine.say(msg)
    print("reply")
    print(msg)
    engine.runAndWait()




r = sr.Recognizer()
engine = pyttsx3.init()
talk()
