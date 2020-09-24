from note import *

# Accidentals in 15 keys with syntax: (num_flats, num_sharps)
ACCIDENTALS = ((0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
               (7, 0), (6, 0), (5, 0), (4, 0), (3, 0), (2, 0), (1, 0))

# Set of all valid modes of the major scale, with indexes
# matching the appropriate value in ACCIDENTALS
MODES = {"lydian": ("F", "C", "G", "D", "A", "E", "B", "F#",
                    "Fb", "Cb", "Gb", "Db", "Ab", "Eb", "Bb"),
         "major": ("C", "G", "D", "A", "E", "B", "F#", "C#",
                   "Cb", "Gb", "Db", "Ab", "Eb", "Bb", "F"),
         "mixolydian": ("G", "D", "A", "E", "B", "F#", "C#", "G#",
                        "Gb", "Db", "Ab", "Eb", "Bb", "F", "C"),
         "dorian": ("D", "A", "E", "B", "F#", "C#", "G#", "D#",
                    "Db", "Ab", "Eb", "Bb", "F", "C", "G"),
         "minor": ("A", "E", "B", "F#", "C#", "G#", "D#", "A#",
                   "Ab", "Eb", "Bb", "F", "C", "G", "D"),
         "phrygian": ("E", "B", "F#", "C#", "G#", "D#", "A#", "E#",
                      "Eb", "Bb", "F", "C", "G", "D", "A"),
         "locrian": ("B", "F#", "C#", "G#", "D#", "A#", "E#", "B#",
                     "Bb", "F", "C", "G", "D", "A", "E")}


class KeySignature:

    def __init__(self, center, mode):
        self.center = center
        self.mode = mode
        self.name = self.center.name + ' ' + mode
        self.scale_len = 7
        if not self.is_mode():
            raise ValueError("Invalid key center/mode pair")

    def __str__(self):
        return f"<KeySignature object: {self.center} {self.mode}>"

    def is_mode(self):
        for name, values in MODES.items():
            for value in values:
                if value == self.center.name and name == self.mode:
                    return True


g = Note(7, 0)
gmajor = KeySignature(g, "major")
print(gmajor.name)
