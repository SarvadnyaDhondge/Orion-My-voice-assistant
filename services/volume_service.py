"""
volume_service.py

This module provides access to volume information.

Responsibilities
----------------
- Read current volume level.
- Read mute status.

This module does NOT:
- Speak
- Listen
- Understand commands

Those responsibilities belong to skills/volume.py.
"""

from pycaw.pycaw import AudioUtilities


MAX_VOLUME = 100


def _get_volume_interface():
    """
    Return the Windows master volume interface.
    """

    device = AudioUtilities.GetSpeakers()
    return device.EndpointVolume


def get_volume():
    """
    Get the current system volume level and mute status.

    Returns
    -------
    dict
        Example:
        {
            "percent": 50,
            "muted": False
        }
    """

    volume = _get_volume_interface()

    return {
        "percent": round(volume.GetMasterVolumeLevelScalar() * MAX_VOLUME),
        "muted": bool(volume.GetMute()),
    }


def set_volume(percent):
    """
    Set the system volume level.

    Parameters
    ----------
    percent : int
        Volume level (0-100).

    Returns
    -------
    dict
        Example:
        {
            "percent": 75
        }
    """

    percent = max(0, min(MAX_VOLUME, percent))

    volume = _get_volume_interface()
    volume.SetMasterVolumeLevelScalar(percent / MAX_VOLUME, None)

    return {
        "percent": percent
    }


def volume_up(step=10):
    """
    Increase the system volume.

    Parameters
    ----------
    step : int
        Amount to increase the volume.

    Returns
    -------
    dict
        Updated volume level.
    """

    current = get_volume()
    new_volume = min(MAX_VOLUME, current["percent"] + step)

    return set_volume(new_volume)


def volume_down(step=10):
    """
    Decrease the system volume.

    Parameters
    ----------
    step : int
        Amount to decrease the volume.

    Returns
    -------
    dict
        Updated volume level.
    """

    current = get_volume()
    new_volume = max(0, current["percent"] - step)

    return set_volume(new_volume)


def mute_volume():
    """
    Mute the system volume.

    Returns
    -------
    dict
        Example:
        {
            "muted": True
        }
    """

    volume = _get_volume_interface()
    volume.SetMute(True, None)

    return {
        "muted": True
    }


def unmute_volume():
    """
    Unmute the system volume.

    Returns
    -------
    dict
        Example:
        {
            "muted": False
        }
    """

    volume = _get_volume_interface()
    volume.SetMute(False, None)

    return {
        "muted": False
    }