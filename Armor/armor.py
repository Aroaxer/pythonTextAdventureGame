from Characters.character import Character

class Armor():
    # Stats
    defense = 0
    flatReduction = 0

    strReq = 0

    def getDfsPercent(self): return ((-1.025) ** (-(self.defense - 186))) + 100
    defenseReduction = property(fget = getDfsPercent)

    # Methods
    def __init__(self, defense, flatReduction, strReq):
        self.defense = defense
        self.flatReduction = flatReduction
        self.strReq = strReq

    def reduceDamage(self, damage, wearer):
        if wearer.bStr >= self.strReq:
            return (damage * (self.defenseReduction / 100)) - self.flatReduction
        else:
            return damage