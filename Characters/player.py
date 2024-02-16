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
                self.weapon = self.startWepPrompt("Melee")
                self.armor = pre.adventureGear
                super().__init__(14, 16, 12, 6, isEnemy = False)
            case "Knight":
                self.weapon = self.startWepPrompt("Melee")
                self.armor = pre.adventureGear
                super().__init__(16, 14, 8, 5, isEnemy = False)
            case "Ranger":
                self.weapon = self.startWepPrompt("Ranged")
                self.armor = pre.clothing
                super().__init__(12, 16, 14, 5, isEnemy = False)
            case "Rogue":
                self.weapon = self.startWepPrompt("Ranged")
                self.armor = pre.clothing
                super().__init__(8, 14, 16, 4, isEnemy = False)

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
                try:
                    # Works if accesory
                    item.isAcc()
                    self.accesory = item
                except Exception:
                    # Works if item
                    self.inventory.append(item)

    def startWepPrompt(self, type):
        print("")

        valid = []
        for wep in pre.weaponTier[0]:
            if wep.dmgType == type:
                valid.append(wep)
        
        for i, wep in enumerate(valid):
            print(str(i + 1) + ": " + wep.name)

        while True:
            choice = input("\nEnter an index starting at 1 to choose your starting weapon\n")
            try:
                for i, wep in enumerate(valid):
                    if int(choice) == i + 1:
                        return wep
            except TypeError:
                pass

        
    def isProf(self, armor):
        return (armor.armWeight == self.type.armor)
    
    def checkLevel(self):
        self.level = self.getLevel()

    
