"""
Main.py

Entry point for Orion.

Workflow:
1. Wait for the wake word.
2. Listen to the user.
3. Normalize the spoken text.
4. Execute the command.
"""

import time

from speak import speak
from speech import listen
from commands import handle_command
from utils.command_normalizer import normalize_command


WAKE_WORD = "come back"


speak("Initializing Comeback")


def clean_text(text):
    """
    Basic cleanup before normalization.
    """

    if not text:
        return ""

    text = text.lower()
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.strip()

    return text


while True:

    print("\nWaiting for wake word...")

    # ---------------- Listen ----------------

    raw_text = listen()

    raw_text = clean_text(raw_text)

    if not raw_text:
        continue

    text = normalize_command(raw_text)

    print("Raw        :", raw_text)
    print("Normalized :", text)

    # ---------------- Wake Word ----------------

    if WAKE_WORD in text:

        command = text.replace(WAKE_WORD, "").strip()

        # Wake word + command together
        if command:

            print("Direct command:", command)

            result = handle_command(command)

        # Only wake word
        else:

            speak("Yes?")

            raw_command = listen()

            raw_command = clean_text(raw_command)

            if not raw_command:
                continue

            command = normalize_command(raw_command)

            print("Raw command        :", raw_command)
            print("Normalized command :", command)

            result = handle_command(command)

    else:
        continue

    if result == "stop":
        speak("Goodbye")
        break

    time.sleep(0.2)