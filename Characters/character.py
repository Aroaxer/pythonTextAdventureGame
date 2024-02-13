import random

import premades as pre

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

    baseBlock = 3
    blockPower = baseBlock
    blockCharges = 0
    blockChargesOnBlock = 3

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
                    self.weapon = pre.bronzeSword
                    self.armor = pre.leatherArmor
                case "Basic Dex":
                    self.weapon = pre.oakShortbow
                    self.armor = pre.clothing
                case "Medium Str":
                    self.weapon = pre.ironSword
                    self.armor = pre.hideArmor
                case "Medium Dex":
                    self.weapon = pre.ironShortbow
                    self.armor = pre.leatherArmor
                case "Advanced Str":
                    kit = random.randint(1, 4)
                    match kit:
                        case 1 | 2:
                            self.weapon = pre.steelSword
                        case 3:
                            self.weapon = pre.steelSpear
                        case 4:
                            self.weapon = pre.steelAxe
                    self.armor = pre.chainmailArmor
                case "Advanced Dex":
                    kit = random.randint(1, 4)
                    match kit:
                        case 1 | 2:
                            self.weapon = pre.oakLongbow
                        case 3:
                            self.weapon = pre.heavyCrossbow
                        case 4:
                            self.weapon = pre.steelJavelin
                    self.armor = pre.steelsilkArmor
                case "Greater Str":
                    kit = random.randint(1, 4)
                    match kit:
                        case 1 | 2:
                            self.weapon = pre.mythrilSword
                        case 3:
                            self.weapon = pre.mythrilSpear
                        case 4:
                            self.weapon = pre.mythrilAxe
                    self.armor = pre.splintArmor
                case "Greater Dex":
                    kit = random.randint(1, 4)
                    match kit:
                        case 1 | 2:
                            self.weapon = pre.ironLongbow
                        case 3:
                            self.weapon = pre.steelCrossbow
                        case 4:
                            self.weapon = pre.mythrilJavelin
                    self.armor = pre.steelsilkArmor
                case "Runic Str":
                    kit = random.randint(1, 4)
                    match kit:
                        case 1 | 2:
                            self.weapon = pre.runicSword
                        case 3:
                            self.weapon = pre.runicSpear
                        case 4:
                            self.weapon = pre.runicAxe
                    self.armor = pre.plateArmor
                case "Runic Dex":
                    kit = random.randint(1, 4)
                    match kit:
                        case 1 | 2:
                            self.weapon = pre.runicBow
                        case 3:
                            self.weapon = pre.runicCrossbow
                        case 4:
                            self.weapon = pre.runicJavelin
                    self.armor = pre.runicLeather

    def takeDamage(self, source, amt):
        tempHp = self.hp
        self.hp -= round(self.armor.reduceDamage(amt, self) / (self.blockPower if self.blockCharges > 0 else 1))
        if self.hp > tempHp: self.hp = tempHp
        self.blockPower = self.baseBlock
        self.blockCharges -= (1 if self.blockCharges > 0 else 0)
        return (self.hp <= 0)

    def attack(self, target, damageMult = 1):
        tempCharge = self.chargeMult
        self.chargeMult = 1
        return target.takeDamage(self, self.weapon.dealDamage(self) * damageMult * tempCharge)
    
    def block(self):
        self.blockCharges = self.blockChargesOnBlock

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
            startCharge = self.chargeMult
            for enemy in game.enemies:
                self.chargeMult = startCharge
                self.attack(enemy, self.weapon.specMult)
        elif self.weapon.specType == "Pierce":
            print("This attack targets the next highest index as well.")
            startCharge = self.chargeMult
            target = game.getTarget(returnsIndex = True, totalTargets = 2)
            self.attack(game.enemies[target], self.weapon.specMult)
            if target < len(game.enemies) - 1:
                self.chargeMult = startCharge
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
            target.blockPower /= 4
            target.blockCharges = 1