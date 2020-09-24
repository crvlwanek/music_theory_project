DBFLAT, FLAT, NATURAL, SHARP, DBSHARP = -2, -1, 0, 1, 2

NOTES = {"B#": (0, SHARP), "C": (0, NATURAL), "Dbb": (0, DBFLAT),
         "C#": (1, SHARP), "Db": (1, FLAT),
         "C##": (2, DBSHARP), "D": (2, NATURAL), "Ebb": (2, DBFLAT),
         "D#": (3, SHARP), "Eb": (3, FLAT),
         "E": (4, NATURAL), "Fb": (4, FLAT),
         "E#": (5, SHARP), "F": (5, NATURAL),
         "F#": (6, SHARP), "Gb": (6, FLAT),
         "F##": (7, DBSHARP), "G": (7, NATURAL), "Abb": (7, DBFLAT),
         "G#": (8, SHARP), "Ab": (8, FLAT),
         "G##": (9, DBSHARP), "A": (9, NATURAL), "Bbb": (9, DBFLAT),
         "A#": (10, SHARP), "Bb": (10, FLAT),
         "B": (11, NATURAL), "Cb": (11, FLAT)}

ACCIDENTALS = {"C": 0, "G": 1, "D": 2, "A": 3, "E": 4, "B": 5, "F#": 6, "C#": 7,
               "F": -1, "Bb": -2, "Eb": -3, "Ab": -4, "Db": -5, "Gb": -6, "Cb": -7}

FREQUENCIES = []

MODES = {"lydian": [4, "F"], "major": [1, "C"], "mixolydian": [5, "G"],
         "dorian": [2, "D"], "minor": [6, "A"], "phrygian": [2, "E"], "locrian": [7, "B"]}

MAJOR_STEPS = [0, 2, 4, 5, 7, 9, 11]

TET = 12

