import random
import math

from Characters.character import Character

class Weapon():
    # Stats
    dmgLow = 0
    dmgHigh = 0

    dmgType = "Melee"
    
    def getDamage(self): return random.randint(self.dmgLow, self.dmgHigh)


    # Methods
    def __init__(self, dmg, type) -> None:
        self.dmgType = type
        
        variation = math.ceil(dmg / 5)
        self.dmgLow = dmg - variation
        self.dmgHigh = dmg + variation

    def dealDamage(self, wielder):
        relevantMod = 0
        match self.dmgType:
            case "Melee":
                relevantMod = wielder.strMod
            case "Ranged":
                relevantMod = wielder.dexMod
        if wielder.type.weapon == self.dmgType:
            return self.getDamage() + relevantMod
        else:
            return 0 + relevantMod
        