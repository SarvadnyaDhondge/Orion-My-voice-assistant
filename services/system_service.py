"""
system_service.py

This module provides access to system information.

Responsibilities
----------------
- Read battery information.
- Read CPU usage.
- Read RAM usage.
- Read disk usage.
- Check internet connectivity.

This module does NOT:
- Speak
- Listen
- Understand commands

Those responsibilities belong to skills/system.py.
"""

import socket

import psutil


BYTES_PER_GB = 1024 ** 3
SYSTEM_DRIVE = "C:\\"


def get_battery_status():
    """
    Get the current battery status.

    Returns
    -------
    dict | None
        Example:
        {
            "percent": 85,
            "charging": True
        }

        Returns None if the system has no battery.
    """

    battery = psutil.sensors_battery()

    if battery is None:
        return None

    return {
        "percent": round(battery.percent),
        "charging": battery.power_plugged,
    }


def get_cpu_usage():
    """
    Get the current CPU usage percentage.

    Returns
    -------
    dict
        Example:
        {
            "percent": 45
        }
    """

    cpu_usage = psutil.cpu_percent(interval=1)

    return {
        "percent": round(cpu_usage)
    }


def get_ram_usage():
    """
    Get the current RAM usage.

    Returns
    -------
    dict
        Example:
        {
            "percent": 70,
            "used_gb": 8.5,
            "total_gb": 16,
            "available_gb": 7.5
        }
    """

    ram = psutil.virtual_memory()

    return {
        "percent": round(ram.percent),
        "used_gb": round(ram.used / BYTES_PER_GB, 2),
        "total_gb": round(ram.total / BYTES_PER_GB, 2),
        "available_gb": round(ram.available / BYTES_PER_GB, 2),
    }


def get_disk_usage():
    """
    Get the current disk usage.

    Returns
    -------
    dict
        Example:
        {
            "percent": 60,
            "used_gb": 300,
            "total_gb": 500,
            "free_gb": 200
        }
    """

    disk = psutil.disk_usage(SYSTEM_DRIVE)

    return {
        "percent": round(disk.percent),
        "used_gb": round(disk.used / BYTES_PER_GB, 2),
        "total_gb": round(disk.total / BYTES_PER_GB, 2),
        "free_gb": round(disk.free / BYTES_PER_GB, 2),
    }


def get_internet_status():
    """
    Check whether the computer has an active internet connection.

    Returns
    -------
    bool
        True  -> Internet is available.
        False -> No internet connection.
    """

    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True

    except OSError:
        return False