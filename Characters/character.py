from Weapons import preWeapons
from Armor import preArmors

class Character():
    # Stats
    bStr = 10
    bDex = 10
    bCon = 10

    level = 1
    hpPerLevel = 5

    def getMaxHp(self): 
        levelHp = self.hpPerLevel + self.getMod("c")
        return self.level * levelHp
    maxHealth = property(fget = getMaxHp)
    hp = 0

    weapon = None
    armor = None

    # Methods
    def __init__(self, str, con , dex, hpPerLevel, gearSet = None) -> None:
        self.bStr = str
        self.bDex = dex
        self.bCon = con
        self.hpPerLevel = hpPerLevel
        self.hp = self.maxHealth

        if not gearSet == None:
            match gearSet:
                case "Basic Str":
                    self.weapon = preWeapons.bronzeSword
                    self.armor = preArmors.leatherArmor
                case "Basic Dex":
                    self.weapon = preWeapons.oakShortbow
                    self.armor = preArmors.leatherArmor
                case "Medium Str":
                    self.weapon = preWeapons.ironSword
                    self.armor = preArmors.scaleMail
                case "Medium Dex":
                    self.weapon = preWeapons.ironShortbow
                    self.armor = preArmors.studdedLeather

    def takeDamage(self, source, amt):
        self.hp -= self.armor.reduceDamage(amt, self)
        return (self.hp <= 0)

    def attack(self, target, damageMult = 1):
        return target.takeDamage(self, self.weapon.dealDamage(self) * damageMult)

    def getMod(self, stat): 
        match stat:
            case "s":
                return round((self.bStr - 10) / 2)
            case "d":
                return round((self.bDex - 10) / 2)
            case "c":
                return round((self.bCon - 10) / 2)
