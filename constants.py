import pyaudio

CHUNK = 1024  # measured in bytes
FORMAT = pyaudio.paFloat32
CHANNELS = 2  # stereo
RATE = 44100  # common sampling frequency
VOLUME = 0.3
