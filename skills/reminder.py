"""
reminder.py

This module handles reminder-related voice commands.

Responsibilities
----------------
- Understand reminder commands.
- Extract the reminder text.
- Ask reminder_service.py to save it.
- Speak the result.

This module does NOT store reminders itself.
"""

from speak import speak
from services.reminder_service import (
    add_reminder,
    load_reminders,
    delete_reminder,
)


def handle_reminder(command):
    """
    Handle reminder commands.

    Returns
    -------
    bool
        True  -> Reminder command handled.
        False -> Not a reminder command.
    """

    command = command.lower().strip()

    # ---------------- Show reminders ----------------

    if command in [
        "show my reminders",
        "show reminders",
        "what are my reminders",
        "list reminders",
    ]:
        reminders = load_reminders()

        if not reminders:
            speak("You don't have any reminders.")
            return True

        speak(f"You have {len(reminders)} reminders.")

        for index, reminder in enumerate(reminders, start=1):
            speak(f"Reminder {index}: {reminder['task']}")

        return True


    # ---------------- Delete reminder ----------------

    if command.startswith("delete reminder"):

        try:
            number = int(command.replace("delete reminder", "", 1).strip())
        except ValueError:
            speak("Please tell me the reminder number to delete.")
            return True

        deleted = delete_reminder(number)

        if deleted is None:
            speak("I couldn't find that reminder.")
            return True

        speak(f"Deleted reminder {number}: {deleted['task']}")
        return True
        

    # Check if the command starts with "remind me"
    if not command.startswith("remind me"):
        return False

    # Remove "remind me"
    task = command.replace("remind me", "", 1).strip()

    # Remove optional "to"
    if task.startswith("to "):
        task = task[3:].strip()

    # Make sure the reminder isn't empty
    if not task:
        speak("What should I remind you about?")
        return True

    # Save the reminder
    add_reminder(task)

    speak(f"Reminder saved: {task}")

    return True