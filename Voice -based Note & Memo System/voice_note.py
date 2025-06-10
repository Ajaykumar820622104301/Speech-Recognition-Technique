import speech_recognition as sr
import pyttsx3
from datetime import datetime
import os

class VoiceNoteSystem:
    def __init__(self, notes_dir="notes"):
        self.recognizer = sr.Recognizer()
        self.tts_engine = pyttsx3.init()
        os.makedirs(notes_dir, exist_ok=True)
        self.notes_dir = notes_dir

    def listen(self):
        with sr.Microphone() as source:
            print("Listening for note...")
            audio = self.recognizer.listen(source)
        try:
            text = self.recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Could not understand audio."
        except sr.RequestError as e:
            return f"Request error: {e}"

    def save_note(self, text):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(self.notes_dir, f"note_{timestamp}.txt")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(text)
        return filename

    def speak(self, text):
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()
