import os
import webbrowser
import subprocess
import string
from datetime import datetime

from speak import speak
from music import play_song


# ===================== APPS =====================

APPS = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "calculator": "calc.exe",
    "calc": "calc.exe",
    "notepad": "notepad.exe",
    "vs code": "code",
    "vscode": "code",
}


# ===================== FOLDERS =====================

FOLDERS = {
    "desktop": os.path.join(os.path.expanduser("~"), "Desktop"),
    "documents": os.path.join(os.path.expanduser("~"), "Documents"),
    "downloads": os.path.join(os.path.expanduser("~"), "Downloads"),
    "pictures": os.path.join(os.path.expanduser("~"), "Pictures"),
    "music": os.path.join(os.path.expanduser("~"), "Music"),
    "videos": os.path.join(os.path.expanduser("~"), "Videos"),
}


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

        if item in APPS:
            try:
                subprocess.Popen(APPS[item])
                speak(f"Opening {item}")
                return
            except Exception as e:
                print(e)
                speak("Sorry, I couldn't open that application.")
                return

        # ---------- Folders ----------

        elif item in FOLDERS:
            try:
                subprocess.Popen(f'explorer "{FOLDERS[item]}"')
                speak(f"Opening {item}")
                return
            except Exception as e:
                print(e)
                speak("Sorry, I couldn't open that folder.")
                return

        # ---------- Websites ----------

        elif item == "google":
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
            return

        elif item == "youtube":
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
            return

        elif item == "github":
            speak("Opening GitHub")
            webbrowser.open("https://github.com")
            return

        else:
            speak("I don't know how to open that.")
            return

    # ================= MUSIC =================

    elif command.startswith("play "):

        song = command.replace("play", "", 1).strip()
        song = song.strip(string.punctuation + " ")

        speak(f"Playing {song}")

        success = play_song(song)

        if not success:
            speak("Sorry, I couldn't find that song.")

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