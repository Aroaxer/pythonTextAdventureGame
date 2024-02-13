import random

from Characters.player import Player
from Consumables.consumable import Consumable
from Stages.stage import Stage
import premades as pre

class Game():
    player = None
    enemies = []

    possibleLoot = []

    nextOutput = ""

    stage = 0
    difficulty = 0
    encountersComplete = 0

    extraSettings = {
        "printProjDamage" : False,
        "printDmgOnAction" : False,
        "displayOwnDamageReduction" : False
    }

    def __init__(self) -> None:
        self.beginGame()

    def setupPlayer(self):
        succeeded = False
        while not succeeded:
            self.emptyTerminal()
            if self.extraSettings["printProjDamage"]:
                print("Will automatically project damage")
            if self.extraSettings["printDmgOnAction"]:
                print("Will display action damage")
            if self.extraSettings["displayOwnDamageReduction"]:
                print("Will display own dr")
            print("\n\n")
            try:
                choice = input("What class would you like to play as?\n" +
                            "Warrior - 14 str 16 con 12 dex\n" +
                            "Knight - 16 str 14 con 8 dex\n" +
                            "Ranger - 10 str 16 con 14 dex\n" +
                            "Rogue - 8 str 12 con 16 dex\n").lower()
                match choice:
                    case "project damage":
                        self.extraSettings["printProjDamage"] = not self.extraSettings["printProjDamage"]
                    case "show action damage":
                        self.extraSettings["printDmgOnAction"] = not self.extraSettings["printDmgOnAction"]
                    case "show own dr":
                        self.extraSettings["displayOwnDamageReduction"] = not self.extraSettings["displayOwnDamageReduction"]
                    case _:
                        self.player = Player(pre.types[choice])
                        succeeded = True
            except Exception:
                pass

    def beginGame(self):
        self.emptyTerminal()
        self.nextOutput = ""

        self.possibleLoot = []
        self.possibleLoot.extend(pre.weaponTier[0])
        self.possibleLoot.extend(pre.weaponTier[1])
        self.possibleLoot.extend(pre.armorTier[0])

        self.setStage(pre.stages["Forest"])
        self.setupPlayer()
        self.difficulty = 1
        self.encountersComplete = 0

        self.enemies = self.stage.getEncounter(self.difficulty)

        self.mainLoop()

    def mainLoop(self):
        self.emptyTerminal()

        print(self.nextOutput + "\n\n")
        self.nextOutput = ""

        if len(self.enemies) == 0:
            self.completeEncounter()

        self.printInfo()
        plResult = self.takePlayerInput()

        tempEnems = []
        if plResult != "No Move":
            for enemy in self.enemies:
                if round(enemy.hp) <= 0:
                    self.nextOutput += "You killed the " + enemy.name + "!\n"
                else:
                    enemy.takeAction(self)
                    tempEnems.append(enemy)
            self.enemies = tempEnems

        if self.player.hp <= 0:
            self.emptyTerminal()
            print("Game Over\n\n\n")
            return False
        
        tempLevel = self.player.level
        self.player.checkLevel()
        if tempLevel < self.player.level:
            self.nextOutput += "\nYou gained " + ((str(self.player.level - tempLevel) + " levels") if (self.player.level - tempLevel) != 1 else ("a level")) + "!\n"



        return self.mainLoop() # Loops
    
    def emptyTerminal(self):
        cycles = 0
        while cycles < 15:
            print("\n\n\n")
            cycles += 1
    
    def printInfo(self):
        print("Player (" + self.player.type.name + "): " + str(round(self.player.hp)) + " health, "
               + self.player.weapon.name + ", " + self.player.armor.name
                + (", " + (str(self.player.blockCharges) + " block charges left") if self.player.blockCharges > 0 else ""))
        if self.extraSettings["displayOwnDamageReduction"]:
            print("Damage Reduction: " + str(self.player.armor.defense) + " percent, " + str(self.player.armor.flatReduction) + " flat")
        for enemy in self.enemies:
            projection = self.projectDamage(enemy)
            print(enemy.name + ": " + str(round(enemy.hp)) + " health" + ("" if not self.extraSettings["printProjDamage"] else 
                                                                          ", " + str(projection[0]) + " damage, " + str(projection[1]) + " special"))
        
    def setStage(self, stage):
        self.stage = Stage(stage[0], stage[1])
    
    def completeEncounter(self):
        self.player.exp += self.player.hp
        self.player.hp += self.player.maxHealth / 2
        if self.player.hp > self.player.maxHealth: 
            self.player.hp = self.player.maxHealth

        print("You defeated the enemies!\n\n")
        self.encountersComplete += 1

        if (self.encountersComplete + 1) % 5 == 0:
            self.difficulty += 1
            self.tryLoot()

        if self.encountersComplete % 10 == 0:
            match self.stage.index:
                case 0: # Forest
                    self.setStage(pre.stages["Caves"])
                    self.nextOutput += "\nYou advance to the Caves!\n"

                    self.possibleLoot = self.removeMatches(self.possibleLoot, pre.weaponTier[0])
                
                    self.possibleLoot.extend(pre.weaponTier[2])
                    self.possibleLoot.extend(pre.armorTier[1])
                case 1: # Caves
                    self.setStage(pre.stages["Castle"])
                    self.nextOutput += "\nYou advance to the Castle!\n"
                
                    self.possibleLoot = self.removeMatches(self.possibleLoot, pre.weaponTier[1])
                    self.possibleLoot = self.removeMatches(self.possibleLoot, pre.armorTier[0])

                    self.possibleLoot.extend(pre.weaponTier[3])
                    self.possibleLoot.extend(pre.armorTier[2])
                case 2: # Castle
                    self.setStage(pre.stages["Underworld"])
                    self.nextOutput += "\nYou advance to the Underworld!\n"

                    self.possibleLoot = self.removeMatches(self.possibleLoot, pre.weaponTier[2])
                    self.possibleLoot = self.removeMatches(self.possibleLoot, pre.armorTier[1])

                    self.possibleLoot.extend(pre.weaponTier[4])
                    self.possibleLoot.extend(pre.armorTier[3])
                case 3: # Underworld
                    self.setStage(pre.stages["Astral"])
                    self.nextOutput += "\nYou advance to the Astral Plane!\n"
                        
                    self.possibleLoot = self.removeMatches(self.possibleLoot, pre.weaponTier[3])
                    self.possibleLoot = self.removeMatches(self.possibleLoot, pre.weaponTier[2])
                case 4: # Astral
                    self.setStage(pre.stages["Infinite"])
                    self.nextOutput += "\nYou advance to the Infinite Realm!\n"
                case 5: # Infinite
                    self.difficulty += round(self.difficulty / 10)
                    self.nextOutput += "\nThe enemies grow more dangerous!\n"
                    
        # Get next encounter
        if (self.encountersComplete + 1) % 10 != 0 or self.stage.boss == None:
            self.enemies = self.stage.getEncounter(self.difficulty)
        else: # Boss
            self.enemies = [self.stage.boss]

    def removeMatches(self, list, remList):
        tempList = []
        for entry in list:
            if not entry in remList:
                tempList.append(entry)
        return tempList

    def tryLoot(self):
        loot = []
        cycles = 0
        while cycles < self.difficulty + 5:
            loot.append(self.getRandomLoot())
            cycles += 1
        print("You opened a chest and found some loot!\nEnter an index starting at 1 to choose\nEnter 'skip' to skip\n")
        cycles = 1
        for item in loot:
            print(str(cycles) + ": " + item.name)
            cycles += 1
        choice = None
        didSkip = False
        while choice == None:
            try:
                choice = input("\n")
                if choice.lower() != "skip":
                    choice = int(choice)
                else:
                    didSkip = True
                    break
                if choice < 1 or choice > len(loot):
                    raise ValueError
                if not didSkip:
                    self.player.getItem(loot[choice - 1])
            except ValueError:
                choice = None
                print("Bad Input")
                

    def getRandomLoot(self):
        roll = random.randint(1,100)
        if roll > (30 if (self.stage.index < 5) else 90):
            return self.possibleLoot[random.randint(0, len(self.possibleLoot) - 1)]
        else:
            return Consumable(pre.consumables[random.randint(0, len(pre.consumables) - 1)])

    def takePlayerInput(self):
        pIn = input("What would you like to do?\n")
        return self.handlePlayerInput(pIn)

    def handlePlayerInput(self, pIn):
        match (pIn).lower():
            case "attack" | "a":
                target = self.getTarget()
                tempHp = target.hp
                self.player.attack(target)
                if not self.extraSettings["printDmgOnAction"]:
                    self.nextOutput += "You attacked the " + target.name + "!\n"
                else:
                    self.nextOutput += "You attacked the " + target.name + " for " + str(tempHp - target.hp) + " damage!\n"
                return "Attack"
            case "block" | "b":
                self.player.block()
                self.nextOutput += "You blocked!\n"
                return "Block"
            case "charge" | "c":
                self.player.charge()
                self.nextOutput += "You charged your attack!\n"
                return "Charge"
            case "special" | "s":
                self.player.useSpecial(self)
                self.nextOutput += "You used your weapon's special!\n"
                return "Special"
            case "use item" | "use" | "u":
                print("Inventory:")
                counter = 1
                for item in self.player.inventory:
                    print(str(counter) + ": " + item.name)
                    counter += 1
                choice = input("Which item would you like to use?\nEnter an index starting at one\nEnter cancel to cancel\n")
                if choice.lower() != "cancel":
                    try:
                        self.player.inventory[int(choice) - 1].use(self)
                    except Exception:
                        self.nextOutput += "Couldn't find an item at that index\n\n"
                return "No Move"
            case "get stats" | "stats" | "see stats":
                self.nextOutput += ("\n" + str(self.player.bStr) + " Str\n" + str(self.player.bCon) + " Con\n"
                      + str(self.player.bDex) + " Dex\n\n")
                return "No Move"
            case "give up":
                self.player.hp = 0
                return "No Move"
            
            case _:
                return "No Move"
            
    def projectDamage(self, target):
        startHp = target.hp
        startCharge = self.player.chargeMult
        startBlock = target.blockPower
        startBCharges = target.blockCharges

        self.player.attack(target)
        damage = startHp - target.hp

        target.hp = startHp
        self.player.chargeMult = startCharge
        target.blockPower = startBlock
        target.blockCharges = startBCharges

        return [round(damage), round(damage * self.player.weapon.specMult)]
                
    def getTarget(self, targetsFriendly = False, returnsIndex = False, totalTargets = 1):
        if targetsFriendly:
            pass # May or may not end up using this
        else:
            try:
                if len(self.enemies) > totalTargets:
                    pIn = input("Which enemy would you like to target?\nEnter an index starting at 1\n")
                    
                    pIn = int(pIn)
                    if pIn > 0 and pIn <= len(self.enemies):
                        return (self.enemies[pIn - 1]) if not returnsIndex else (pIn - 1)
                    else: 
                        raise ValueError
                else:
                    raise ValueError
            except ValueError:
                return (self.enemies[0]) if not returnsIndex else 0


game = Game()

while True:
    game.emptyTerminal()
    print("Game Over\n")
    if game.stage.index > 0:
        print("Enter 'project damage' when choosing a class to see how much damage you will deal")
    if game.stage.index > 1:
        print("Enter 'show action damage' when choosing a class to see the damage each enemy does")
    if game.stage.index > 2:
        print("Enter 'show own dr' when choosing a class to see your own damage reduction")
    goOn = input("\nTry Again?\n")
    match goOn.lower(): # There are far too many of these, but its funny
        case "yes" | "y" | "ok" | "continue" | "try again" | "affirmative" | "yes please" | "indeed" | "certainly" | "sure" | "quite so" | "why not" | "lets do it" | "let's do it" | "go ahead" | "aight" | "k" | "kk" | "okie" | "okie dokie" | "hell yeah" | "yeah" | "most definitely" | "heck yeah" | "most certainly" | "i don't see why not" | "i dont see why not" | "i guess" | "i guess so" | "ig" | "for sure" | "yes sir" | "okie doki" | "bet" | "ight" | "yh" | "lets go" | "let's go" | "totally" | "mhm" | "mhm hm" | "mhm-hm" | "fo sho" | "try":
            game.beginGame()
        case "a" | "b" | "c" | "s" | "":
            pass
        case _:
            break