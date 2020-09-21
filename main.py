from constants import NOTES, MODES, STEPS, TET


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


gm_kso = KeySignature("G", "minor")
g_minor_scale = gm_kso.build_scale()
print(g_minor_scale)
