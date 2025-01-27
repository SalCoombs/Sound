import numpy as np
from constants import RATE


def sin(time_arr, frequency, volume=1):
    return np.sin(time_arr * 2 * np.pi * frequency) * volume


def time(duration):
    return np.linspace(0, duration, duration*RATE)

def beat_duration(bpm):
    return time(bpm / 60)