TET = 12  # Future-proofing to implement other equal temperaments


class Pitch:
    # index --> int
    def __init__(self, index):
        # Set-up ----------------------------------------------------
        try:
            int(index)
        except ValueError:
            raise ValueError(f"<{index}> is not a valid pitch")
        self.index = index
        self.constrain_chromatic()

    def __repr__(self):
        return f"{self.__class__.__name__} object: {self.index}"

    def __eq__(self, other):
        if other.__class__ != self.__class__:
            raise ValueError(f"Operand not supported for types: \'{other.__class__}\' and \'{self.__class__}\'")
        return self.index == other.index

        # -----------------------------------------------------------

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


def constrain_chromatic(index):
    if index >= TET:
        index %= TET
        constrain_chromatic(index)
    if index < 0:
        index += TET
        constrain_chromatic(index)
    else:
        return index
