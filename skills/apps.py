"""
apps.py

This module is responsible for opening desktop applications.

Why is this file separate?

Instead of putting all application-opening code inside commands.py,
we keep it here so every feature has its own file.

Benefits:
- Cleaner project structure
- Easier to maintain
- Easier to add new applications
- commands.py only decides WHICH skill should handle a command
"""

import subprocess

from speak import speak


# Dictionary of applications Orion can launch.
#
# Key   -> Voice command spoken by the user
# Value -> Executable path or command used to start the application
#
# Example:
# User: "come back open chrome"
# app_name = "chrome"
# subprocess launches chrome.exe

APPS = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "calculator": "calc.exe",
    "calc": "calc.exe",
    "notepad": "notepad.exe",
    "vs code": "code",
    "vscode": "code",
}


def open_app(app_name):
    """
    Attempts to open a desktop application.

    Parameters
    ----------
    app_name : str
        Name of the application extracted from the voice command.

    Returns
    -------
    bool
        True  -> This module handled the command.
        False -> Application is unknown.
                 commands.py should let another module
                 (folders, websites, etc.) try instead.
    """

    # If Orion doesn't know this application,
    # let another skill try to handle the command.
    if app_name not in APPS:
        return False

    try:
        # Launch the application.
        subprocess.Popen(APPS[app_name])

        # Speak confirmation.
        speak(f"Opening {app_name}")

        # Command handled successfully.
        return True

    except Exception as e:

        # Print the error for debugging.
        print(e)

        # Inform the user.
        speak("Sorry, I couldn't open that application.")

        # Return True because Orion recognized
        # the command even though opening failed.
        return True