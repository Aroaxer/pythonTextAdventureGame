import random

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
        return (1 + (self.level / 5)) * levelHp
    maxHealth = property(fget = getMaxHp)
    hp = 0

    weapon = None
    armor = None

    blockPower = 3
    blockCharges = 0

    chargeMult = 1
    chargePower = 1

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
                    self.armor = preArmors.clothing
                case "Medium Str":
                    self.weapon = preWeapons.ironSword
                    self.armor = preArmors.hideArmor
                case "Medium Dex":
                    self.weapon = preWeapons.ironShortbow
                    self.armor = preArmors.leatherArmor
                case "Advanced Str":
                    kit = random.randint(1, 4)
                    match kit:
                        case 1 | 2:
                            self.weapon = preWeapons.steelSword
                        case 3:
                            self.weapon = preWeapons.steelSpear
                        case 4:
                            self.weapon = preWeapons.steelAxe
                    self.armor = preArmors.chainmailArmor
                case "Advanced Dex":
                    kit = random.randint(1, 4)
                    match kit:
                        case 1 | 2:
                            self.weapon = preWeapons.oakLongbow
                        case 3:
                            self.weapon = preWeapons.heavyCrossbow
                        case 4:
                            self.weapon = preWeapons.steelJavelin
                    self.armor = preArmors.steelsilkArmor
                case "Greater Str":
                    kit = random.randint(1, 4)
                    match kit:
                        case 1 | 2:
                            self.weapon = preWeapons.mythrilSword
                        case 3:
                            self.weapon = preWeapons.mythrilSpear
                        case 4:
                            self.weapon = preWeapons.mythrilAxe
                    self.armor = preArmors.splintArmor
                case "Greater Dex":
                    kit = random.randint(1, 4)
                    match kit:
                        case 1 | 2:
                            self.weapon = preWeapons.ironLongbow
                        case 3:
                            self.weapon = preWeapons.steelCrossbow
                        case 4:
                            self.weapon = preWeapons.mythrilJavelin
                    self.armor = preArmors.steelsilkArmor
                case "Runic Str":
                    kit = random.randint(1, 4)
                    match kit:
                        case 1 | 2:
                            self.weapon = preWeapons.runicSword
                        case 3:
                            self.weapon = preWeapons.runicSpear
                        case 4:
                            self.weapon = preWeapons.runicAxe
                    self.armor = preArmors.plateArmor
                case "Runic Dex":
                    kit = random.randint(1, 4)
                    match kit:
                        case 1 | 2:
                            self.weapon = preWeapons.runicBow
                        case 3:
                            self.weapon = preWeapons.runicCrossbow
                        case 4:
                            self.weapon = preWeapons.runicJavelin
                    self.armor = preArmors.runicLeather

    def takeDamage(self, source, amt):
        tempHp = self.hp
        self.hp -= (self.armor.reduceDamage(amt, self) / (self.blockPower if self.blockCharges > 0 else 1))
        if self.hp > tempHp: self.hp = tempHp
        return (self.hp <= 0)

    def attack(self, target, damageMult = 1):
        tempCharge = self.chargeMult
        self.chargeMult = 1
        return target.takeDamage(self, self.weapon.dealDamage(self) * damageMult * tempCharge)
    
    def block(self):
        self.blockCharges = 3

    def charge(self):
        self.chargeMult += self.chargePower

    def getMod(self, stat): 
        match stat:
            case "s":
                return round((self.bStr - 10) / 2)
            case "d":
                return round((self.bDex - 10) / 2)
            case "c":
                return round((self.bCon - 10) / 2)

    def useSpecial(self, game):
        if self.weapon.specType == "Sweep":
            print("This attack targets all enemies.")
            for enemy in game.enemies:
                self.attack(enemy, self.weapon.specMult)
        elif self.weapon.specType == "Pierce":
            print("This attack targets the next highest index as well.")
            target = game.getTarget(returnsIndex = True)
            self.attack(game.enemies[target], self.weapon.specMult)
            if target < len(game.enemies) - 1:
                self.attack(game.enemies[target + 1], self.weapon.specMult)
        elif self.weapon.specType == "Weakening":
            print("This attack causes the enemy's next attack to do much less damage.")
            target = game.getTarget()
            self.attack(target, self.weapon.specMult)
            target.chargeMult /= 2
        elif self.weapon.specType == "Fracturing":
            print("This attack makes the enemy vulnerable to your next attack.")
            target = game.getTarget()
            self.attack(target, self.weapon.specMult)
            target.blockDivisor /= 2