"""
notes.py

This module is responsible for creating and reading notes.

Why is this file separate?

Instead of putting note-related code inside commands.py,
we keep it here so every feature has its own file.

Benefits:
- Cleaner project structure
- Easier to maintain
- Easy to add future note features
- commands.py only decides WHICH skill should handle a command
"""

import os

from speak import speak
from speech import listen


# Path to the notes file.
NOTES_FILE = os.path.join("data", "notes.txt")


def add_note():
    """
    Records a voice note and saves it to notes.txt.
    """

    speak("What should I write?")

    note = listen()

    if not note:
        speak("I didn't hear anything.")
        return

    with open(NOTES_FILE, "a", encoding="utf-8") as file:
        file.write(note + "\n")

    speak("Note saved.")


def show_notes():
    """
    Reads all saved notes aloud.
    """

    if not os.path.exists(NOTES_FILE):
        speak("You don't have any notes yet.")
        return

    with open(NOTES_FILE, "r", encoding="utf-8") as file:
        notes = file.readlines()

    if not notes:
        speak("You don't have any notes yet.")
        return

    speak("Here are your notes.")

    for index, note in enumerate(notes, start=1):
        note = note.strip()

        if note:
            print(f"{index}. {note}")
            speak(note)


def handle_notes(command):
    """
    Handles note-related voice commands.

    Returns
    -------
    bool
        True  -> Note command handled.
        False -> Not a note command.
    """

    command = command.lower()

    if "take a note" in command:
        add_note()
        return True

    if "show my notes" in command:
        show_notes()
        return True

    return False