from note import *

# Accidentals in 15 keys with syntax: (num_flats, num_sharps)
ACCIDENTALS = ((0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
               (7, 0), (6, 0), (5, 0), (4, 0), (3, 0), (2, 0), (1, 0))

# Set of all valid mode centers of the major scale, with indexes
# matching the appropriate value in ACCIDENTALS
# Syntax: {mode: ((valid centers), (steps))}
MODES = {"lydian": (("F", "C", "G", "D", "A", "E", "B", "F#",
                    "Fb", "Cb", "Gb", "Db", "Ab", "Eb", "Bb"), (2, 2, 2, 1, 2, 2, 1)),
         "major": (("C", "G", "D", "A", "E", "B", "F#", "C#",
                    "Cb", "Gb", "Db", "Ab", "Eb", "Bb", "F"), (2, 2, 1, 2, 2, 2, 1)),
         "mixolydian": (("G", "D", "A", "E", "B", "F#", "C#", "G#",
                        "Gb", "Db", "Ab", "Eb", "Bb", "F", "C"), (2, 2, 1, 2, 2, 1, 2)),
         "dorian": (("D", "A", "E", "B", "F#", "C#", "G#", "D#",
                    "Db", "Ab", "Eb", "Bb", "F", "C", "G"), (2, 1, 2, 2, 2, 1, 2)),
         "minor": (("A", "E", "B", "F#", "C#", "G#", "D#", "A#",
                   "Ab", "Eb", "Bb", "F", "C", "G", "D"), (2, 1, 2, 2, 1, 2, 2)),
         "phrygian": (("E", "B", "F#", "C#", "G#", "D#", "A#", "E#",
                      "Eb", "Bb", "F", "C", "G", "D", "A"), (1, 2, 2, 2, 1, 2, 2)),
         "locrian": (("B", "F#", "C#", "G#", "D#", "A#", "E#", "B#",
                     "Bb", "F", "C", "G", "D", "A", "E"), (1, 2, 2, 1, 2, 2, 2))}

MAJOR_STEPS = [0, 2, 2, 1, 2, 2, 1]


class KeySignature:

    def __init__(self, center, mode):
        self.center = center
        self.mode = mode
        self.accidentals = None
        if not self.is_mode():
            raise ValueError("Invalid key center/mode pair")
        self.steps = MODES[self.mode][1]
        self.name = self.center.name + ' ' + mode

    def __str__(self):
        return f"<KeySignature object: {self.center} {self.mode}>"

    def is_mode(self):
        for name, values in MODES.items():
            for value in values[0]:
                if value == self.center.name and name == self.mode:
                    self.accidentals = ACCIDENTALS[values[0].index(value)]
                    return True
