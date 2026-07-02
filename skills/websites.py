"""
websites.py

This module is responsible for opening websites.

Responsibilities
----------------
- Open supported websites in the default browser.

This module does NOT:
- Speak commands.
- Listen to the user.
- Decide which command to execute.
"""

import webbrowser

from speak import speak


WEBSITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://github.com",
}


def open_website(website_name):
    """
    Open a supported website.

    Parameters
    ----------
    website_name : str
        Website name extracted from the command.

    Returns
    -------
    bool
        True  -> Command handled.
        False -> Website not found.
    """

    url = WEBSITES.get(website_name)

    if url is None:
        return False

    try:

        webbrowser.open(url)

        speak(f"Opening {website_name}")

        return True

    except Exception as e:

        print(f"Website Error: {e}")

        speak("Sorry, I couldn't open that website.")

        return True