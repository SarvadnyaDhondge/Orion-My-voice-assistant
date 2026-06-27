"""
websites.py

This module is responsible for opening websites in the default web browser.

Why is this file separate?

Instead of putting all website-opening code inside commands.py,
we keep it here so every feature has its own file.

Benefits:
- Cleaner project structure
- Easier to maintain
- Easy to add new websites
- commands.py only decides WHICH skill should handle a command
"""

import webbrowser

from speak import speak


# Dictionary of websites Orion can open.
#
# Key   -> Voice command spoken by the user
# Value -> Website URL
#
# Example:
# User: "come back open google"
# website_name = "google"
# Orion opens https://www.google.com

WEBSITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://github.com",
}


def open_website(website_name):
    """
    Attempts to open a website.

    Parameters
    ----------
    website_name : str
        Name of the website extracted from the voice command.

    Returns
    -------
    bool
        True  -> This module handled the command.
        False -> Website is unknown.
                 commands.py should let another module
                 try instead.
    """

    # If Orion doesn't know this website,
    # let another skill try.
    if website_name not in WEBSITES:
        return False

    try:
        # Open the website in the default browser.
        webbrowser.open(WEBSITES[website_name])

        # Speak confirmation.
        speak(f"Opening {website_name}")

        # Command handled successfully.
        return True

    except Exception as e:

        # Print the error for debugging.
        print(e)

        # Inform the user.
        speak("Sorry, I couldn't open that website.")

        # Return True because Orion recognized
        # the command even though opening failed.
        return True