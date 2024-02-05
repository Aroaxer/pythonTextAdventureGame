

class Armor():
    # Stats
    defense = 0
    flatReduction = 0

    armWeight = "Light"
    def getStrReq(self):
        match self.armWeight:
            case "Light":
                return 0
            case "Medium":
                return 12
            case "Heavy":
                return 16
    strReq = property(fget = getStrReq)


    def getDfsPercent(self): return ((-1.025) ** (-(self.defense - 186))) + 100
    defenseReduction = property(fget = getDfsPercent)

    # Methods
    def __init__(self, defense, flatReduction, weight):
        self.defense = defense
        self.flatReduction = flatReduction
        self.armWeight = weight

    def reduceDamage(self, damage, wearer):
        if wearer.bStr >= self.strReq and self.armWeight in wearer.type.armors:
            return (damage * (self.defenseReduction / 100)) - self.flatReduction
        else:
            return damage