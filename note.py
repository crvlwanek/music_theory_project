from constants import *


class Note:

    def __init__(self, pitch, enharmonic):
        self.pitch = pitch
        self.enharmonic = enharmonic
        for name, info in NOTES.items():
            if info == (self.pitch, self.enharmonic):
                self.name = name
        try:
            self.name
        except AttributeError:
            raise ValueError("Note not found")
        self.in_scale = self.in_chord = self.in_key = False
        if self.in_key:
            pass

    def is_same(self, note2):
        if self.name == note2.name:
            return True
        else:
            return False

    def adjust_chromatic(self, half_steps, enharmonic=None):
        pitch = self.pitch
        if enharmonic is None:
            enharmonic = self.enharmonic
        pitch += half_steps
        if pitch >= TET:
            pitch = pitch % TET
        return Note(pitch, enharmonic)

    def add_fifth(self):
        return self.adjust_chromatic(7)


def adjust_chromatic(pitch, half_steps):
    pitch += half_steps
    if pitch >= 12:
        pitch = pitch % 12
    return pitch


def add_fifth(pitch):
    return adjust_chromatic(pitch, 7)


def circle_fifth(step):
    step += 4
    if step > 6:
        step = step % 7
    return step


def circle_fourth(step):
    step += 3
    if step > 6:
        step = step % 7
    return step


def get_accidentals(total_accidentals, adjust_accidental, scale_len):
    accidentals = [0] * scale_len
    if total_accidentals == 0:
        return accidentals
    if total_accidentals > 0:
        step = 3
    if total_accidentals < 0:
        step = 3
    for i in range(abs(total_accidentals)):
        if total_accidentals > 0:
            step = circle_fourth(step)
        if total_accidentals < 0:
            step = circle_fourth(step)
        accidentals[step] += adjust_accidental
    return accidentals

