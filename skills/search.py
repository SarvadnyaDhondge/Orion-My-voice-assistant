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


def search_google(command):
    """
    Handles Google search commands.

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

    # This module only handles commands
    # that begin with "search ".
    if not command.startswith("search "):
        return False

    # Extract the search query.
    query = command.replace("search", "", 1).strip()

    # Ignore an empty search.
    if not query:
        speak("What would you like me to search?")
        return True

    # Convert spaces into a URL-friendly format.
    encoded_query = quote_plus(query)

    # Build the Google search URL.
    url = f"https://www.google.com/search?q={encoded_query}"

    # Tell the user what Orion is doing.
    speak(f"Searching Google for {query}")

    # Open the search in the default browser.
    webbrowser.open(url)

    return True