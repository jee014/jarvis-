import pyttsx3
import speech_recognition as sr
import eel

engine = pyttsx3.init()

def speak(audio):
    text = str(audio)
    if audio:
        engine.say(text)
        eel.receiverText(text)
        engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=5, phrase_time_limit=8)

    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("You said:", query)
        eel.DisplayMessage(query)
        speak(query)
        eel.ShowHood()
        return query.lower()
    except Exception as e:
        print("Error:", e)
        eel.DisplayMessage("Sorry, I didn't catch that.")
        return ""

@eel.expose
def allCommands(message=1):
    if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)