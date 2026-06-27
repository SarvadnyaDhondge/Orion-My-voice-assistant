"""
player.py

This module is responsible for handling music playback commands.

Why is this file separate?

The actual logic for searching and playing music already exists
inside music.py.

This module acts as a bridge between commands.py and music.py.

Benefits:
- commands.py stays clean.
- Music-related commands stay in one place.
- Future music features (pause, resume, next, previous,
  volume, playlists, etc.) can all be added here.
"""

import string

from speak import speak
from music import play_song


def play_music(command):
    """
    Handles commands that begin with 'play'.

    Parameters
    ----------
    command : str
        Full voice command.

    Returns
    -------
    bool
        True  -> Music command handled.
        False -> Not a music command.
    """

    # This module only handles commands that start with "play".
    if not command.startswith("play "):
        return False

    # Extract the song name.
    song = command.replace("play", "", 1).strip()
    song = song.strip(string.punctuation + " ")

    # Tell the user what Orion is doing.
    speak(f"Playing {song}")

    # Use the existing function from music.py.
    success = play_song(song)

    if not success:
        speak("Sorry, I couldn't find that song.")

    return True