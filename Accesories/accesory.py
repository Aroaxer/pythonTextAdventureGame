

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
            case "Old Amulet":
                pass
            case "Iron Gauntlets":
                self.statMods["charge"] = 1.5
            case "Iron Shield":
                self.statMods["block"] = 1.5
            case "Crystal Necklace":
                self.canUse = True
                self.useDesc = "Weakens all enemies to your next attack."
                self.statMods["con"] = 0.8
            case "Steel Gauntlets":
                self.statMods["charge"] = 1.5
                self.statMods["str"] = 1.2
            case "Steelsilk Gloves":
                self.statMods["charge"] = 1.5
                self.statMods["dex"] = 1.2
            case "Tower Shield":
                self.statMods["block"] = 2
                self.statMods["con"] = 1.2
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
            


    def use(self, game):
        if self.canUse:
            match self.name:
                case "Crystal Necklace":
                    for enemy in game.enemies:
                        enemy.blockCharges = 1
                        enemy.blockPower /= 4
                case "Ritual Dagger":
                    target = game.getTarget()
                    game.player.attack(target)
                    if target.hp <= 0:
                        game.player.bCon += 0.5
                        game.player.bStr += 0.5
                        game.player.bDex += 0.5
                        game.player.hp = game.player.maxHealth
                        game.nextOutput += "You absorb some of the enemy's power!\n"

    def passive(self, game):
        if self.hasPassive:
            match self.name:
                case "Animated Shield":
                    game.player.blockCharges += round(game.player.blockChargesOnBlock / 3)
                case "Energy Accumulator":
                    game.player.chargeMult += game.player.chargePower / 2
