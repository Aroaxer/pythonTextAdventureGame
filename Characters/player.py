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

    def __init__(self, type):
        self.type = type
        self.armor = preArmors.leatherArmor
        match type.name:
            case "Warrior":
                self.weapon = preWeapons.bronzeSword
                super.__init__(14, 16, 12, 6)
            case "Knight":
                self.weapon = preWeapons.bronzeSword
                super.__init__(16, 14, 8, 5)
            case "Ranger":
                self.weapon = preWeapons.oakShortbow
                super.__init__(12, 16, 14, 5)
            case "Rogue":
                self.weapon = preWeapons.oakShortbow
                super.__init__(8, 14, 16, 4)

    def getItem(self, item):
        if item.type == Weapon:
            self.weapon = item
        elif item.type == Armor:
            self.armor = item

    
    def useSpecial(self, game):
        if self.weapon.dmgType == "Melee":
            for enemy in game.enemies:
                self.attack(enemy, 0.5)
        elif self.weapon.dmgType == "Ranged":
            print("This attack targets the next highest index as well.")
            target = game.getTarget(returnsIndex = True)
            self.attack(target, 0.75)
            self.attack(target + 1, 0.75)
    
