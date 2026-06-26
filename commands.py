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


# ===================== COMMAND HANDLER =====================

def handle_command(command):

    # Clean command
    command = command.lower().strip()
    command = command.strip(string.punctuation + " ")

    print(f"Executing command: {command}")

    # ================= OPEN APPLICATIONS =================

    if command.startswith("open "):

        app_name = command.replace("open", "", 1).strip()

        if app_name in APPS:
            try:
                subprocess.Popen(APPS[app_name])
                speak(f"Opening {app_name}")
                return
            except Exception as e:
                print(e)
                speak("Sorry, I couldn't open that application.")
                return

        # Open websites
        elif app_name == "google":
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
            return

        elif app_name == "youtube":
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
            return

        elif app_name == "github":
            speak("Opening GitHub")
            webbrowser.open("https://github.com")
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

        speak("My name is Comeback.")
        return

    # ================= STOP =================

    elif command in ["stop", "exit", "quit"]:

        speak("Goodbye")
        return "stop"

    # ================= UNKNOWN =================

    speak("Sorry, I don't know that command yet.")
    return None