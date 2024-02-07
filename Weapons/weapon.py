import random
import math

class Weapon():
    # Stats
    name = ""
    dmgLow = 0
    dmgHigh = 0

    dmgType = "Melee"
    specType = "Sweep"
    
    def getDamage(self): return random.randint(self.dmgLow, self.dmgHigh)


    # Methods
    def __init__(self, name, dmg, type, specType) -> None:
        self.name = name
        self.dmgType = type
        self.specType = specType
        
        variation = math.ceil(dmg / 5)
        self.dmgLow = dmg - variation
        self.dmgHigh = dmg + variation

    def dealDamage(self, wielder):
        relevantMod = 0
        match self.dmgType:
            case "Melee":
                relevantMod = wielder.getMod("s")
            case "Ranged":
                relevantMod = wielder.getMod("d")
        try:
            if wielder.type.weapon == self.dmgType:
                return (self.getDamage() + relevantMod)
            else:
                return (relevantMod) / 2
        except Exception:
            return (self.getDamage() + relevantMod) / 5
        