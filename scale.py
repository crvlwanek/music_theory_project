from key import *

CIRCLE = (0, 3, 6, 2, 5, 1, 4)


def circle(x):
    return (x + 3) % 7


def rev_circle(x):
    return (x + 4) % 7


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
            #self.add_sharps(self.key.accidentals[1])
        if self.key.accidentals[0] != 0 and self.key.accidentals[1] == 0:
            #self.add_flats(self.key.accidentals[0])

    def __str__(self):
        return f"{self.key.name} scale"

    def add_sharps(self, num_sharps):
        pass

    def add_flats(self, num_flats):
        pass
