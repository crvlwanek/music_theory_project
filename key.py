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


def choose_enh(chr_index, accidental):
    for k, v in NOTES.items():
        if v == (chr_index, accidental):
            return k


def add_interval(pitch, interval):
    pitch += interval
    if pitch >= 12:
        pitch = pitch % 12
    return pitch


def add_fifth(pitch):
    return add_interval(pitch, 7)


def circle_fifth(step):
    step += 4
    if step > 6:
        step = step % 7
    return step


def circle_fourth(step):
    step += 3
    if step > 6:
        step = step % 7
    return step


def define_modes():
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


def is_mode(center, mode):
    if center in MODES[mode][2]:
        return True
    else:
        return False


def get_accidentals(total_accidentals, adjust_accidental, scale_len):
    accidentals = [0] * scale_len
    if total_accidentals == 0:
        return accidentals
    if total_accidentals > 0:
        step = 3
    if total_accidentals < 0:
        step = 2
        for i in range(abs(total_accidentals)):
            step = circle_fourth(step)
    for i in range(abs(total_accidentals)):
        if total_accidentals > 0:
            step = circle_fourth(step)
        if total_accidentals < 0:
            step = circle_fifth(step)
        accidentals[step] += adjust_accidental
    return accidentals


class KeySignature:

    def __init__(self, center, mode):
        define_modes()
        self.center = center
        self.mode = mode
        self.scale_len = 7
        if not is_mode(self.center, self.mode):
            raise ValueError("Invalid key center/mode pair")
        self.rel_major = MODES["major"][2][MODES[self.mode][2].index(self.center)]

    def find_accidentals(self):
        scale_len = self.scale_len
        total_accidentals = ACCIDENTALS[self.rel_major]
        if total_accidentals > 0:
            return get_accidentals(total_accidentals, SHARP, scale_len)
        elif total_accidentals < 0:
            return get_accidentals(total_accidentals, FLAT, scale_len)
        else:
            return get_accidentals(total_accidentals, NATURAL, scale_len)


    def build_rel_major(self):
        scale = []
        tonic = NOTES[self.rel_major][0]
        accidentals = self.find_accidentals()
        print(accidentals)
        for step in range(self.scale_len):
            pitch = add_interval(tonic, MAJOR_STEPS[step])
            print(pitch)
            print(accidentals[step])
            scale.append(choose_enh(pitch, accidentals[step]))
        return scale



gsharpminor = KeySignature("G#", "minor")
print(gsharpminor.rel_major)
print(gsharpminor.build_rel_major())

