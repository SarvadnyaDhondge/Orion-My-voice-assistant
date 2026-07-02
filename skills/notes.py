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

from pathlib import Path

from speak import speak
from speech import listen


DATA_DIRECTORY = Path("data")
NOTES_FILE = DATA_DIRECTORY / "notes.txt"


ADD_NOTE_COMMANDS = [
    "take a note",
    "write a note",
    "save a note",
]

SHOW_NOTE_COMMANDS = [
    "show my notes",
    "show notes",
    "read my notes",
    "read notes",
]


def add_note():
    """
    Record a voice note and save it.
    """

    speak("What should I write?")

    note = listen()

    if not note:
        speak("I didn't hear anything.")
        return

    note = note.strip()

    if not note:
        speak("I didn't hear anything.")
        return

    DATA_DIRECTORY.mkdir(parents=True, exist_ok=True)

    with open(NOTES_FILE, "a", encoding="utf-8") as file:
        file.write(note + "\n")

    speak("Note saved.")


def show_notes():
    """
    Read all saved notes aloud.
    """

    if not NOTES_FILE.exists():
        speak("You don't have any notes yet.")
        return

    with open(NOTES_FILE, "r", encoding="utf-8") as file:
        notes = file.readlines()

    notes = [note.strip() for note in notes if note.strip()]

    if not notes:
        speak("You don't have any notes yet.")
        return

    speak("Here are your notes.")

    for index, note in enumerate(notes, start=1):
        print(f"{index}. {note}")
        speak(note)


def handle_notes(command):
    """
    Handle note-related voice commands.

    Returns
    -------
    bool
        True  -> Command handled.
        False -> Not a note command.
    """

    command = command.lower().strip()

    if command in ADD_NOTE_COMMANDS:
        add_note()
        return True

    if command in SHOW_NOTE_COMMANDS:
        show_notes()
        return True

    return False