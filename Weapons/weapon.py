import random
import math

class Weapon():
    # Stats
    name = ""

    dmgType = "Melee"
    specType = "Sweep"
    
    damage = 0
    specMult = 0
    multi = 1


    # Methods
    def __init__(self, name, dmg, type, specType, specMult, multi = 1) -> None:
        self.name = name
        self.dmgType = type
        self.specType = specType
        self.multi = multi
        
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
        
    def getStatDisplay(self):
        return (str(self.name) + ": " + str(self.damage) + " " + str(self.dmgType) + " damage\n" +
                      str(self.specType) + " special, hits " + str(self.multi) + " enemies" + ((", " + str(self.specMult) + " special damage multiplier") if self.specType != "Oneshot" and self.specMult != "Finisher" else ("")))
        