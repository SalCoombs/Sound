import numpy as np
from output import output, plot
from form import sin, time, beat_duration
from constants import NOTES, BPM

def run():
    t1 = time(6)
    
    worble = sin(t1, 1, 0.5) + 0.5
    output(sin(t1, NOTES.C+worble, worble))
    output(sin(2, NOTES.C, worble))
