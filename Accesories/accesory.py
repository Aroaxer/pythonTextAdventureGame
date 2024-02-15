

class Accesory():
    name = ""
    canUse = False
    useDesc = ""
    statMods = {
        "str" : 1,
        "dex" : 1,
        "con" : 1,
        "charge" : 1,
        "block" : 1
    }
    hasPassive = False

    def __init__(self, name) -> None:
        self.name = name

        match name:
            case "Iron Gauntlets":
                self.statMods["charge"] = 1.5
                self.statMods["dex"] = 0.9
                self.statMods["str"] = 0.9
                self.statMods["con"] = 1.2
            case "Iron Shield":
                self.statMods["block"] = 1.5
                self.statMods["dex"] = 0.8
                self.statMods["str"] = 0.9
                self.statMods["con"] = 1.2
            case "Crystal Necklace":
                self.canUse = True
                self.useDesc = "Weakens all enemies to your next attack."
                self.statMods["con"] = 0.8
            case "Steel Gauntlets":
                self.statMods["charge"] = 1.5
                self.statMods["str"] = 1.2
                self.statMods["con"] = 1.2
            case "Steelsilk Gloves":
                self.statMods["charge"] = 1.5
                self.statMods["dex"] = 1.2
                self.statMods["con"] = 1.2
            case "Tower Shield":
                self.statMods["block"] = 2
                self.statMods["con"] = 1.4
                self.statMods["dex"] = 0.6
            case "Ritual Dagger":
                self.canUse = True
                self.useDesc = "If you get a kill, your stats increase."
                self.statMods["str"] = 2
                self.statMods["dex"] = 2
                self.statMods["con"] = 0.6
                self.statMods["block"] = 0
            case "Animated Shield":
                self.hasPassive = True
                self.statMods["block"] = 1.5
            case "Energy Accumulator":
                self.hasPassive = True
                self.statMods["charge"] = 1.5
            case "Runic Sheath":
                self.canUse = True
                self.statMods["str"] = 2
                self.statMods["charge"] = 2
                self.statMods["dex"] = 0.8
            case "Runic Quiver":
                self.canUse = True
                self.statMods["dex"] = 2
                self.statMods["str"] = 0
            case "Runic Shield":
                self.hasPassive = True
                self.canUse = True
                self.statMods["block"] = 2
                self.statMods["con"] = 1.2
            case "Runic Accumulator":
                self.hasPassive = True
                self.statMods["charge"] = 2
                self.statMods["str"] = 1.2
                self.statMods["dex"] = 1.2
            case "Runic Amulet":
                self.hasPassive = True
                self.canUse = True
                self.useDesc = "Weakens all enemies to your next attack."
                self.statMods["str"] = 1.4
                self.statMods["dex"] = 1.4
                self.statMods["con"] = 0.8
            case "Sacrificial Blade":
                self.canUse = True
                self.useDesc = "If you get a kill, your stats increase. Does 20 percent extra damage."
                self.statMods["str"] = 2.2
                self.statMods["dex"] = 2.2
                self.statMods["con"] = 0.6
                self.statMods["block"] = 0.5
            case "Recovery Jewel":
                self.canUse = True
                self.statMods["con"] = 2
            case "Regenerative Circlet":
                self.canUse = True
                self.hasPassive = True
                self.statMods["con"] = 3
            case _:
                pass


    def isAcc(self):
        pass # Used when collecting an item to check if it is an accesory


    def use(self, game):
        if self.canUse:
            match self.name:
                case "Crystal Necklace":
                    for enemy in game.enemies:
                        enemy.blockCharges = 1
                        enemy.blockPower /= 6
                case "Ritual Dagger":
                    print(self.useDesc)
                    target = game.getTarget()
                    game.player.attack(target)
                    if target.hp <= 0:
                        game.player.bCon += 0.5
                        game.player.bStr += 0.5
                        game.player.bDex += 0.5
                        game.player.hp = game.player.maxHealth
                        game.nextOutput += "You absorb some of the enemy's power!\n"
                case "Runic Sheath":
                    game.player.chargeMult += (game.player.chargePower * 2) * self.statMods["charge"]
                    game.player.blockPower /= 6
                    game.player.blockCharges = 1
                case "Runic Quiver":
                    startCharge = game.player.chargeMult
                    for enemy in game.enemies:
                        game.player.chargeMult = startCharge
                        game.player.attack(enemy, 1)
                case "Runic Shield":
                    game.player.blockCharges += game.player.blockChargesOnBlock
                    game.player.chargeMult += (game.player.chargePower / 2) * self.statMods["charge"]
                case "Runic Amulet":
                    for enemy in game.enemies:
                        enemy.blockCharges = 1
                        enemy.blockPower /= 4
                case "Sacrificial Blade":
                    print(self.useDesc)
                    target = game.getTarget()
                    game.player.attack(target, 1.2)
                    if target.hp <= 0:
                        game.player.bCon += 1
                        game.player.bStr += 1
                        game.player.bDex += 1
                        game.player.hp = game.player.maxHealth
                        game.nextOutput += "You absorb some of the enemy's power!\n"
                case "Recovery Jewel" | "Regerative Circlet":
                    game.player.hp = game.player.maxHealth
            return True
        return False


    def passive(self, game):
        if self.hasPassive:
            match self.name:
                case "Animated Shield":
                    game.player.blockCharges += round(game.player.blockChargesOnBlock / 3)
                case "Energy Accumulator":
                    game.player.chargeMult += (game.player.chargePower / 2) * self.statMods["charge"]
                case "Runic Shield":
                    game.player.blockCharges += round(game.player.blockChargesOnBlock * (2 / 3))
                case "Runic Accumulator":
                    game.player.chargeMult += game.player.chargePower * self.statMods["charge"]
                case "Runic Amulet":
                    for enemy in game.enemies:
                        enemy.blockCharges = 1
                        enemy.blockPower /= 1.5
                case "Regenerative Circlet":
                    game.player.hp += game.player.maxHealth / 3
                    if game.player.hp > game.player.maxHealth:
                        game.player.hp = game.player.maxHealth
            return True
        return False
