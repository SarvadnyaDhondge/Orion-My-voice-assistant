"""
music.py

This module searches YouTube for a song
and opens the first result in the default browser.
"""

import webbrowser

from yt_dlp import YoutubeDL


YDL_OPTIONS = {
    "quiet": True,
    "extract_flat": True,
}


def play_song(song_name):
    """
    Search YouTube and play the first matching song.

    Parameters
    ----------
    song_name : str

    Returns
    -------
    bool
        True  -> Song found.
        False -> Song not found.
    """

    try:

        with YoutubeDL(YDL_OPTIONS) as ydl:

            results = ydl.extract_info(
                f"ytsearch1:{song_name}",
                download=False,
            )

        entries = results.get("entries")

        if not entries:
            return False

        video = entries[0]

        print(f"Found: {video['title']}")

        video_id = video["id"]

        url = f"https://www.youtube.com/watch?v={video_id}"

        webbrowser.open(url)

        return True

    except Exception as e:

        print(f"Music Error: {e}")

        return False