import math

class Armor():
    # Stats
    name = ""
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

    # Methods
    def __init__(self, name, defense, flatReduction, weight):
        self.name = name
        self.defense = defense
        self.flatReduction = flatReduction
        self.armWeight = weight

    def reduceDamage(self, damage, wearer):
        if wearer.bStr >= self.getStrReq() and wearer.isProf(self):
            if self.armWeight != "Light":
                return math.ceil((damage * (1 - (self.defense / 100))) - self.flatReduction)
            else:
                return math.ceil((damage * (1 - (self.defense / 100))) - self.flatReduction - wearer.getMod("d"))
        else:
            return damage