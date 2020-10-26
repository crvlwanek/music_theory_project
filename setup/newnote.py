from setup.pitchclass import *


def find_frequency(midi, temperament):
    return temperament * (2 ** ((midi-57) / TET))


class Note(PitchClass):

    A440 = 440

    def __init__(self, index, quantifier, octave, temperament=A440):

        self.pitch_class = find_pitch_class(index, quantifier)
        self.octave = octave
        self.name = self.pitch_class.name + str(self.octave)
        self.temperament = temperament
        self.midi = self.pitch_class.pitch.index + (TET * self.octave)
        self.frequency = find_frequency(self.midi, self.temperament)

    def __repr__(self):
        return f"{self.__class__.__name__} object: {self.name}"
