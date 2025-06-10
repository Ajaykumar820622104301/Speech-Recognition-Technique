import speech_recognition as sr
from subtitle_display import SubtitleDisplay

def recognize_speech(callback):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    print("Listening...")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)

    while True:
        with mic as source:
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"Recognized: {text}")
            callback(text)
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Request failed; {e}")

if __name__ == "__main__":
    display = SubtitleDisplay()
    recognize_speech(display.update_subtitle)
