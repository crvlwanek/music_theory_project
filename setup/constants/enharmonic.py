# Syntax: {quantifier: (sign, name)}
SIGNS = {-2: ("bb", "double flat"), -1: ("b", "flat"),
         0: ("", "natural"), 1: ("#", "sharp"), 2: ("##", "double sharp")}


class Enharmonic:
    # quantifier --> int
    def __init__(self, quantifier):
        # Set-up ----------------------------------------------------
        if quantifier not in SIGNS:
            raise ValueError(f"Quantifier <{quantifier}> not defined")
        self.quantifier = quantifier
        self.sign = SIGNS[self.quantifier][0]
        self.name = SIGNS[self.quantifier][1]

    def __repr__(self):
        return f"{self.__class__.__name__} object: {self.quantifier}"

    def __eq__(self, other):
        if other.__class__ != self.__class__:
            raise ValueError(f"Operand not supported for types: \'{other.__class__}\' and \'{self.__class__}\'")
        return self.quantifier == other.quantifier

        # -----------------------------------------------------------


DBFLAT = Enharmonic(-2)
FLAT = Enharmonic(-1)
NATURAL = Enharmonic(0)
SHARP = Enharmonic(1)
DBSHARP = Enharmonic(2)
