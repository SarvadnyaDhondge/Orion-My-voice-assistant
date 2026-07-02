"""
folders.py

This module is responsible for opening common Windows folders.

Why is this file separate?

Instead of putting all folder-opening code inside commands.py,
we keep it here so every feature has its own file.

Benefits
--------
- Cleaner project structure
- Easier to maintain
- Easier to add new folders
- commands.py only decides WHICH skill should handle a command
"""

import os
import subprocess

from speak import speak


HOME_DIRECTORY = os.path.expanduser("~")

FOLDER_PATHS = {
    "desktop": os.path.join(HOME_DIRECTORY, "Desktop"),
    "documents": os.path.join(HOME_DIRECTORY, "Documents"),
    "downloads": os.path.join(HOME_DIRECTORY, "Downloads"),
    "music": os.path.join(HOME_DIRECTORY, "Music"),
    "pictures": os.path.join(HOME_DIRECTORY, "Pictures"),
    "videos": os.path.join(HOME_DIRECTORY, "Videos"),
}


def open_folder(folder_name):
    """
    Attempt to open a Windows folder.

    Parameters
    ----------
    folder_name : str
        Name of the folder.

    Returns
    -------
    bool
        True  -> Command handled.
        False -> Folder is unknown.
    """

    if folder_name not in FOLDER_PATHS:
        return False

    folder_path = FOLDER_PATHS[folder_name]

    try:
        subprocess.Popen(["explorer", folder_path])
        speak(f"Opening {folder_name}")
        return True

    except Exception as e:
        print(f"Failed to open folder '{folder_name}': {e}")
        speak("Sorry, I couldn't open that folder.")
        return True