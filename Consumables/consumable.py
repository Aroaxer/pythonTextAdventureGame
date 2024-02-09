

class Consumable():
    name = ""

    def __init__(self, name) -> None:
        self.name = name
    
    def use(self, game):
        match self.name:
            case "Heal":
                game.player.hp = game.player.maxHp
            case "Kill":
                game.enemies = []
            case "Strength Boost":
                game.player.bStr += 2
            case "Dexterity Boost":
                game.player.bDex += 2
            case "Constitution Boost":
                game.player.bCon += 2
            case "Charge Boost":
                game.player.chargePower += 0.5
            case "Block Boost":
                game.player.baseBlock += 1
                game.player.blockPower += 1
        game.player.inventory.remove(self)
            
consumables = [
    "Heal",
    "Kill",
    "Strength Boost",
    "Dexterity Boost",
    "Constitution Boost",
    "Charge Boost",
    "Block Boost"
]