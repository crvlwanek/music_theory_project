from constants.enharmonic import *
from constants.pitch import *

# Defining each note by its pitch and enharmonic values
CHROMATIC = {"B#": (PITCHES[0], SHARP), "C": (PITCHES[0], NATURAL), "Dbb": (PITCHES[0], DBFLAT),
             "C#": (PITCHES[1], SHARP), "Db": (PITCHES[1], FLAT),
             "C##": (PITCHES[2], DBSHARP), "D": (PITCHES[2], NATURAL), "Ebb": (PITCHES[2], DBFLAT),
             "D#": (PITCHES[3], SHARP), "Eb": (PITCHES[3], FLAT),
             "E": (PITCHES[4], NATURAL), "Fb": (PITCHES[4], FLAT),
             "E#": (PITCHES[5], SHARP), "F": (PITCHES[5], NATURAL),
             "F#": (PITCHES[6], SHARP), "Gb": (PITCHES[6], FLAT),
             "F##": (PITCHES[7], DBSHARP), "G": (PITCHES[7], NATURAL), "Abb": (PITCHES[7], DBFLAT),
             "G#": (PITCHES[8], SHARP), "Ab": (PITCHES[8], FLAT),
             "G##": (PITCHES[9], DBSHARP), "A": (PITCHES[9], NATURAL), "Bbb": (PITCHES[9], DBFLAT),
             "A#": (PITCHES[10], SHARP), "Bb": (PITCHES[10], FLAT),
             "B": (PITCHES[11], NATURAL), "Cb": (PITCHES[11], FLAT)}


class Note:

    def __init__(self, pitch, enharmonic):
        try:
            self.pitch = PITCHES[pitch]
        except:
            raise ValueError(f"Pitch <{pitch}> not found")
        for sign, value in ENHARMONICS.items():
            if value[0] == enharmonic:
                self.enharmonic = value[1]
        try:
            self.enharmonic
        except AttributeError:
            raise ValueError(f"Enharmonic <{enharmonic}> not found")
        for name, value in CHROMATIC.items():
            if value == (self.pitch, self.enharmonic):
                self.name = name
        try:
            self.name
        except AttributeError:
            raise ValueError(f"Note ({self.pitch}, {self.enharmonic}) not found")
        self.in_scale = self.in_chord = self.in_key = False
        if self.in_key:
            pass

    def __str__(self):
        return f"<{self.name}>"

    def is_same(self, note2):
        if self.name == note2.name:
            return True
        else:
            return False


# Syntax: {name: Note}
NOTES = {name: Note(value[0].index, value[1].quantifier) for name, value in CHROMATIC.items()}


def constrain_chromatic(index):
    if index >= TET:
        index %= TET
        constrain_chromatic(index)
    if index < 0:
        index += TET
        constrain_chromatic(index)
    else:
        return index


def pick_note(name):
    return NOTES[name]


def find_note(index, quantifier):
    for name, values in CHROMATIC.items():
        if (find_pitch(index), find_enharmonic(quantifier)) == values:
            return pick_note(name)


def adjust_note(note, half_steps, quantifier=None):
    if quantifier is None:
        quantifier = note.enharmonic.quantifier
    return find_note((note.pitch.index + half_steps), quantifier)


def add_fifth(note, quantifier=None):
    return adjust_note(note, 7, quantifier)
