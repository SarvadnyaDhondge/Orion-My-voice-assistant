import sounddevice as sd
import numpy as np

SAMPLE_RATE = 16000

print("Measuring microphone noise...")
print("Please stay quiet for 5 seconds.")

audio = sd.rec(
    int(5 * SAMPLE_RATE),
    samplerate=SAMPLE_RATE,
    channels=1,
    dtype="int16"
)

sd.wait()

volume = np.abs(audio).mean()

print("Average microphone level:", volume)