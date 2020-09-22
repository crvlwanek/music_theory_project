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

FREQUENCIES = []

MODES = {"lydian": [4, "F"], "major": [1, "C"], "mixolydian": [5, "G"],
         "dorian": [2, "D"], "minor": [6, "A"], "phrygian": [2, "E"], "locrian": [7, "B"]}


def choose_enh(chr_index, accidental):
    for k, v in NOTES.items():
        if v == (chr_index, accidental):
            return k


def add_fifth(pitch):
    pitch += 7
    if pitch >= 12:
        pitch = pitch % 12
    return pitch


sharp_offset = 7
natural_offset = 7
for mode, info in MODES.items():
    info.append([])
    p = NOTES[info[1]][0]
    acc = 0
    for i in range(sharp_offset):
        info[2].append(choose_enh(p, acc))
        p = add_fifth(p)
    acc = 1
    for i in range(8 - sharp_offset):
        info[2].append(choose_enh(p, acc))
        p = add_fifth(p)
    p = (NOTES[info[1]][0] + 11) % 12
    acc = -1
    for i in range(natural_offset):
        info[2].append(choose_enh(p, acc))
        p = add_fifth(p)
    acc = 0
    for i in range(7 - natural_offset):
        info[2].append(choose_enh(p, acc))
        p = add_fifth(p)
    sharp_offset -= 1
    natural_offset -= 1


def is_mode(n, m):
    if n in MODES[m][2]:
        return True
    else:
        return False


print(is_mode("G#", "major"))
