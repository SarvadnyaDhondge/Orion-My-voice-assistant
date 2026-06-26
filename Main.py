from speak import speak
from speech import listen
from commands import handle_command
import time

WAKE_WORD = "come back"  # Set your desired wake word here

speak("Initializing Comeback")


def clean_text(text):
    if not text:
        return ""

    text = text.lower()
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.strip()

    return text


while True:

    print("Waiting for wake word...")

    text = listen()
    text = clean_text(text)

    if not text:
        continue

    print("Heard:", text)

    # 🔥 CASE 1 & CASE 2 HANDLING
    if WAKE_WORD in text:

        # remove wake word
        command = text.replace(WAKE_WORD, "").strip()

        # CASE 2: wake word + command together
        if command:
            print("Direct command:", command)
            result = handle_command(command)

        # CASE 1: only wake word
        else:
            speak("Yes?")
            command = listen()
            command = clean_text(command)

            if command:
                print("Command:", command)
                result = handle_command(command)

    else:
        continue

    if result == "stop":
        speak("Goodbye")
        break

    time.sleep(0.2)