"""
speech.py

Handles microphone recording and speech-to-text.

Responsibilities
----------------
- Record microphone audio.
- Detect silence.
- Transcribe speech using Faster-Whisper.

This module does NOT:
- Speak
- Understand commands
- Execute commands
"""

import queue
import time

import numpy as np
import sounddevice as sd
from faster_whisper import WhisperModel


# ================= CONFIGURATION =================

SAMPLE_RATE = 16000
BLOCK_SIZE = 1024

MIN_RECORD_TIME = 2.5
SILENCE_THRESHOLD = 0.02
SILENCE_LIMIT = 0.7

SILENCE_CHUNKS = int(
    (SILENCE_LIMIT * SAMPLE_RATE) / BLOCK_SIZE
)

# ================= WHISPER MODEL =================

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8",
)

# ================= AUDIO QUEUE =================

audio_queue = queue.Queue()


def callback(indata, frames, time_info, status):
    """
    Audio callback used by sounddevice.
    """

    if status:
        print(status)

    audio_queue.put(indata.copy())


def clear_audio_queue():
    """
    Remove any old audio remaining in the queue.
    """

    while not audio_queue.empty():
        audio_queue.get_nowait()


def listen() -> str:
    """
    Listen to the microphone until silence is detected.

    Returns
    -------
    str
        Recognized speech.
    """

    print("Listening...")

    clear_audio_queue()

    record_start = None
    silent_counter = 0
    audio_buffer = []

    with sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32",
        blocksize=BLOCK_SIZE,
        callback=callback,
    ):

        while True:

            chunk = audio_queue.get()

            if record_start is None:
                record_start = time.time()

            audio_buffer.append(chunk)

            volume = np.abs(chunk).mean()

            if volume < SILENCE_THRESHOLD:
                silent_counter += 1
            else:
                silent_counter = 0

            elapsed = time.time() - record_start

            if (
                elapsed >= MIN_RECORD_TIME
                and silent_counter >= SILENCE_CHUNKS
            ):
                break

    if len(audio_buffer) < 5:
        print("Too little audio captured.")
        return ""

    audio = np.concatenate(audio_buffer, axis=0).reshape(-1)

    peak = np.max(np.abs(audio))

    if peak > 0:
        audio /= peak

    print("Processing...")

    try:

        segments, _ = model.transcribe(
            audio,
            language="en",
            beam_size=5,
            vad_filter=True,
        )

    except Exception as e:

        print(f"Speech Error: {e}")
        return ""

    text = " ".join(segment.text for segment in segments)

    text = text.strip().lower()

    print(f"You said: {text}")

    return text