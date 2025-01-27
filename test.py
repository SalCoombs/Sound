import numpy as np
from output import output, plot
from form import sin, time

C = 261.63/2

def run():
    t1 = time(6)

    worble = sin(t1, 7, 0.5) + 0.5
    output(sin(t1, C, worble))
