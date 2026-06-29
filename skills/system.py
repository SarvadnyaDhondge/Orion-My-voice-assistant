"""
system.py

This module handles system-related voice commands.

Responsibilities
----------------
- Understand system commands.
- Ask system_service.py for information.
- Speak the result.

This module does NOT directly communicate with the operating system.
"""

from speak import speak
from services.system_service import (
    get_battery_status,
    get_cpu_usage,
    get_ram_usage,
    get_disk_usage,
)

BATTERY_COMMANDS = [
    "battery",
    "battery status",
    "battery percentage",
    "how much battery",
    "how much battery is left",
    "how much charge is left",
    "battery level",
]

CPU_COMMANDS = [
    "cpu",
    "cpu usage",
    "processor",
    "processor usage",
    "processor percentage"
]

RAM_COMMANDS = [
    "ram",
    "ram usage",
    "memory",
    "memory usage"
]

DISK_COMMANDS = [
    "disk",
    "disk usage",
    "storage",
    "storage usage",
    "drive usage"
]


def handle_system(command):
    """
    Handle system-related commands.

    Returns
    -------
    bool
        True  -> Command handled.
        False -> Not a system command.
    """

    command = command.lower().strip()

    if command in BATTERY_COMMANDS:
        battery = get_battery_status()

        if battery is None:
            speak("This computer does not have a battery.")
            return True

        status = "charging" if battery["charging"] else "not charging"

        speak(
            f"The battery is {battery['percent']} percent and is currently {status}."
        )

        return True

    if command in CPU_COMMANDS:
        cpu = get_cpu_usage()
        speak(
            f"The CPU usage is {cpu['percent']} percent. "
        )
        return True

    if command in RAM_COMMANDS:
        ram = get_ram_usage()
        speak(
            f"The RAM usage is {ram['percent']} percent. "
            f"You are using {ram['used_gb']} gigabytes "
            f"out of {ram['total_gb']} gigabytes."
        )
        return True

    if command in DISK_COMMANDS:
        disk = get_disk_usage()
        speak(
        f"The C drive is {disk['percent']} percent full. "
        f"You are using {disk['used_gb']} gigabytes "
        f"out of {disk['total_gb']} gigabytes."
        )
        return True

    return False