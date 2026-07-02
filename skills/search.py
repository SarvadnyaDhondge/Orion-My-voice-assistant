"""
search.py

This module is responsible for searching Google.

Why is this file separate?

Instead of putting all search-related code inside commands.py,
we keep it here so every feature has its own file.

Benefits:
- Cleaner project structure
- Easier to maintain
- Easy to add more search engines later
- commands.py only decides WHICH skill should handle a command
"""

import webbrowser
from urllib.parse import quote_plus

from speak import speak


SEARCH_COMMAND_PREFIX = "search "

GOOGLE_SEARCH_URL = "https://www.google.com/search?q={}"


def search_google(command):
    """
    Handle Google search commands.

    Parameters
    ----------
    command : str
        Full voice command.

    Returns
    -------
    bool
        True  -> Search command handled.
        False -> Not a Google search command.
    """

    if not command.startswith(SEARCH_COMMAND_PREFIX):
        return False

    query = command[len(SEARCH_COMMAND_PREFIX):].strip()

    if not query:
        speak("What would you like me to search?")
        return True

    encoded_query = quote_plus(query)

    url = GOOGLE_SEARCH_URL.format(encoded_query)

    speak(f"Searching Google for {query}")

    webbrowser.open(url)

    return True