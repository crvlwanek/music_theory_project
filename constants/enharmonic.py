# Syntax: {sign: (quantifier, name)}
SIGNS = {"bb": (-2, "double flat"), "b": (-1, "flat"),
         "": (0, "natural"), "#": (1, "sharp"), "##": (2, "double sharp")}


class Enharmonic:

    def __init__(self, quantifier):
        self.quantifier = quantifier
        self.update()

    def __str__(self):
        return f"{self.quantifier}"

    def update(self):
        for sign, values in SIGNS.items():
            if values[0] == self.quantifier:
                self.sign = sign
                self.name = values[1]
        try:
            self.sign
        except AttributeError:
            raise ValueError(f"Quantifier <{self.quantifier}> not defined")

    def adjust(self, amount):
        self.quantifier += amount
        return Enharmonic(self.quantifier)


# Syntax: {sign: (quantifier, Enharmonic)}
ENHARMONICS = {sign: (value[0], Enharmonic(value[0])) for sign, value in SIGNS.items()}

DBFLAT = ENHARMONICS["bb"][1]
FLAT = ENHARMONICS["b"][1]
NATURAL = ENHARMONICS[""][1]
SHARP = ENHARMONICS["#"][1]
DBSHARP = ENHARMONICS["##"][1]


def find_enharmonic(quantifier):
    for sign, values in ENHARMONICS.items():
        if quantifier == values[0]:
            return values[1]
