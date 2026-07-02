"""
mic_calibration.py

Measure your microphone's background noise level.

Use the reported value to help choose an appropriate
SILENCE_THRESHOLD for speech.py.
"""

import numpy as np
import sounddevice as sd

SAMPLE_RATE = 16000
DURATION = 5  # seconds


def main():
    print("Microphone Calibration")
    print("-" * 30)
    print(f"Recording {DURATION} seconds of background noise...")
    print("Please remain as quiet as possible.\n")

    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32",
    )

    sd.wait()

    audio = audio.reshape(-1)

    average_level = np.abs(audio).mean()
    peak_level = np.abs(audio).max()

    print(f"Average noise level : {average_level:.5f}")
    print(f"Peak noise level    : {peak_level:.5f}")

    recommended = round(average_level * 2.5, 3)

    print("\nSuggested SILENCE_THRESHOLD:")
    print(recommended)


if __name__ == "__main__":
    main()