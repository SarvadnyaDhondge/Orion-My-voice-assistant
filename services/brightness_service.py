"""
brightness_service.py

This module provides access to screen brightness.

Responsibilities
----------------
- Read current brightness.
- Increase brightness.
- Decrease brightness.
- Set brightness.

This module does NOT:
- Speak
- Listen
- Understand commands

Those responsibilities belong to skills/brightness.py.
"""

import screen_brightness_control as sbc


DISPLAY_INDEX = 0
MAX_BRIGHTNESS = 100


def get_brightness():
    """
    Get the current screen brightness.

    Returns
    -------
    dict | None
        Example:
        {
            "percent": 75
        }

        Returns None if the brightness cannot be read.
    """

    try:
        brightness = sbc.get_brightness(display=DISPLAY_INDEX)[0]

        return {
            "percent": brightness
        }

    except Exception:
        return None


def set_brightness(percent):
    """
    Set the screen brightness.

    Parameters
    ----------
    percent : int
        Brightness level (0-100).

    Returns
    -------
    dict | None
        Example:
        {
            "percent": 80
        }

        Returns None if the brightness could not be changed.
    """

    percent = max(0, min(MAX_BRIGHTNESS, percent))

    try:
        sbc.set_brightness(percent, display=DISPLAY_INDEX)

        return {
            "percent": percent
        }

    except Exception:
        return None


def brightness_up(step=10):
    """
    Increase the screen brightness.

    Parameters
    ----------
    step : int, optional
        Amount to increase brightness.

    Returns
    -------
    dict | None
        Updated brightness information.
    """

    current = get_brightness()

    if current is None:
        return None

    new_brightness = current["percent"] + step

    return set_brightness(new_brightness)


def brightness_down(step=10):
    """
    Decrease the screen brightness.

    Parameters
    ----------
    step : int, optional
        Amount to decrease brightness.

    Returns
    -------
    dict | None
        Updated brightness information.
    """

    current = get_brightness()

    if current is None:
        return None

    new_brightness = current["percent"] - step

    return set_brightness(new_brightness)