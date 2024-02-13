import math

from Characters.character import Character
import premades as pre

class Player(Character):
    exp = 0
    gold = 0
    type = None # Holds the Playertype
    inventory = []

    def getLevel(self):
        lvl = 0
        tempExp = self.exp
        while tempExp > 5 * lvl:
            tempExp -= 5 * lvl
            lvl += 1
        return lvl

    def __init__(self, type):
        self.type = type
        match type.name:
            case "Warrior":
                self.weapon = pre.bronzeSword
                self.armor = pre.adventureGear
                super().__init__(14, 16, 12, 6)
            case "Knight":
                self.weapon = pre.bronzeSword
                self.armor = pre.adventureGear
                super().__init__(16, 14, 8, 5)
            case "Ranger":
                self.weapon = pre.oakShortbow
                self.armor = pre.clothing
                super().__init__(12, 16, 14, 5)
            case "Rogue":
                self.weapon = pre.oakShortbow
                self.armor = pre.clothing
                super().__init__(8, 14, 16, 4)

    def getItem(self, item):
        try: 
            # Works if weapon
            item.dealDamage(self)
            self.weapon = item
        except Exception:
            try: 
                # Works if armor
                item.reduceDamage(0, self)
                self.armor = item
            except Exception:
                # Works if item
                self.inventory.append(item)

    def isProf(self, armor):
        return (armor.armWeight in self.type.armors)
    
    def checkLevel(self):
        self.level = self.getLevel()

    
