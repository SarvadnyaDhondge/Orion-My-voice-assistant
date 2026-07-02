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
DEBUG = True


speak("Initializing Comeback")


def clean_text(text: str) -> str:
    """
    Perform basic cleanup before normalization.
    """

    if not text:
        return ""

    text = text.lower()

    for char in ",.!?":
        text = text.replace(char, "")

    return text.strip()


def listen_and_prepare() -> tuple[str, str]:
    """
    Listen to the user's speech and prepare it for processing.

    Returns
    -------
    tuple[str, str]
        (raw_text, normalized_text)

        Returns ("", "") if nothing was recognized.
    """

    raw_text = listen()
    raw_text = clean_text(raw_text)

    if not raw_text:
        return "", ""

    normalized_text = normalize_command(raw_text)

    return raw_text, normalized_text


while True:

    if DEBUG:
        print("\nWaiting for wake word...")

    # ---------------- Listen ----------------

    raw_text, text = listen_and_prepare()

    if not raw_text:
        continue

    if DEBUG:
        print("Raw        :", raw_text)
        print("Normalized :", text)

    # ---------------- Wake Word ----------------

    if WAKE_WORD not in text:
        continue

    command = text.replace(WAKE_WORD, "", 1).strip()

    # Wake word + command together
    if command:

        if DEBUG:
            print("Direct command:", command)

        result = handle_command(command)

    # Only wake word
    else:

        speak("Yes?")

        raw_command, command = listen_and_prepare()

        if not raw_command:
            continue

        if DEBUG:
            print("Raw command        :", raw_command)
            print("Normalized command :", command)

        result = handle_command(command)

    if result == "stop":
        speak("Goodbye")
        break

    time.sleep(0.2)