from Weapons.weapon import Weapon
from Armor.armor import Armor

from Armor import preArmors

class Character():
    # Stats
    bStr = 10
    bDex = 10
    bCon = 10

    level = 1
    hpPerLevel = 5

    def getMod(stat): return round((stat - 10) / 2)
    strMod = property(fget = getMod(bStr))
    dexMod = property(fget = getMod(bDex))
    conMod = property(fget = getMod(bCon))

    def getMaxHp(self): return self.level * (self.hpPerLevel + self.conMod)
    maxHealth = property(fget = getMaxHp)
    currentHealth = 0

    weapon = None
    armor = None

    # Methods
    def __init__(self, str, dex, con, hpPerLevel) -> None:
        self.bStr = str
        self.bDex = dex
        self.bCon = con
        self.hpPerLevel = hpPerLevel
        self.currentHealth = self.maxHealth

    def takeDamage(self, source, amt):
        self.hp -= self.armor.reduceDamage(amt)
        # TODO: check if dead

    def attack(self, target, damageMult = 1):
        target.takeDamage(self, self.weapon.dealDamage() * damageMult)

