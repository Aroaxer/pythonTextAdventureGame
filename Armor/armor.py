import math
import random

class Armor():
    # Stats
    name = ""
    defense = 0
    flatReduction = 0

    armWeight = "Light"

    hasPassive = False
    passiveDesc = ""

    hasReactive = False
    reactiveDesc = ""
    reactiveCharges = -1
    baseReactiveCharges = -1

    # Methods
    def __init__(self, name, defense, flatReduction, weight):
        self.name = name
        self.defense = defense
        self.flatReduction = flatReduction
        self.armWeight = weight

        match self.name:
            case "Spiked Mail":
                self.hasReactive = True
                self.reactiveDesc = "Damages attackers"
            case "Battlerager Mail":
                self.hasReactive = True
                self.reactiveDesc = "Damages attackers and charges your attack"
            case "Stony Plate":
                self.hasPassive = True
                self.passiveDesc = "Gains a small amount of block charges"
            case "Overgrown Plate":
                self.hasPassive = True
                self.passiveDesc = "Gains a moderate amount of block charges"
            case "Shadowed Cloak":
                self.hasReactive = True
                self.baseReactiveCharges = 1
                self.reactiveDesc = "Completely block the first attack each turn"
            case "Midnight Cloak":
                self.hasReactive = True
                self.baseReactiveCharges = 3
                self.reactiveDesc = "Completely block the first three attacks each turn"
            case "Holy Plate":
                self.hasReactive = True
                self.reactiveDesc = "Slightly damages all attackers"
            case "Sacred Plate":
                self.hasReactive = True
                self.reactiveDesc = "Slightly damages all attackers"
            case "Coat of Knives":
                self.hasPassive = True
                self.passiveDesc = "Attacks a random enemy for a quarter damage, doesn't use charge"
            case "Cloak of Blades":
                self.hasPassive = True
                self.passiveDesc = "Attacks 2 random enemies for a quarter damage, doesn't use charge"
            case "Explorer's Leathers":
                self.hasPassive = True
                self.passiveDesc = "Slightly heals you"
            case "Adaptive Mail":
                self.hasReactive = True
                self.reactiveDesc = "Reduces damage taken from next attack proportional to damage taken"
            
        
        self.reactiveCharges = self.baseReactiveCharges

    def reduceDamage(self, damage, wearer):
        if self.armWeight != "Light":
            return math.ceil((damage * (1 - (self.defense / 100))) - self.flatReduction)
        else:
            return math.ceil((damage * (1 - (self.defense / 100))) - self.flatReduction - math.ceil(wearer.getMod("d") / 3))
        
    def getStatDisplay(self):
        return (f"{self.name}: {self.defense} defense, {self.flatReduction} flat reduction\n" + 
                (f"Passive: {self.passiveDesc}" if self.hasPassive else "No passive") + "\n" + 
                (f"Reactive: {self.reactiveDesc}" if self.hasReactive else "No Reactive"))
    
    def passive(self, game):
        if self.hasPassive:
            plr = game.player
            acc = plr.accesory
            match self.name:
                case "Stony Plate":
                    plr.blockCharges += (plr.blockChargesOnBlock / 3) * acc.blkMult
                case "Overgrown Plate":
                    plr.blockCharges += (plr.blockChargesOnBlock * (2 / 3)) * acc.blkMult
                case "Coat of Knives":
                    enem = game.enemies[random.randint(0, len(game.enemies) - 1)]
                    startCharge = plr.chargeMult
                    plr.attack(enem, 0.25)
                    plr.chargeMult = startCharge
                case "Cloak of Blades":
                    enem = game.enemies[random.randint(0, len(game.enemies) - 1)]
                    startCharge = plr.chargeMult
                    plr.attack(enem, 0.25)
                    plr.chargeMult = startCharge
                    enem = game.enemies[random.randint(0, len(game.enemies) - 1)]
                    plr.attack(enem, 0.25)
                    plr.chargeMult = startCharge
                case "Explorer's Leathers":
                    plr.hp += plr.maxHealth / 10
                    if plr.hp > plr.maxHealth:
                        plr.hp = plr.maxHealth
            
            return True
        return False

    def reactive(self, game, attacker, dmg):
        if self.hasReactive and self.reactiveCharges != 0:
            plr = game.player
            acc = plr.accesory
            match self.name:
                case "Spiked Mail":
                    attacker.takeDamage(5)
                case "Battlerager Mail":
                    attacker.takeDamage(10)
                    plr.chargePow += (plr.chargeMult / 4) * acc.chrMult
                case "Shadowed Cloak":
                    plr.hp += dmg
                case "Midnight Cloak":
                    plr.hp += dmg
                case "Holy Plate":
                    for enem in game.enemies:
                        enem.hp -= 1
                case "Sacred Plate":
                    for enem in game.enemies:
                        enem.hp -= 2
                case "Adaptive Mail":
                    plr.tempDamageModifier /= dmg
                    
            self.reactiveCharges -= 1 if self.reactiveCharges > 0 else 0
            return True
        return False