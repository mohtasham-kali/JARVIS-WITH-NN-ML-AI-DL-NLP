# Function
import datetime
import wikipedia
import pywhatkit
from Speak import Say
# 2 Types

# 1 Non Input
# eg: Time, Date, Speedtest
def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)

def Date():
    date = datetime.datetime.today()
    Say(date)

def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)

def NonInputExecution(query):

    query = str(query)

    if "time" in query:
        Time()

    elif "date" in query:
        Date()

    elif "day" in query:
        Date()


# 2 Input
# eg: googlw seach, wikipedia

def InputExecution(tag,query):

    if "wikipedia" in tag:
        name = str(query).replace("who is","").replace("who's","").replace("about","").replace("what is","").replace("what's","").replace("on wikipedia","").replace("wikipedia","")
        result = wikipedia.summary(name)
        Say(result)
    
    elif "google" in tag:
        query = str(query).replace("google","")
        query = query.replace("search","")
        query = query.replace
        pywhatkit.search(query)