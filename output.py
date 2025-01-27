import pyaudio
import numpy as np
from constants import FORMAT, CHANNELS, RATE, CHUNK, VOLUME
import matplotlib.pyplot as plt


def output(audio):
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True,
                    frames_per_buffer=CHUNK)

    # Normalize audio and avoid division by zero
    max_val = np.max(np.abs(audio))
    if max_val == 0:
        print("Error: Audio data is silent (all zeros).")
        return

    nice_audio = audio / max_val * VOLUME

    data = nice_audio.astype(np.float32).tobytes()
    stream.write(data)

    print("*done playing")

    stream.stop_stream()
    stream.close()
    p.terminate()


def plot(audio):
    plt.figure(figsize=(10, 4))
    duration = audio.size/RATE
    t = np.linspace(0, duration, audio.size, endpoint=False)
    plt.plot(t, audio, label="Audio Signal")
    plt.title("Audio Signal Waveform")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()