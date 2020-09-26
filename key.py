from note import *


def define_modes():
    sharp_offset = 6
    natural_offset = 6
    for mode, info in MODES.items():
        info.append([])
        add = Note(NOTES[info[1]][0], 0)
        info[2].append(add)
        for i in range(sharp_offset):
            add = add.add_fifth()
            info[2].append(add)
        add = add.adjust_chromatic(7, 1)
        info[2].append(add)
        for i in range(6 - sharp_offset):
            add = add.add_fifth()
            info[2].append(add)
        add = add.adjust_chromatic(10, -1)
        info[2].append(add)
        for i in range(natural_offset):
            add = add.add_fifth()
            info[2].append(add)
        if natural_offset < 6:
            add = add.adjust_chromatic(7, 0)
            info[2].append(add)
            for i in range(5 - natural_offset):
                add = add.add_fifth()
                info[2].append(add)
        sharp_offset -= 1
        natural_offset -= 1


def is_mode(center, mode):
    for name in MODES[mode][2]:
        if center.is_same(name):
            return True
    else:
        return False


class KeySignature:

    def __init__(self, center, mode):
        define_modes()
        self.center = center
        self.mode = mode
        self.name = center.name + ' ' + mode
        self.scale_len = 7
        if not is_mode(self.center, self.mode):
            raise ValueError("Invalid key center/mode pair")
        for notes in MODES[self.mode][2]:
            if notes.name == self.center.name:
                self.rel_major = MODES["major"][2][MODES[self.mode][2].index(notes)]

    def __str__(self):
        return f"<KeySignature object: {self.center} {self.mode}>"

    def find_accidentals(self):
        scale_len = self.scale_len
        total_accidentals = ACCIDENTALS[self.rel_major.name]
        if total_accidentals > 0:
            return get_accidentals(total_accidentals, SHARP, scale_len)
        elif total_accidentals < 0:
            return get_accidentals(total_accidentals, FLAT, scale_len)
        else:
            return get_accidentals(total_accidentals, NATURAL, scale_len)

    def build_rel_major(self):
        scale = []
        tonic = NOTES[self.rel_major.name][0]
        accidentals = self.find_accidentals()
        for step in range(self.scale_len):
            pitch = adjust_chromatic(tonic, MAJOR_STEPS[step])
            scale.append(Note(pitch, accidentals[step]))
        return scale


bflat = Note(10, -1)
bflat_major = KeySignature(bflat, "minor")
print(bflat_major.rel_major)
