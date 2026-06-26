import webbrowser
from yt_dlp import YoutubeDL


def play_song(song_name):
    try:
        ydl_opts = {
            "quiet": True,
            "extract_flat": True,
        }

        with YoutubeDL(ydl_opts) as ydl:
            results = ydl.extract_info(
                f"ytsearch1:{song_name}",
                download=False
            )

            if results and "entries" in results:
                video = results["entries"][0]

                print("Found:", video["title"])

                url = f"https://www.youtube.com/watch?v={video['id']}"
                webbrowser.open(url)

                return True

    except Exception as e:
        print("Music Error:", e)

    return False