from key import *


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
