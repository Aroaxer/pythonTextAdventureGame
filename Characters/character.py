import random

import premades as pre

class Character():
    # Stats
    bStr = 10
    bDex = 10
    bCon = 10

    level = 1
    hpPerLevel = 5


    isEnemy = True
    def getMaxHp(self): 
        levelHp = self.hpPerLevel + self.getMod("c")
        if self.isEnemy:
            levelHp *= 3
        return ((1 if self.isEnemy else 2) + (self.level / 5)) * levelHp
    maxHealth = property(fget = getMaxHp)
    hp = 0

    weapon = None
    armor = None
    accesory = None

    baseBlock = 3
    blockPower = baseBlock
    blockCharges = 0
    blockChargesOnBlock = 3

    tempDamageModifier = 1

    chargeMult = 1
    chargePower = 0.5

    # Methods
    def __init__(self, str, con , dex, hpPerLevel, gearSet = None, isEnemy = True) -> None:
        self.accesory = pre.oldAmulet

        self.isEnemy = isEnemy

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

    def takeDamage(self, amt):
        tempHp = self.hp
        self.hp -= round((self.armor.reduceDamage(amt, self) / ((self.blockPower * self.accesory.blkMod) if self.blockCharges > 0 else 1)) * self.tempDamageModifier)
        if self.hp > tempHp: self.hp = tempHp
        self.blockPower = self.baseBlock
        self.tempDamageModifier = 1
        self.blockCharges -= (1 if self.blockCharges > 0 else 0)
        return (self.hp <= 0)

    def attack(self, target, damageMult = 1):
        tempCharge = self.chargeMult
        self.chargeMult = 1
        return target.takeDamage(self.weapon.dealDamage(self) * damageMult * tempCharge * (1.75 if self.isEnemy else 1))
    
    def block(self):
        self.blockCharges = self.blockChargesOnBlock

    def charge(self):
        self.chargeMult += self.chargePower * self.accesory.chrMod

    def getMod(self, stat): 
        match stat:
            case "s":
                return round(((self.bStr * self.accesory.strMod) - 10) / 2)
            case "d":
                return round(((self.bDex * self.accesory.dexMod) - 10) / 2)
            case "c":
                return round(((self.bCon * self.accesory.conMod) - 10) / 2)

    def useSpecial(self, game):
        wep = self.weapon
        shouldReset = False
        if wep.multi < 0: # Target every enemy
            wep.multi = len(game.enemies)
            shouldReset = True

        target = game.getTarget(returnsIndex = True, totalTargets = wep.multi)
        initTarget = target

        if target == "cancel":
            return "cancel"

        # Target as many enemies as the weapon should
        startCharge = self.chargeMult
        while target < wep.multi + initTarget and target < len(game.enemies):
            trg = game.enemies[target]
            self.chargeMult = startCharge

            if wep.specType == "Oneshot":
                enemPercent = (trg.hp / trg.maxHealth) * 100
                wep.specMult = enemPercent / 30
            elif wep.specType == "Finisher":
                enemPercent = (trg.hp / trg.maxHealth) * 100
                wep.specMult = (100 - enemPercent) / 25
            
            self.attack(trg, wep.specMult)

            if wep.specType == "Weakening":
                trg.chargeMult /= 2
            elif wep.specType == "Fracturing":  
                trg.tempDamageModifier += 1

            target += 1

        if shouldReset: # Reset multi back to negative
            wep.multi = -1