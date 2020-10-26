from setup.constants.enharmonic import FLAT, SHARP
from setup.pitchclass import find_pitch_class


def constrain_step(step):
    if step >= 7:
        step %= 7
    return step


def circle_fifth(step):
    step += 3
    return constrain_step(step)


def circle_fourth(step):
    step += 4
    return constrain_step(step)


class Scale:
    # key --> KeySignature
    def __init__(self, key, scale_type=None):
        # Set-up ----------------------------------------------------
        self.key = key
        self.name = f"{self.key.name} scale"
        # Scale length and type
        if scale_type is None:
            self.length = 7
        else:  # Later implementation may be subclass of Scale
            self.length = len(scale_type)
        # Determine accidentals
        self.accidentals = [0] * 7
        # num_accidental Syntax: (flat, sharps)
        if self.key.accidentals[0] == 0 and self.key.accidentals[1] != 0:
            self.add_sharps(self.key.accidentals[1], self.key.step_start[1])
        if self.key.accidentals[0] != 0 and self.key.accidentals[1] == 0:
            self.add_flats(self.key.accidentals[0], self.key.step_start[0])
        # Building scale
        self.pitch_classes = []
        self.build_scale()

    def __repr__(self):
        return f"{self.__class__.__name__} object: {self.name}"

    def __eq__(self, other):
        if other.__class__ != self.__class__:
            raise ValueError(f"Operand not supported for types: \'{other.__class__}\' and \'{self.__class__}\'")
        return self.name == other.name

    def __iter__(self):
        return (pitch_class for pitch_class in self.pitch_classes)

    def add_sharps(self, num_sharps, step_start):
        for i in range(num_sharps):
            step_start = circle_fifth(step_start)
            self.accidentals[step_start] += SHARP.quantifier

    def add_flats(self, num_flats, step_start):
        for i in range(num_flats):
            step_start = circle_fourth(step_start)
            self.accidentals[step_start] += FLAT.quantifier

    def build_scale(self):
        scale_step = self.key.center.pitch.index
        for half_step, quantifier in zip(self.key.steps, self.accidentals):
            self.pitch_classes.append(find_pitch_class(scale_step, quantifier))
            scale_step += half_step

    # -----------------------------------------------------------


# Scales can be printed with the following syntax:
#
#   note_object = Note(8, -1)
#   ks_object = KeySignature(note_object, "minor")
#   scale_object = Scale(ks_object)
#   for note in scale_object:
#       print(note.name, end=' ')
