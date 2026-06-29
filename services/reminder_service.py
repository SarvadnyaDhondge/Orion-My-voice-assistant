"""
reminder_service.py

This module manages reminder storage.

Responsibilities
----------------
- Load reminders from reminders.json
- Save reminders to reminders.json
- Add new reminders

This module does NOT:
- Speak
- Listen
- Understand voice commands

Those responsibilities belong to reminder.py.
"""

import json
from pathlib import Path


# Path to the reminders file
DATA_FILE = Path("data/reminders.json")


def load_reminders():
    """
    Load all reminders from the JSON file.

    Returns
    -------
    list
        A list of reminder dictionaries.
    """

    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_reminders(reminders):
    """
    Save the reminder list to the JSON file.
    """

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(reminders, file, indent=4)


def add_reminder(task):
    """
    Add a new reminder.

    Parameters
    ----------
    task : str
        The reminder text.
    """

    reminders = load_reminders()

    reminder = {
        "task": task,
        "completed": False
    }

    reminders.append(reminder)

    save_reminders(reminders)

    return reminder


def delete_reminder(index):
    """
    Delete a reminder by its index.

    Parameters
    ----------
    index : int
        Reminder number (starting from 1).

    Returns
    -------
    dict | None
        The deleted reminder if successful, otherwise None.
    """

    reminders = load_reminders()

    # Convert from 1-based to 0-based indexing
    index -= 1

    if index < 0 or index >= len(reminders):
        return None

    deleted = reminders.pop(index)

    save_reminders(reminders)

    return deleted