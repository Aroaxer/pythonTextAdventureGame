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
    recharge = ""

    # Methods
    def __init__(self, name, defense, flatReduction, weight):
        self.name = name
        self.defense = defense
        self.flatReduction = flatReduction
        self.armWeight = weight

        self.recharge = "Turn"

        match self.name:
            case "Spiked Mail":
                self.hasReactive = True
                self.reactiveDesc = "Damages attackers"
            case "Battlerager Mail":
                self.hasReactive = True
                self.reactiveDesc = "Damages attackers and charges your attack"
            case "Ragnarok Mail":
                self.hasReactive = True
                self.reactiveDesc = "Damages attackers and charges your attack"
            case "Stony Plate":
                self.hasPassive = True
                self.passiveDesc = "Gains a small amount of block charges"
            case "Overgrown Plate":
                self.hasPassive = True
                self.passiveDesc = "Gains a moderate amount of block charges"
            case "Yggdrasil Plate":
                self.hasPassive = True
                self.passiveDesc = "Gains a notable amount of block charges"
                self.hasReactive = True
                self.baseReactiveCharges = 1
                self.reactiveDesc = "You survive one hit that would kill you at one hp each turn"
            case "Shadowed Cloak":
                self.hasReactive = True
                self.baseReactiveCharges = 1
                self.reactiveDesc = "Completely block the first attack each turn"
            case "Midnight Cloak":
                self.hasReactive = True
                self.baseReactiveCharges = 2
                self.reactiveDesc = "Completely block the first two attacks each turn"
            case "Purenight Cloak":
                self.hasReactive = True
                self.baseReactiveCharges = 2
                self.reactiveDesc = "Completely block the first two strong / deadly attacks each turn"
            case "Holy Plate":
                self.hasReactive = True
                self.reactiveDesc = "Slightly damages all attackers"
            case "Sacred Plate":
                self.hasReactive = True
                self.reactiveDesc = "Slightly damages all attackers"
            case "Heavenly Plate":
                self.hasReactive = True
                self.reactiveDesc = "Slightly damages all attackers, you heal to full on dying once per fight"
                self.baseReactiveCharges = 1
                self.recharge = "Encounter"
            case "Coat of Knives":
                self.hasPassive = True
                self.passiveDesc = "Attacks a random enemy for a quarter damage, doesn't use charge"
            case "Cloak of Daggers":
                self.hasPassive = True
                self.passiveDesc = "Attacks 2 random enemies for a quarter damage, doesn't use charge"
            case "Cloak of Blades" :
                self.hasPassive = True
                self.passiveDesc = "Attacks 2 random enemies for a quarter damage, doesn't use charge"
                self.hasReactive = True
                self.reactiveDesc = "Attacks enemies that hit you for a sixteenth damage, doesn't use charge"
            case "Explorer's Leathers":
                self.hasPassive = True
                self.passiveDesc = "Slightly heals you"
            case "Dungeoneer's Mail":
                self.hasPassive = True
                self.passiveDesc = "Slightly heals you"
                self.hasReactive = True
                self.baseReactiveCharges = 2
                self.reactiveDesc = "Heals you when on low health twice per fight"
                self.recharge = "Encounter"
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
                    plr.blockCharges += (plr.blockChargesOnBlock / 3) * acc.blkMod
                case "Overgrown Plate":
                    plr.blockCharges += (plr.blockChargesOnBlock * (2 / 3)) * acc.blMod
                case "Yggdrasil Plate":
                    plr.blockCharges += plr.blockChargesOnBlock * acc.blkMod
                case "Coat of Knives":
                    enem = game.enemies[random.randint(0, len(game.enemies) - 1)]
                    startCharge = plr.chargeMult
                    plr.attack(enem, 0.25)
                    plr.chargeMult = startCharge
                case "Cloak of Daggers" | "Cloak of Blades":
                    enem = game.enemies[random.randint(0, len(game.enemies) - 1)]
                    startCharge = plr.chargeMult
                    plr.attack(enem, 0.25)
                    plr.chargeMult = startCharge
                    enem = game.enemies[random.randint(0, len(game.enemies) - 1)]
                    plr.attack(enem, 0.25)
                    plr.chargeMult = startCharge
                case "Explorer's Leathers" | "Dungeoneer's Mail":
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
                case "Yggdrasil Plate":
                    if plr.hp <= 0:
                        plr.hp = 1
                    else:
                        self.reactiveCharges += 1
                case "Spiked Mail":
                    attacker.takeDamage(5)
                case "Battlerager Mail":
                    attacker.takeDamage(10)
                    plr.chargePow += (plr.chargeMult / 4) * acc.chrMod
                case "Ragnarok Mail":
                    attacker.takeDamage(15)
                    plr.chargePow += (plr.chargeMult / 3) * acc.chrMod
                case "Shadowed Cloak":
                    plr.hp += dmg
                case "Midnight Cloak":
                    plr.hp += dmg
                case "Purenight Cloak":
                    if dmg >= plr.maxHealth / 5 or plr.hp <= 0:
                        plr.hp += dmg
                    else:
                        self.reactiveCharges += 1
                case "Cloak of Blades":
                    startCharge = plr.chargeMult
                    plr.attack(attacker, 0.0625)
                    plr.chargeMult = startCharge
                case "Holy Plate":
                    for enem in game.enemies:
                        enem.hp -= 1
                case "Sacred Plate":
                    for enem in game.enemies:
                        enem.hp -= 2
                case "Heavenly Plate":
                    for enem in game.enemies:
                        enem.hp -= 3
                    if plr.hp <= 0:
                        plr.hp = plr.maxHealth
                    else:
                        self.reactiveCharges += 1
                case "Dungeoneer's Mail":
                    if plr.hp <= plr.maxHealth / 3:
                        plr.hp += plr.maxHealth / 3
                    else:
                        self.reactiveCharges += 1
                case "Adaptive Mail":
                    plr.tempDamageModifier /= (dmg / 7)
                    
            self.reactiveCharges -= 1 if self.reactiveCharges > 0 else 0
            return True
        return False