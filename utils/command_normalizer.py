"""
command_normalizer.py

Purpose
-------
Whisper does not always recognize words correctly.

Instead of making every skill handle speech mistakes,
we fix them here.

This module receives the raw text from Whisper,
cleans it,
replaces common mistakes,
and returns a standardized command.

This keeps commands.py simple.
"""

import re


# Common Whisper mistakes
REPLACEMENTS = {
    # ---------- Temperature ----------
    "forecast": "temperature",

    # ---------- Google ----------
    "gogle": "google",
    "googel": "google",
    "googal": "google",

    # ---------- GitHub ----------
    "githab": "github",
    "git hub": "github",
    "gitub": "github",

    # ---------- Notepad ----------
    "note pad": "notepad",

    # ---------- VS Code ----------
    "vscode": "vs code",
}


def normalize_command(command):
    """
    Clean and normalize spoken commands.
    """

    command = command.lower()

    # Remove punctuation
    command = re.sub(r"[^\w\s]", "", command)

    # Remove extra spaces
    command = " ".join(command.split())

    # Replace commonly misheard words
    for wrong, correct in REPLACEMENTS.items():
        command = command.replace(wrong, correct)

    return command