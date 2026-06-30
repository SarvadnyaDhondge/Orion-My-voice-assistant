"""
volume.py

This module handles volume-related voice commands.

Responsibilities
----------------
- Understand volume commands.
- Call volume_service.py for system control.
- Speak results to the user.

This module does NOT:
- Directly control system volume
- Use OS APIs
"""

from speak import speak
from services.volume_service import (
    get_volume,
    set_volume,
    volume_up,
    volume_down,
    mute_volume,
    unmute_volume,
)

VOLUME_UP_COMMANDS = [
    "volume up",
    "increase volume",
    "turn up volume",
    "louder",
    "make it louder",
    "raise volume",
]

VOLUME_DOWN_COMMANDS = [
    "volume down",
    "decrease volume",
    "turn down volume",
    "quieter",
    "lower volume",
    "make it quieter",
]

MUTE_COMMANDS = [   
    "mute",
    "mute volume",
]

UNMUTE_COMMANDS = [
    "unmute",
    "unmute volume",
]

VOLUME_COMMANDS = [
    "volume",
    "current volume",
    "what is volume",
]

SET_VOLUME_COMMANDS = [
    "set volume to",
    "set volume at",
    "set volume",
]


def handle_volume(command: str) -> bool:
    """
    Handle volume-related voice commands.

    Returns
    -------
    bool
        True -> command handled
        False -> not a volume command
    """

    command = command.lower().strip()

    # CURRENT VOLUME
    if command in VOLUME_COMMANDS:
        data = get_volume()
        if data["muted"]:
            speak(f"The volume is {data['percent']} percent and it is muted.")
        else:
            speak(f"The volume is {data['percent']} percent.")
        return True

    # VOLUME UP
    if command in VOLUME_UP_COMMANDS:
        current = get_volume()

        if current["percent"] >= 100:
            speak("The volume is already at maximum.")
        else:
            volume_up()
            current = get_volume()
            speak(f"Volume increased to {current['percent']} percent.")

        return True

    # VOLUME DOWN
    if command in VOLUME_DOWN_COMMANDS:
        current = get_volume()

        if current["percent"] <= 0:
            speak("The volume is already at minimum.")
        else:
            volume_down()
            current = get_volume()
            speak(f"Volume decreased to {current['percent']} percent.")

        return True

    # MUTE
    if command in MUTE_COMMANDS:
        mute_volume()
        speak("Volume muted.")
        return True

    # UNMUTE
    if command in UNMUTE_COMMANDS:
        unmute_volume()
        speak("Volume unmuted.")
        return True

    # SET VOLUME
    for phrase in SET_VOLUME_COMMANDS:
        if command.startswith(phrase):
            numbers = [word for word in command.split() if word.isdigit()]

            if numbers:
                percent = int(numbers[0])
                set_volume(percent)
                speak(f"Volume set to {percent} percent.")
            else:
                speak("Please tell me a valid volume percentage.")

            return True

    return False