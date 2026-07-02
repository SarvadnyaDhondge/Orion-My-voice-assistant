"""
command_normalizer.py

Purpose
-------
Normalize spoken commands before they reach the skills.

Responsibilities
----------------
- Convert text to lowercase.
- Remove punctuation.
- Remove extra whitespace.
- Correct common speech-recognition mistakes.

This keeps command handling simple and consistent.
"""

import re


REPLACEMENTS = {

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

    # ---------- Temperature ----------
    "forecast": "temperature",

    # ---------- VS Code ----------
    "vscode": "vs code",
}


def normalize_command(command):
    """
    Clean and normalize spoken commands.

    Parameters
    ----------
    command : str

    Returns
    -------
    str
        Normalized command.
    """

    command = command.lower()

    # Remove punctuation
    command = re.sub(r"[^\w\s]", "", command)

    # Remove extra whitespace
    command = " ".join(command.split())

    # Correct common recognition mistakes
    for wrong, correct in REPLACEMENTS.items():
        command = re.sub(
            rf"\b{re.escape(wrong)}\b",
            correct,
            command,
        )

    return command