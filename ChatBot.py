import numpy as np
import speech_recognition as sr
from gtts import gTTS
import os

class ChatBot():
    def __init__(self, name):
        print("----- starting up", name, "-----")
        self.name = name

    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("listening...")
            audio = recognizer.listen(mic)
        try:
            self.text = recognizer.recognize_google(audio)
            print("me --> ", self.text)
        except:
            print("me -->  ERROR")

    def wake_up(self, text):
        return True if self.name in text.lower() else False
    
    @staticmethod
    def text_to_speech(text):
        print("AI --> ", text)
        speaker = gTTS(text=text, lang="en", slow=False)
        speaker.save("res.mp3")
        os.system("start res.mp3")  #if you have a macbook->afplay or for windows use->start
        os.remove("res.mp3")

if __name__ == "__main__":
    ai = ChatBot(name="project")
    while True:
        ai.speech_to_text()
        if ai.wake_up(ai.text):
             res = "Hello I am Dev the AI, what can I do for you?"
        ai.text_to_speech(res)