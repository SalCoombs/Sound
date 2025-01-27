import numpy as np
from output import output, plot
from form import sin, time

C = 261.63/2
BPM = 120

def run():
    t1 = time(6)
    quarter = beat_duration(BPM)


    worble = sin(t1, 7, 0.5) + 0.5
    output(sin(t1, C, worble))
