import re
import speech_recognition as sr # pip install speechrecognition

def Listen():
    r = sr.Recogizer()


    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,4)


    try:
        print("Recogizing...")
        query = r.recogize_google(audio, language="en-us")
        print(f"You Said : {query}")

    except:
        return ""

    query = str(query)
    return query.lower()