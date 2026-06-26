import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel
import queue
import time

SAMPLE_RATE = 16000
BLOCK_SIZE = 1024

model = WhisperModel("base", device="cpu", compute_type="int8")

audio_queue = queue.Queue()


def callback(indata, frames, t, status):
    audio_queue.put(indata.copy())


def listen():
    print("Listening...")

    min_record_time = 2.5
    record_start = None

    silence_threshold = 0.02
    silence_limit = 0.7
    silence_chunks = int((silence_limit * SAMPLE_RATE) / BLOCK_SIZE)

    audio_buffer = []
    silent_counter = 0

    # 🔥 CLEAR OLD QUEUE (VERY IMPORTANT FIX)
    while not audio_queue.empty():
        audio_queue.get()

    with sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32",
        blocksize=BLOCK_SIZE,
        callback=callback
    ):

        while True:
            chunk = audio_queue.get()

            if record_start is None:
                record_start = time.time()

            audio_buffer.append(chunk)

            volume = np.abs(chunk).mean()

            if volume < silence_threshold:
                silent_counter += 1
            else:
                silent_counter = 0

            elapsed = time.time() - record_start

            if elapsed > min_record_time and silent_counter > silence_chunks:
                break

    # 🔥 SAFETY CHECK
    if len(audio_buffer) < 5:
        print("Too short audio, ignoring...")
        return ""

    audio = np.concatenate(audio_buffer, axis=0).reshape(-1)

    # 🔥 NORMALIZATION (CRITICAL FOR ACCURACY)
    audio = audio / (np.max(np.abs(audio)) + 1e-6)

    print("Processing...")

    segments, _ = model.transcribe(
        audio,
        language="en",
        beam_size=5,
        vad_filter=True
    )

    text = " ".join(s.text for s in segments).strip().lower()

    print("You said:", text)

    return text