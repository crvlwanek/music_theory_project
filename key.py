from note import *


def define_modes():
    sharp_offset = 7
    natural_offset = 7
    for mode, info in MODES.items():
        info.append([])
        pitch = NOTES[info[1]][0]
        enharmonic = 0
        for i in range(sharp_offset):
            info[2].append(Note(pitch, enharmonic))
            pitch = add_fifth(pitch)
        enharmonic = 1
        for i in range(8 - sharp_offset):
            info[2].append(Note(pitch, enharmonic))
            pitch = add_fifth(pitch)
        pitch = (NOTES[info[1]][0] + 11) % 12
        enharmonic = -1
        for i in range(natural_offset):
            info[2].append(Note(pitch, enharmonic))
            pitch = add_fifth(pitch)
        enharmonic = 0
        for i in range(7 - natural_offset):
            info[2].append(Note(pitch, enharmonic))
            pitch = add_fifth(pitch)
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


csharp = Note(1, 1)
csharpminor = KeySignature(csharp, "minor")
print(csharpminor)
for note in csharpminor.build_rel_major():
    print(note.name)

