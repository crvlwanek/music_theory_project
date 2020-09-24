TET = 12  # Future-proofing to implement other equal temperaments


class Pitch:

    def __init__(self, index):
        self.index = index
        try:
            int(self.index)
        except ValueError:
            raise ValueError(f"<{self.index}> is not a valid pitch")
        self.constrain_chromatic()

    def __str__(self):
        return f"{self.index}"

    def constrain_chromatic(self):
        if self.index >= TET:
            self.index %= TET
            self.constrain_chromatic()
        if self.index < 0:
            self.index += TET
            self.constrain_chromatic()
        else:
            return self.index


# Set of pitches in a given TET
PITCHES = [Pitch(i) for i in range(TET)]


def find_pitch(index):
    for pitch in PITCHES:
        if index == pitch.index:
            return pitch
