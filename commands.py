import webbrowser
import string
from datetime import datetime

from speak import speak
from skills.apps import open_app
from skills.folders import open_folder
from skills.websites import open_website
from skills.player import play_music


# ===================== COMMAND HANDLER =====================

def handle_command(command):

    # Clean command
    command = command.lower().strip()
    command = command.strip(string.punctuation + " ")

    print(f"Executing command: {command}")

    # ================= OPEN =================

    if command.startswith("open "):

        item = command.replace("open", "", 1).strip()

        # ---------- Applications ----------

        if open_app(item):
            return

        # ---------- Folders ----------

        if open_folder(item):
            return

        # ---------- Websites ----------

        if open_website(item):
            return

        speak("I don't know how to open that.")
        return

    # ================= MUSIC =================

    elif play_music(command):
        return

    # ================= TIME =================

    elif "time" in command:

        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
        return

    # ================= IDENTITY =================

    elif "your name" in command:

        speak("My name is Orion.")
        return

    # ================= STOP =================

    elif command in ["stop", "exit", "quit"]:

        speak("Goodbye")
        return "stop"

    # ================= UNKNOWN =================

    else:
        speak("Sorry, I don't know that command yet.")

    return None