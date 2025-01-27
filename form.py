import numpy as np
from constants import RATE


def sin(time_arr, frequency, amplitude=1):
    return np.sin(time_arr * 2 * np.pi * frequency) * amplitude


def time(duration):
    return np.linspace(0, duration, duration*RATE)


def add_at_pos(target, source, pos):
    end = pos + len(source)
    target[pos:end] += source[:max(0, len(target) - pos)]


def add_at_time(target, source, time, time_arr):
    positions = np.where(time_arr == time)
    for position in positions:
        add_at_pos(target, source, position)