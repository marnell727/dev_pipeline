import speech_recognition as sr
import pyttsx3
import datetime
import os

listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('Hello Dev Pipeline')
engine.runAndWait()

r = sr.Recognizer()
with sr.Microphone() as source:
    print('Say something!')
    audio = r.listen(source)

try:
    print('Sphinx thinks you said ' + r.recognize_audio(audio))
except sr. UnknownValueError:
    print('Sphinx could not understand audio')
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))