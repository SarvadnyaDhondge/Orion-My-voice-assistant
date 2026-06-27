"""
folders.py

This module is responsible for opening common Windows folders.

Why is this file separate?

Instead of putting all folder-opening code inside commands.py,
we keep it here so every feature has its own file.

Benefits:

* Cleaner project structure
* Easier to maintain
* Easier to add new folders
* commands.py only decides WHICH skill should handle a command
  """


import os
import subprocess

from speak import speak


# Dictionary of folders Orion can open.
#
# Key   -> Voice command spoken by the user
# Value -> Actual path of the folder on the computer
#
# Example:
# User: "come back open downloads"
# folder_name = "downloads"
# explorer opens the Downloads folder.

FOLDERS = {
    "desktop": os.path.join(os.path.expanduser("~"), "Desktop"),
    "documents": os.path.join(os.path.expanduser("~"), "Documents"),
    "downloads": os.path.join(os.path.expanduser("~"), "Downloads"),
    "pictures": os.path.join(os.path.expanduser("~"), "Pictures"),
    "music": os.path.join(os.path.expanduser("~"), "Music"),
    "videos": os.path.join(os.path.expanduser("~"), "Videos"),
}


def open_folder(folder_name):
    """
    Attempts to open a Windows folder.

    Parameters
    ----------
    folder_name : str
        Name of the folder extracted from the voice command.

    Returns
    -------
    bool
        True  -> This module handled the command.
        False -> Folder is unknown.
                 commands.py should let another module
                 (websites, music, etc.) try instead.
    """

    # If Orion doesn't know this folder,
    # let another skill try to handle the command.
    if folder_name not in FOLDERS:
        return False

    try:
        # Open the folder using Windows File Explorer.
        subprocess.Popen(f'explorer "{FOLDERS[folder_name]}"')

        # Speak confirmation.
        speak(f"Opening {folder_name}")

        # Command handled successfully.
        return True

    except Exception as e:

        # Print the error for debugging.
        print(e)

        # Inform the user.
        speak("Sorry, I couldn't open that folder.")

        # Return True because Orion recognized
        # the command even though opening failed.
        return True