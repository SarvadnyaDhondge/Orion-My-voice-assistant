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


APPLICATIONS = {
    "calc": "calc.exe",
    "calculator": "calc.exe",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "notepad": "notepad.exe",
    "vs code": "code",
    "vscode": "code",
}


def open_app(app_name):
    """
    Attempt to open a desktop application.

    Parameters
    ----------
    app_name : str
        Name of the application.

    Returns
    -------
    bool
        True  -> Command handled.
        False -> Application is unknown.
    """

    if app_name not in APPLICATIONS:
        return False

    application = APPLICATIONS[app_name]

    try:
        subprocess.Popen(application)
        speak(f"Opening {app_name}")
        return True

    except Exception as e:
        print(f"Failed to open '{app_name}': {e}")
        speak("Sorry, I couldn't open that application.")
        return True