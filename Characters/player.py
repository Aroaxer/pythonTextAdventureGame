import math

from Characters.character import Character
from Playertypes.playertype import Playertype
from Armor.armor import Armor
from Weapons.weapon import Weapon
from Armor import preArmors
from Weapons import preWeapons

class Player(Character):
    exp = 0
    gold = 0
    type = None # Holds the Playertype

    def getLevel(self):
        level = 0
        while self.exp > 5 * level:
            self.exp -= 5 * level
            level += 1
        return level

    def __init__(self, type):
        self.type = type
        self.armor = preArmors.clothing
        match type.name:
            case "Warrior":
                self.weapon = preWeapons.bronzeSword
                super().__init__(14, 16, 12, 6)
            case "Knight":
                self.weapon = preWeapons.bronzeSword
                super().__init__(16, 14, 8, 5)
            case "Ranger":
                self.weapon = preWeapons.oakShortbow
                super().__init__(12, 16, 14, 5)
            case "Rogue":
                self.weapon = preWeapons.oakShortbow
                super().__init__(8, 14, 16, 4)

    def getItem(self, item):
        try:
            item.dealDamage(self)
            self.weapon = item
        except Exception:
            self.armor = item

    def isProf(self, armor):
        return (armor.armWeight in self.type.armors)
    
    def checkLevel(self):
        self.level = self.getLevel()

    
