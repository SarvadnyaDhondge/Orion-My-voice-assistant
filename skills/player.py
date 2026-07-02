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


PLAY_COMMAND_PREFIX = "play "


def play_music(command):
    """
    Handle music playback commands.

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

    if not command.startswith(PLAY_COMMAND_PREFIX):
        return False

    song = command[len(PLAY_COMMAND_PREFIX):].strip()
    song = song.strip(string.punctuation + " ")

    if not song:
        speak("Please tell me what you want to play.")
        return True

    success = play_song(song)

    if success:
        speak(f"Playing {song}")
    else:
        speak("Sorry, I couldn't find that song.")

    return True