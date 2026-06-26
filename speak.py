import pyttsx3

def speak(text):
    print("Comeback:", text)

    engine = pyttsx3.init('sapi5')
    engine.say(text)
    engine.runAndWait()
    engine.stop()