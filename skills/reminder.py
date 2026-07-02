"""
reminder.py

This module handles reminder-related voice commands.

Responsibilities
----------------
- Understand reminder commands.
- Extract reminder text.
- Ask reminder_service.py to save, load, or delete reminders.
- Speak the result.

This module does NOT store reminders itself.
"""

from speak import speak
from services.reminder_service import (
    add_reminder,
    delete_reminder,
    load_reminders,
)


ADD_REMINDER_PREFIX = "remind me"
DELETE_REMINDER_PREFIX = "delete reminder"

SHOW_REMINDER_COMMANDS = [
    "show my reminders",
    "show reminders",
    "what are my reminders",
    "list reminders",
]


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

    # SHOW REMINDERS
    if command in SHOW_REMINDER_COMMANDS:

        reminders = load_reminders()

        if not reminders:
            speak("You don't have any reminders.")
            return True

        speak(f"You have {len(reminders)} reminders.")

        for index, reminder in enumerate(reminders, start=1):
            speak(f"Reminder {index}: {reminder['task']}")

        return True

    # DELETE REMINDER
    if command.startswith(DELETE_REMINDER_PREFIX):

        try:
            reminder_number = int(
                command.replace(DELETE_REMINDER_PREFIX, "", 1).strip()
            )

        except ValueError:
            speak("Please tell me the reminder number to delete.")
            return True

        deleted = delete_reminder(reminder_number)

        if deleted is None:
            speak("I couldn't find that reminder.")
            return True

        speak(
            f"Deleted reminder {reminder_number}: {deleted['task']}"
        )

        return True

    # ADD REMINDER
    if not command.startswith(ADD_REMINDER_PREFIX):
        return False

    task = command.replace(ADD_REMINDER_PREFIX, "", 1).strip()

    if task.startswith("to "):
        task = task[3:].strip()

    if not task:
        speak("What should I remind you about?")
        return True

    add_reminder(task)

    speak(f"Reminder saved: {task}")

    return True