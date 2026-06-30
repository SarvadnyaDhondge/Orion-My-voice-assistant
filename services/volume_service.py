'''
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
'''

from pycaw.pycaw import AudioUtilities

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
        {
            "percent": 50,
            "muted": False
        }
    """

    volume = _get_volume_interface()
    level = volume.GetMasterVolumeLevelScalar()
    muted = volume.GetMute()

    return {
        "percent": round(level * 100),
        "muted": bool(muted)
    }

def set_volume(percent):
    """
    Set the system volume level.

    Parameters
    ----------
    percent : int
        Volume level (0-100)

    Returns
    -------
    dict
        Updated volume level
    """

    percent = max(0, min(100, percent))

    volume = _get_volume_interface()
    volume.SetMasterVolumeLevelScalar(percent / 100.0, None)

    return {
            "percent": percent
        }

def volume_up(step=10):
    '''
    Increase the volume level.

    Parameters
    ----------
    step : int
        Amount to increase the volume by (default is 10).
    '''
    current_volume = get_volume()
    new_volume = min(100, current_volume["percent"] + step)
    set_volume(new_volume)

    return {
        "percent": new_volume
    }

def volume_down(step=10):
    '''
    Decrease the volume level.

    Parameters
    ----------
    step : int
        Amount to decrease the volume by (default is 10).
    '''
    current_volume = get_volume()
    new_volume = max(0, current_volume["percent"] - step)
    set_volume(new_volume)

    return {
        "percent": new_volume
    }

def mute_volume():
    '''
    Mute the volume.
    '''
    volume = _get_volume_interface()
    volume.SetMute(True, None)

    return {
        "muted": True
    }

def unmute_volume():
    '''
    Unmute the volume.
    '''
    volume = _get_volume_interface()
    volume.SetMute(False, None)

    return {
        "muted": False
    }