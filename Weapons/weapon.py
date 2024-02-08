import random
import math

class Weapon():
    # Stats
    name = ""

    dmgType = "Melee"
    specType = "Sweep"
    
    damage = 0
    specMult = 0


    # Methods
    def __init__(self, name, dmg, type, specType, specMult) -> None:
        self.name = name
        self.dmgType = type
        self.specType = specType
        
        self.damage = dmg
        self.specMult = specMult

    def dealDamage(self, wielder):
        relevantMod = 0
        match self.dmgType:
            case "Melee":
                relevantMod = wielder.getMod("s")
            case "Ranged":
                relevantMod = wielder.getMod("d")
        try:
            if wielder.type.weapon == self.dmgType:
                return (self.damage + relevantMod) / 2
            else:
                return (relevantMod) / 2
        except Exception:
            return (self.damage + relevantMod) / 5
        