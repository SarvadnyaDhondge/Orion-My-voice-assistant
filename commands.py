import string
from datetime import datetime

from speak import speak
from skills.apps import open_app
from skills.folders import open_folder
from skills.websites import open_website
from skills.player import play_music
from skills.search import search_google
from skills.notes import handle_notes
from skills.weather import handle_weather
from skills.reminder import handle_reminder
from skills.system import handle_system
from skills.volume import handle_volume
from skills.brightness import handle_brightness


STOP_COMMANDS = [
    "stop",
    "exit",
    "quit",
]


SKILL_HANDLERS = (
    search_google,
    handle_weather,
    handle_reminder,
    handle_system,
    play_music,
    handle_notes,
    handle_volume,
    handle_brightness,
)


def handle_command(command):
    """
    Route the user's command to the appropriate skill.
    """

    command = command.lower().strip().strip(string.punctuation)

    print(f"Executing command: {command}")

    # ---------------- OPEN ----------------

    if command.startswith("open"):

        item = command.replace("open", "", 1).strip()

        if open_app(item):
            return

        if open_folder(item):
            return

        if open_website(item):
            return

        speak("I don't know how to open that.")
        return

    # ---------------- SKILLS ----------------

    for handler in SKILL_HANDLERS:
        if handler(command):
            return

    # ---------------- TIME ----------------

    if "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
        return

    # ---------------- IDENTITY ----------------

    if "your name" in command:
        speak("My name is Orion.")
        return

    # ---------------- STOP ----------------

    if command in STOP_COMMANDS:
        speak("Goodbye")
        return "stop"

    # ---------------- UNKNOWN ----------------

    speak("Sorry, I don't know that command yet.")