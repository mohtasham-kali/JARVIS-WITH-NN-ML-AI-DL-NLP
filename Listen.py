
import speech_recognition as sr # pip install speechrecognition

def Listen():
    r = sr.Recognizer()


    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source,0,5)


    try:
        print("Recogizing...")
        query = r.recogize_google(audio, language="en-in")
        print(f"You Said : {query}")

    except:
        return ""

    query = str(query)
    return query.lower()