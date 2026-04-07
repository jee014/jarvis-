"""import json
import os
from pipes import quote
import re
import sqlite3
import struct
import subprocess
import time
import webbrowser"""

#from playsound import playsound
import re
import os
import struct
from time import time
import pvporcupine # pyright: ignore[reportMissingImports]

import eel
#from pywhatkit import playonyt
#import pyaudio
#import pyautogui
from engine.command import speak
from engine.config import ASSISTANT_NAME
from hugchat import hugchat # pyright: ignore[reportMissingImports]



def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query = query.lower()

    if query!="":
        speak(f"Opening "+query)
        os.system('start ' +query)
    else:
        speak("Please specify what you want to open.")
"""
def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    playonyt(search_term)
    
def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else "None"
"""
"""
def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
        porcupine = pvporcupine.create(
            keywords=["jarvis","alexa"],
            sensitivities=[0.9,0.9]
        )

        paud = pyaudio.PyAudio()

        audio_stream = paud.open(
            rate=16000,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            input_device_index=5,
            frames_per_buffer=porcupine.frame_length
        )

        print("Listening...")

        while True:
            keyword = audio_stream.read(
                porcupine.frame_length,
                exception_on_overflow=False
            )

            keyword = struct.unpack_from("h"*porcupine.frame_length, keyword)

            keyword_index = porcupine.process(keyword)

            if keyword_index >= 0:
                print(" Hotword detected")

                import pyautogui as autogui # pyright: ignore[reportMissingModuleSource]
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")

    except Exception as e:
        print("Error:", e)

    finally:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()

hotword() """


# chat bot 
def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine\cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response =  chatbot.chat(user_input)
    print(response)
    speak(response)
    return response