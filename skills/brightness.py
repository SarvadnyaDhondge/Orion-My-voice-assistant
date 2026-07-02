"""
brightness.py

This module handles brightness-related voice commands.

Responsibilities
----------------
- Understand brightness commands.
- Call brightness_service.py for system control.
- Speak results to the user.

This module does NOT:
- Directly control system brightness.
"""

from speak import speak
from services.brightness_service import (
    get_brightness,
    set_brightness,
    brightness_up,
    brightness_down,
)


BRIGHTNESS_UP_COMMANDS = [
    "brightness up",
    "increase brightness",
    "turn up brightness",
    "brighter",
    "make it brighter",
    "raise brightness",
]

BRIGHTNESS_DOWN_COMMANDS = [
    "brightness down",
    "decrease brightness",
    "turn down brightness",
    "dimmer",
    "make it dimmer",
    "lower brightness",
]

BRIGHTNESS_COMMANDS = [
    "brightness",
    "current brightness",
    "what is brightness",
]

SET_BRIGHTNESS_COMMANDS = [
    "set brightness to",
    "set brightness at",
    "set brightness",
]


def handle_brightness(command: str) -> bool:
    """
    Handle brightness-related voice commands.

    Returns
    -------
    bool
        True -> Command handled.
        False -> Not a brightness command.
    """

    command = command.lower().strip()

    # CURRENT BRIGHTNESS
    if command in BRIGHTNESS_COMMANDS:

        brightness = get_brightness()

        if brightness is None:
            speak("Sorry, I couldn't get the current brightness.")
        else:
            speak(
                f"The current brightness is {brightness['percent']} percent."
            )

        return True

    # BRIGHTNESS UP
    if command in BRIGHTNESS_UP_COMMANDS:

        current = get_brightness()

        if current is None:
            speak("Sorry, I couldn't get the current brightness.")
            return True

        if current["percent"] >= 100:
            speak("Brightness is already at maximum.")
            return True

        brightness = brightness_up()

        if brightness is None:
            speak("Sorry, I couldn't increase the brightness.")
        else:
            speak(
                f"Brightness increased to {brightness['percent']} percent."
            )

        return True

    # BRIGHTNESS DOWN
    if command in BRIGHTNESS_DOWN_COMMANDS:

        current = get_brightness()

        if current is None:
            speak("Sorry, I couldn't get the current brightness.")
            return True

        if current["percent"] <= 0:
            speak("Brightness is already at minimum.")
            return True

        brightness = brightness_down()

        if brightness is None:
            speak("Sorry, I couldn't decrease the brightness.")
        else:
            speak(
                f"Brightness decreased to {brightness['percent']} percent."
            )

        return True

    # SET BRIGHTNESS
    for phrase in SET_BRIGHTNESS_COMMANDS:

        if command.startswith(phrase):

            numbers = [word for word in command.split() if word.isdigit()]

            if not numbers:
                speak("Please tell me a valid brightness percentage.")
                return True

            percent = int(numbers[0])

            brightness = set_brightness(percent)

            if brightness is None:
                speak("Sorry, I couldn't change the brightness.")
            else:
                speak(
                    f"Brightness set to {brightness['percent']} percent."
                )

            return True

    return False