# Accidentals in 15 keys with syntax: (num_flats, num_sharps)
ACCIDENTALS = ((0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
               (7, 0), (6, 0), (5, 0), (4, 0), (3, 0), (2, 0), (1, 0))

# Set of all valid mode centers of the major scale, with indexes
# matching the appropriate value in ACCIDENTALS
# Syntax: {mode: ((valid centers), (steps), (flat start, sharp start)}
MODES = {"lydian":     (("F", "C", "G", "D", "A", "E", "B", "F#",
                         "Fb", "Cb", "Gb", "Db", "Ab", "Eb", "Bb"),
                        (2, 2, 2, 1, 2, 2, 1), (3, 0)),
         "major":      (("C", "G", "D", "A", "E", "B", "F#", "C#",
                         "Cb", "Gb", "Db", "Ab", "Eb", "Bb", "F"),
                        (2, 2, 1, 2, 2, 2, 1), (6, 3)),
         "mixolydian": (("G", "D", "A", "E", "B", "F#", "C#", "G#",
                         "Gb", "Db", "Ab", "Eb", "Bb", "F", "C"),
                        (2, 2, 1, 2, 2, 1, 2), (2, 6)),
         "dorian":     (("D", "A", "E", "B", "F#", "C#", "G#", "D#",
                         "Db", "Ab", "Eb", "Bb", "F", "C", "G"),
                        (2, 1, 2, 2, 2, 1, 2), (5, 2)),
         "minor":      (("A", "E", "B", "F#", "C#", "G#", "D#", "A#",
                         "Ab", "Eb", "Bb", "F", "C", "G", "D"),
                        (2, 1, 2, 2, 1, 2, 2), (1, 5)),
         "phrygian":   (("E", "B", "F#", "C#", "G#", "D#", "A#", "E#",
                         "Eb", "Bb", "F", "C", "G", "D", "A"),
                        (1, 2, 2, 2, 1, 2, 2), (4, 1)),
         "locrian":    (("B", "F#", "C#", "G#", "D#", "A#", "E#", "B#",
                         "Bb", "F", "C", "G", "D", "A", "E"),
                        (1, 2, 2, 1, 2, 2, 2), (0, 4))}


class KeySignature:
    # center, mode --> PitchClass, str
    def __init__(self, center, mode):
        # Set-up ----------------------------------------------------
        self.center = center
        self.mode = mode
        self.name = self.center.name + ' ' + mode

        self.accidentals = None
        if not self.is_mode():
            raise ValueError("Invalid key center/mode pair")
        self.steps = MODES[self.mode][1]
        self.step_start = MODES[self.mode][2]

    def __repr__(self):
        return f"{self.__class__.__name__} object: {self.name}"

    def __eq__(self, other):
        if other.__class__ != self.__class__:
            raise ValueError(f"Operand not supported for types: \'{other.__class__}\' and \'{self.__class__}\'")
        return self.name == other.name

    def is_mode(self):
        for index, name in enumerate(MODES[self.mode][0]):
            if name == self.center.name:
                self.accidentals = ACCIDENTALS[index]
                return True

    # -----------------------------------------------------------
