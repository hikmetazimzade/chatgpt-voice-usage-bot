import speech_recognition as sr
from googletrans import Translator
import LanguageChoice as lc

r = sr.Recognizer()
translator=Translator()

chosen_language = lc.Choose_Language()

def Chosen_Language():
    return chosen_language

def Take_Data():
    if chosen_language!=None:
        with sr.Microphone() as source:
            print("Please Talk...")
            audio_text = r.listen(source)#Take data from user by audio
            print("Time Is Over,Thanks!")

            try:
                text=r.recognize_google(audio_text, language = chosen_language)

                prompt=translator.translate(text, dest = "en").text#Since chat gpt works better with English it translates prompt to English

            except:
                print("Your voice was not clear.")

        return prompt