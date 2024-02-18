

class Consumable():
    name = ""
    charges = -1
    maxCharges = -1

    def __init__(self, name) -> None:
        self.name = name
        match name:
            case "Heal Potion":
                self.maxCharges = 1
            case "Throwing Daggers":
                self.maxCharges = 2
            case "Tomahawk":
                self.maxCharges = 2
        self.charges = self.maxCharges
    
    def use(self, game):
        if self.charges != 0:
            plr = game.player
            match self.name:
                case "Heal Potion":
                    plr.hp = plr.maxHealth
                case "Strength Potion":
                    plr.bStr += 2
                case "Dexterity Potion":
                    plr.bDex += 2
                case "Constitution Potion":
                    plr.bCon += 2
                case "Charge Potion":
                    plr.chargePower += 0.25
                    plr.chargeMult += 3 * plr.chargePower
                case "Block Potion":
                    plr.blockChargesOnBlock += 1
                    plr.blockCharges += 2 * plr.blockChargesOnBlock
                    plr.baseBlock += 1
                    plr.blockPower += 1
                case "Throwing Daggers":
                    target = game.getTarget()
                    target.takeDamage(5)
                    target.chargeMult /= 2
                case "Tomahawk":
                    target = game.getTarget()
                    target.takeDamage(5)
                    target.tempDamageModifier += 0.3
                case _:
                    pass
            if self.charges < 0:
                plr.inventory.remove(self)
            else:
                self.charges -= 1
            
    def getStatDisplay(self):
        match self.name:
            case "Heal Potion":
                return "Heals you to full, 1 charge"
            case "Strength Potion":
                return "Permanently increases strength by 2"
            case "Dexterity Potion":
                return "Permanently increases dexterity by 2"
            case "Constitution Potion":
                return "Permanently increases constitution by 2"
            case "Charge Potion":
                return "Permanently improves the damage boost of charge, immediately gives a large charge"
            case "Block Potion":
                return "Permanently increases block charges on block, immediately gives a significant amount of block charges"
            case "Throwing Daggers":
                return "Small damage to an enemy, weakens their next attack, 2 charges"
            case "Tomahawk":
                return "Small damage to an enemy, makes them vulnerable to your next attack, 2 charges"