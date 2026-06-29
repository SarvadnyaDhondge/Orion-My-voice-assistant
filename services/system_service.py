"""
system_service.py

This module provides access to system information.

Responsibilities
----------------
- Read battery information.
- Read CPU usage.
- Read RAM usage.
- Read disk usage.

This module does NOT:
- Speak
- Listen
- Understand commands

Those responsibilities belong to skills/system.py.
"""

import psutil


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
        "charging": battery.power_plugged
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
        CPU usage percentage.
    """

    cpu_usage = psutil.cpu_percent(interval=1)

    return {
        "percent": round(cpu_usage)
    }

def get_ram_usage():
    """
    Get the current RAM usage percentage.

    Returns
    -------
    dict
        Example:
        {
            "percent": 70,
            "used": 8.5,
            "total": 16,
            "available": 7.5
        }
        RAM usage percentage.
    """
    ram = psutil.virtual_memory()

    return {
        "percent": round(ram.percent),
        "used_gb": round(ram.used / (1024 ** 3), 2),
        "total_gb": round(ram.total / (1024 ** 3), 2),
        "available_gb": round(ram.available / (1024 ** 3), 2)
    }

def get_disk_usage():
    """
    Get the current disk usage percentage.

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
        Disk usage percentage.
    """

    disk = psutil.disk_usage("C:\\")

    return {
        "percent": round(disk.percent),
        "used_gb": round(disk.used / (1024 ** 3), 2),
        "total_gb": round(disk.total / (1024 ** 3), 2),
        "free_gb": round(disk.free / (1024 ** 3), 2)
    }