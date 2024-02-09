

class Consumable():
    name = ""

    def __init__(self, name) -> None:
        self.name = name
    
    def use(self, game):
        match self.name:
            case "Heal Potion":
                game.player.hp = game.player.maxHp
            case "Strength Potion":
                game.player.bStr += 2
            case "Dexterity Potion":
                game.player.bDex += 2
            case "Constitution Potion":
                game.player.bCon += 2
            case "Charge Potion":
                game.player.chargePower += 0.5
                game.player.chargeMult += 3 * game.player.chargePower
            case "Block Potion":
                game.player.blockChargesOnBlock += 1
                game.player.blockCharges += game.player.blockChargesOnBlock
                game.player.baseBlock += 1
                game.player.blockPower += 1
        game.player.inventory.remove(self)
            
consumables = [
    "Heal Potion",
    "Strength Potion",
    "Dexterity Potion",
    "Constitution Potion",
    "Charge Potion",
    "Block Potion"
]