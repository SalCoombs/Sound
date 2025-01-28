from form import time



def beat_duration(bpm):
    return time(bpm / 60)

class NoteDuration:
    quarter = beat_duration(BPM)
    half = beat_duration(BPM*2)
    whole = beat_duration(BPM*4)
    eighth = beat_duration(BPM/2)

class Song:
    def __init__(self, BPM, melody):
        self.BPM = BPM
        self.melody = melody

class NOTES:
    C = 261.63
    Db = 277.18
    D = 293.18
    Eb = 311.13
    E = 329.63
    F = 349.23
    Gb = 369.99
    G = 390.22
    Ab = 415.30
    A = 440
    Bb = 466.16
    B = 493.88