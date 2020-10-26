from setup.constants.enharmonic import *
from setup.constants.pitch import *

"""
All standard pitch classes are defined and should be called with either:
   - pick_pitch_class(name)
   - find_pitch_class(index, quantifier)
"""

# Defining each pitch class by its pitch and enharmonic values
CHROMATIC = {"B#": (Pitch(0), SHARP), "C": (Pitch(0), NATURAL), "Dbb": (Pitch(0), DBFLAT),
             "C#": (Pitch(1), SHARP), "Db": (Pitch(1), FLAT),
             "C##": (Pitch(2), DBSHARP), "D": (Pitch(2), NATURAL), "Ebb": (Pitch(2), DBFLAT),
             "D#": (Pitch(3), SHARP), "Eb": (Pitch(3), FLAT),
             "E": (Pitch(4), NATURAL), "Fb": (Pitch(4), FLAT),
             "E#": (Pitch(5), SHARP), "F": (Pitch(5), NATURAL),
             "F#": (Pitch(6), SHARP), "Gb": (Pitch(6), FLAT),
             "F##": (Pitch(7), DBSHARP), "G": (Pitch(7), NATURAL), "Abb": (Pitch(7), DBFLAT),
             "G#": (Pitch(8), SHARP), "Ab": (Pitch(8), FLAT),
             "G##": (Pitch(9), DBSHARP), "A": (Pitch(9), NATURAL), "Bbb": (Pitch(9), DBFLAT),
             "A#": (Pitch(10), SHARP), "Bb": (Pitch(10), FLAT),
             "B": (Pitch(11), NATURAL), "Cb": (Pitch(11), FLAT)}


class PitchClass:
    # name --> str
    def __init__(self, name):
        # Set-up ----------------------------------------------------
        if name not in CHROMATIC:
            raise ValueError(f"Pitch Class {name} not found")
        self.name = name
        self.pitch = CHROMATIC[self.name][0]
        self.enharmonic = CHROMATIC[self.name][1]
        self.in_scale = self.in_chord = self.in_key = False
        if self.in_key:
            pass

    def __repr__(self):
        return f"{self.__class__.__name__} object: {self.name}"

    def __eq__(self, other):
        if other.__class__ != self.__class__:
            raise ValueError(f"Operand not supported for types: \'{other.__class__}\' and \'{self.__class__}\'")
        return self.name == other.name

        # -----------------------------------------------------------


# Syntax: PITCH_CLASSES = {name: PitchClass}
PITCH_CLASSES = {name: PitchClass(name) for name in CHROMATIC}


def find_pitch_class(index, quantifier):
    for name, values in CHROMATIC.items():
        if (Pitch(index), Enharmonic(quantifier)) == values:
            return PitchClass(name)
    raise ValueError(f"Pitch Class ({index}, {quantifier}) not found")


def adjust_pitch_class(pitch_class, half_steps, quantifier=None):
    if quantifier is None:
        quantifier = pitch_class.enharmonic.quantifier
    return find_pitch_class((pitch_class.pitch.index + half_steps), quantifier)


def add_fifth(pitch_class, quantifier=None):
    return adjust_pitch_class(pitch_class, 7, quantifier)

