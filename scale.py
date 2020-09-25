from key import *


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

    def __init__(self, key, scale_type=None):
        if scale_type is None:
            self.length = 7
        else:  # Later implementation may be subclass of Scale
            self.length = len(scale_type)
        self.key = key
        self.accidentals = [0] * 7
        # num_accidental Syntax: (flat, sharps)
        if self.key.accidentals[0] == 0 and self.key.accidentals[1] != 0:
            self.add_sharps(self.key.accidentals[1], self.key.step_start[1])
        if self.key.accidentals[0] != 0 and self.key.accidentals[1] == 0:
            self.add_flats(self.key.accidentals[0], self.key.step_start[0])
        self.scale = []
        self.build_scale()

    def __str__(self):
        return f"<{self.key.name} scale>"

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
            self.scale.append(find_note(scale_step, quantifier))
            scale_step += half_step


ab = Note(8, -1)
abminor = KeySignature(ab, "minor")
so = Scale(abminor)
for note in so.scale:
    print(note.name)
