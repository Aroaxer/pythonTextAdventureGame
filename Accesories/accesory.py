

class Accesory():
    name = ""
    canUse = False
    useDesc = ""
    strMod = 1
    dexMod = 1
    conMod = 1
    chrMod = 1
    blkMod = 1
    hasPassive = False
    passiveDesc = ""

    def __init__(self, name) -> None:
        self.name = name

        match name:
            case "Iron Gauntlets":
                self.chrMod = 1.8
                self.dexMod = 0.9
                self.strMod = 0.9
                self.conMod = 1.2
            case "Iron Shield":
                self.blkMod = 1.5
                self.dexMod = 0.8
                self.strMod = 0.9
                self.conMod = 1.2
            case "Crystal Necklace":
                self.canUse = True
                self.useDesc = "Weakens all enemies to your next attack."
                self.conMod = 0.8
            case "Steel Gauntlets":
                self.chrMod = 2.1
                self.strMod = 1.2
                self.conMod = 1.2
            case "Steelsilk Gloves":
                self.chrMod = 2.1
                self.dexMod = 1.2
                self.conMod = 1.2
            case "Tower Shield":
                self.blkMod = 2
                self.conMod = 1.4
                self.dexMod = 0.6
            case "Ritual Dagger":
                self.canUse = True
                self.useDesc = "If you get a kill, your stats increase. Finisher"
                self.strMod = 1.2
                self.dexMod = 1.2
                self.conMod = 0.6
                self.blkMod = 0
            case "Animated Shield":
                self.hasPassive = True
                self.passiveDesc = "Gives you a small amount of block charges every turn"
                self.blkMod = 1.5
            case "Energy Accumulator":
                self.hasPassive = True
                self.passiveDesc = "Gives you a small amount of charge every turn"
                self.chrMod = 1.5
            case "Runic Sheath":
                self.canUse = True
                self.useDesc = "Charges twice as much but makes you vulnerable to the next attack"
                self.strMod = 2
                self.chrMod = 2
                self.dexMod = 0.8
            case "Runic Quiver":
                self.canUse = True
                self.useDesc = "Attacks every enemy for full damage"
                self.dexMod = 2
                self.strMod = 0
            case "Runic Shield":
                self.hasPassive = True
                self.canUse = True
                self.useDesc = "Blocks while giving a small amount of charge"
                self.passiveDesc = "Gives you a moderate amount of block charges every turn"
                self.blkMod = 2
                self.conMod = 1.2
            case "Runic Accumulator":
                self.hasPassive = True
                self.passiveDesc = "Gives you a significant amount of charge every turn"
                self.chrMod = 2
                self.strMod = 1.2
                self.dexMod = 1.2
            case "Runic Amulet":
                self.hasPassive = True
                self.canUse = True
                self.useDesc = "Weakens all enemies to your next attack."
                self.passiveDesc = "Weakens enemies slightly every turn"
                self.strMod = 1.4
                self.dexMod = 1.4
                self.conMod = 0.8
            case "Sacrificial Blade":
                self.canUse = True
                self.useDesc = "If you get a kill, your stats increase. Does 20 percent extra damage. Finisher"
                self.strMod = 1.5
                self.dexMod = 1.5
                self.conMod = 0.6
                self.blkMod = 0.5
            case "Recovery Jewel":
                self.canUse = True
                self.useDesc = "Partially heals you"
            case "Regenerative Circlet":
                self.canUse = True
                self.hasPassive = True
                self.useDesc = "Partially heals you"
                self.passiveDesc = "Heals a small part of your health every turn"
                self.conMod = 1.5
            case _:
                pass


    def isAcc(self):
        pass # Used when collecting an item to check if it is an accesory


    def use(self, game):
        if self.canUse:
            plr = game.player
            match self.name:
                case "Crystal Necklace":
                    for enemy in game.enemies:
                        enemy.tempDamageModifier += 0.4
                case "Ritual Dagger":
                    target = game.getTarget()
                    enemPercent = target.hp / target.maxHealth
                    plr.attack(target, (1 - enemPercent) / 30)
                    if target.hp <= 0:
                        plr.bCon += 0.1
                        plr.bStr += 0.1
                        plr.bDex += 0.1
                        plr.hp = plr.maxHealth
                        game.nextOutput += "You absorb some of the enemy's power!\n"
                case "Runic Sheath":
                    plr.chargeMult += (plr.chargePower * 2) * self.chrMod
                    plr.tempDamageModifier += 1
                case "Runic Quiver":
                    startCharge = plr.chargeMult
                    for enemy in game.enemies:
                        plr.chargeMult = startCharge
                        plr.attack(enemy, 0.8)
                case "Runic Shield":
                    plr.blockCharges += plr.blockChargesOnBlock * self.blkMod
                    plr.chargeMult += (plr.chargePower / 2) * self.chrMod
                case "Runic Amulet":
                    for enemy in game.enemies:
                        enemy.tempDamageModifier += 0.6
                case "Sacrificial Blade":
                    target = game.getTarget()
                    enemPercent = target.hp / target.maxHealth
                    plr.attack(target, ((1 - enemPercent) / 20))
                    if target.hp <= 0:
                        plr.bCon += 0.25
                        plr.bStr += 0.25
                        plr.bDex += 0.25
                        plr.hp = plr.maxHealth
                        game.nextOutput += "You absorb some of the enemy's power!\n"
                case "Recovery Jewel" | "Regerative Circlet":
                    plr.hp += plr.maxHealth / 2
                    if plr.hp > plr.maxHealth:
                        plr.hp = plr.maxHealth
            return True
        return False


    def passive(self, game):
        if self.hasPassive:
            plr = game.player
            match self.name:
                case "Animated Shield":
                    plr.blockCharges += round(plr.blockChargesOnBlock / 3) * self.blkMod
                case "Energy Accumulator":
                    plr.chargeMult += (plr.chargePower / 2) * self.chrMod
                case "Runic Shield":
                    plr.blockCharges += round(plr.blockChargesOnBlock * (2 / 3)) * self.blkMod
                case "Runic Accumulator":
                    plr.chargeMult += plr.chargePower * self.chrMod
                case "Runic Amulet":
                    for enemy in game.enemies:
                        enemy.tempDamageModifier += 0.2
                case "Regenerative Circlet":
                    plr.hp += plr.maxHealth / 10
                    if plr.hp > plr.maxHealth:
                        plr.hp = plr.maxHealth
            return True
        return False
    
    def getStatDisplay(self):
        return (str(self.name) + ":\n" + (("Active: " + str(self.useDesc)) if self.canUse else "Can't be used") + "\n"
                       + (("Passive: " + str(self.passiveDesc)) if self.hasPassive else "Has no passive") + "\n"
                       + str(self.strMod) + "x str\n" + str(self.dexMod) + "x dex\n" + str(self.conMod) + "x con\n" + str(self.blkMod) + "x block charges\n" + str(self.chrMod) + "x charge")
