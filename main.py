from constants.constants import NOTES, MODES, STEPS, TET


class KeySignature:

    def __init__(self, center, mode):
        self.center = center
        self.mode = mode
        for note in NOTES:
            if note.count(center):
                self.center_chr = NOTES.index(note)
                self.center_enh = note.index(center)

    def build_scale(self):
        center = self.center_chr
        mode = MODES.index(self.mode)
        steps = STEPS[mode:] + [step + TET for step in STEPS[:mode]]
        steps[:] = [step - STEPS[mode] for step in steps]
        scale = [NOTES[(center + step) % TET] for step in steps]
        return scale

    def is_sharp(self):
        pass

    def is_flat(self):
        pass

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

    def add_fifth(pitch):
        return adjust_chromatic(pitch, 7)

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

    def get_accidentals(total_accidentals, adjust_accidental, scale_len):
        accidentals = [0] * scale_len
        if total_accidentals == 0:
            return accidentals
        if total_accidentals > 0:
            step = 3
        if total_accidentals < 0:
            step = 3
        for i in range(abs(total_accidentals)):
            if total_accidentals > 0:
                step = circle_fourth(step)
            if total_accidentals < 0:
                step = circle_fourth(step)
            accidentals[step] += adjust_accidental
        return accidentals


gm_kso = KeySignature("G", "minor")
g_minor_scale = gm_kso.build_scale()
print(g_minor_scale)
