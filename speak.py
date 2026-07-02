"""
speak.py

Provides text-to-speech functionality for Orion.

Responsibilities
----------------
- Convert text to speech.
- Print spoken text for debugging.
"""

import pyttsx3


# Initialize the engine only once.
engine = pyttsx3.init("sapi5")

# Optional settings
engine.setProperty("rate", 180)
engine.setProperty("volume", 1.0)


def speak(text):
    """
    Speak the given text.

    Parameters
    ----------
    text : str
        Text to speak.
    """

    print(f"Comeback: {text}")

    engine.say(text)
    engine.runAndWait()