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
    enemiesKilled = 0

    extraSettings = {
        "printProjDamage" : False,
        "printDmgOnAction" : False,
        "displayOwnDamageReduction" : False,
        "displayRunStats" : False
    }

    def __init__(self) -> None:
        self.beginGame()

    def setupPlayer(self): # Sets up player and special settings
        succeeded = False
        while not succeeded:
            self.emptyTerminal()
            if self.extraSettings["printProjDamage"]:
                print("Will automatically project damage")
            if self.extraSettings["printDmgOnAction"]:
                print("Will display action damage")
            if self.extraSettings["displayOwnDamageReduction"]:
                print("Will display own dr")
            if self.extraSettings["displayRunStats"]:
                print("Will display run stats")
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
                    case "show run stats":
                        self.extraSettings["displayRunStats"] = not self.extraSettings["displayRunStats"]
                    case "show all":
                        self.extraSettings["printProjDamage"] = True
                        self.extraSettings["printDmgOnAction"] = True
                        self.extraSettings["displayOwnDamageReduction"] = True
                        self.extraSettings["displayRunStats"] = True
                    case _: # Chose class or invalid input
                        self.player = Player(pre.types[choice]) # Gives error with bad input
                        self.player.inventory = [Consumable("Heal Potion"), Consumable("Heal Potion")]
                        succeeded = True
            except Exception:
                pass # Input doesn't have something associated

    def beginGame(self):
        self.emptyTerminal()
        self.nextOutput = ""

        self.possibleLoot = [] # Initial loot
        self.possibleLoot.extend(pre.weaponTier[0])
        self.possibleLoot.extend(pre.weaponTier[1])
        self.possibleLoot.extend(pre.armorTier[0])
        self.possibleLoot.extend(pre.accTier[0])
        self.possibleLoot.extend(pre.accTier[1])

        self.setStage(pre.stages["Forest"])
        self.setupPlayer()
        self.difficulty = 1
        self.encountersComplete = 0

        self.enemies = self.stage.getEncounter(self.difficulty)

        self.mainLoop()

    def mainLoop(self): # Recurses to loop
        self.emptyTerminal()

        print(self.nextOutput + "\n\n")
        self.nextOutput = ""

        self.printInfo()
        plResult = self.takePlayerInput()

        tempEnems = []
        if plResult != "No Move": # Enemies take turns / die, trigger passives
            self.player.accesory.passive(self)
            self.player.armor.passive(self)
            for enemy in self.enemies:
                if round(enemy.hp) <= 0:
                    self.nextOutput += "You killed the " + enemy.name + "!\n"
                    self.enemiesKilled += 1
                else:
                    enemy.takeAction(self)
                    if round(enemy.hp) <= 0:
                        self.nextOutput += "You killed the " + enemy.name + "!\n"
                        self.enemiesKilled += 1
                    else:
                        tempEnems.append(enemy)
            self.enemies = tempEnems

        if self.player.hp <= 0:
            self.emptyTerminal()
            print("Game Over\n\n\n")
            return False # End loop
        
        if len(self.enemies) == 0:
            self.completeEncounter()

        tempLevel = self.player.level
        self.player.checkLevel() # Level up (maybe)
        if tempLevel < self.player.level:
            self.nextOutput += "\nYou gained " + ((str(self.player.level - tempLevel) + " levels") if (self.player.level - tempLevel) != 1 else ("a level")) + "!\n"



        return self.mainLoop() # Loops
    
    def emptyTerminal(self): # Prints 80 newlines
        cycles = 0
        while cycles < 20:
            print("\n\n\n")
            cycles += 1
    
    def printInfo(self): # Looks really complicated, just prints stats
        if self.extraSettings["displayRunStats"]:
            print(f"Level: {self.player.level}, Enemies Killed: {self.enemiesKilled}\n\n")
        plr = self.player
        print(f"Player ({plr.type.name}): {round(plr.hp)} health, {plr.weapon.name}, {plr.armor.name}, {plr.accesory.name}" + ((f", {plr.blockCharges} block charges left") if plr.blockCharges > 0 else ""))
        if self.extraSettings["displayOwnDamageReduction"]:
            print("Damage Reduction: " + str(plr.armor.defense) + " percent, " + str(plr.armor.flatReduction + (plr.getMod("d") if plr.armor.armWeight == "Light" else 0)) + " flat")
        for enemy in self.enemies:
            projection = self.projectDamage(enemy)
            print(enemy.name + ": " + str(round(enemy.hp)) + " health" + ("" if not self.extraSettings["printProjDamage"] else 
                                                                          ", You will deal: " + str(projection[0]) + " damage, " + str(projection[1]) + " special"))

    def setStage(self, stage):
        self.stage = Stage(stage[0], stage[1])
    
    def completeEncounter(self):
        self.player.exp += self.player.hp
        self.player.hp += self.player.maxHealth / 2
        if self.player.hp > self.player.maxHealth: 
            self.player.hp = self.player.maxHealth
        self.player.armor.reactiveCharges = self.player.armor.baseReactiveCharges
        for item in self.player.inventory:
            item.charges = item.maxCharges

        print("You defeated the enemies!\n\n")
        self.encountersComplete += 1

        if (self.encountersComplete + 1) % 5 == 0:
            self.difficulty += 1
            self.tryLoot()

        if self.encountersComplete % 10 == 0: # Just beat boss
            match self.stage.index:
                case 0: # Forest
                    self.setStage(pre.stages["Caves"])
                    self.nextOutput += "\nYou advance to the Caves!\n"

                    self.possibleLoot = self.removeMatches(self.possibleLoot, pre.weaponTier[0])
                    self.possibleLoot = self.removeMatches(self.possibleLoot, pre.accTier[0])
                
                    self.possibleLoot.extend(pre.weaponTier[2])
                    self.possibleLoot.extend(pre.armorTier[1])
                    self.possibleLoot.extend(pre.accTier[2])
                case 1: # Caves
                    self.setStage(pre.stages["Castle"])
                    self.nextOutput += "\nYou advance to the Castle!\n"
                
                    self.possibleLoot = self.removeMatches(self.possibleLoot, pre.weaponTier[1])
                    self.possibleLoot = self.removeMatches(self.possibleLoot, pre.armorTier[0])
                    self.possibleLoot = self.removeMatches(self.possibleLoot, pre.accTier[1])

                    self.possibleLoot.extend(pre.weaponTier[3])
                    self.possibleLoot.extend(pre.armorTier[2])
                    self.possibleLoot.extend(pre.accTier[3])
                case 2: # Castle
                    self.setStage(pre.stages["Underworld"])
                    self.nextOutput += "\nYou advance to the Underworld!\n"

                    self.possibleLoot = self.removeMatches(self.possibleLoot, pre.weaponTier[2])
                    self.possibleLoot = self.removeMatches(self.possibleLoot, pre.armorTier[1])
                    self.possibleLoot = self.removeMatches(self.possibleLoot, pre.accTier[2])

                    self.possibleLoot.extend(pre.weaponTier[4])
                    self.possibleLoot.extend(pre.armorTier[3])
                    self.possibleLoot.extend(pre.accTier[4])
                case 3: # Underworld
                    self.setStage(pre.stages["Astral"])
                    self.nextOutput += "\nYou advance to the Astral Plane!\n"
                        
                    self.possibleLoot = self.removeMatches(self.possibleLoot, pre.weaponTier[3])
                    self.possibleLoot = self.removeMatches(self.possibleLoot, pre.weaponTier[2])
                    self.possibleLoot = self.removeMatches(self.possibleLoot, pre.accTier[3])
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
        valid = []
        plr = self.player
        for item in self.possibleLoot:
            try: 
                # Weapon
                if item.dmgType == plr.type.weapon:
                    valid.append(item)
            except Exception:
                try: 
                    # Armor
                    if item.armWeight == plr.type.armor:
                        valid.append(item)
                except Exception:
                    # Accesory
                    valid.append(item)
        loot = []
        if not (self.encountersComplete + 1) % 10 == 0:
            cycles = 0
            while cycles < 7:
                loot.append(self.getRandomLoot(valid))
                cycles += 1 
        else:
            loot = valid

        print("You opened a chest and found some loot!\nEnter an index starting at 1 to choose\nEnter 'skip' to skip\nEnter 'info [index]' to see info\n")
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
                    if choice.lower()[:4] == "info":
                        choiceVal = int(choice[5:])
                        print(loot[choiceVal - 1].getStatDisplay())
                        choice = None
                        continue

                    choice = int(choice)
                else:
                    didSkip = True
                    break
                if choice < 1 or choice > len(loot):
                    raise ValueError
                if not didSkip:
                    plr.getItem(loot[choice - 1])
            except ValueError:
                choice = None
                print("Bad Input")
                

    def getRandomLoot(self, pool):
        roll = random.randint(1,100)
        if roll > (30 if (self.stage.index < 5) else 90):
            return pool[random.randint(0, len(pool) - 1)]
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
                print("Inventory:\n")
                counter = 1
                for item in self.player.inventory:
                    print(str(counter) + ": " + item.name + ((", " + str(item.charges) + " charges") if item.maxCharges >= 0 else ""))
                    counter += 1
                choice = input("\nWhich item would you like to use?\nEnter an index starting at one\nEnter cancel to cancel\n")
                if choice.lower() != "cancel":
                    try:
                        self.player.inventory[int(choice) - 1].use(self)
                    except Exception:
                        self.nextOutput += "Couldn't find an item at that index\n\n"
                return "No Move"
            case "accesory" | "acc":
                if self.player.accesory.use(self):
                    self.nextOutput += "You used your accesory!\n"
                    return "Accesory"
                self.nextOutput += "You can't use that accesory!\n"
                return "No Move"
            case "get stats" | "stats" | "see stats":
                self.nextOutput += ("\n" + str(self.player.bStr * self.player.accesory.strMod) + " Str\n" + str(self.player.bCon * self.player.accesory.conMod) + " Con\n"
                      + str(self.player.bDex * self.player.accesory.dexMod) + " Dex\n\n")
                return "No Move"
            case "give up":
                self.player.hp = 0
                return "No Move"
            
            case "help":
                self.getHelp()
                
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

        if self.player.weapon.specType == "Oneshot":
            enemPercent = (target.hp / target.maxHealth) * 100
            self.player.weapon.specMult = enemPercent / 30
        elif self.player.weapon.specType == "Finisher":
            enemPercent = (target.hp / target.maxHealth) * 100
            self.player.weapon.specMult = (100 - enemPercent) / 25

        self.player.attack(target, self.player.weapon.specMult)
        specDamage = startHp - target.hp

        target.hp = startHp
        self.player.chargeMult = startCharge
        target.blockPower = startBlock
        target.blockCharges = startBCharges

        return [round(damage), round(specDamage)]

    def getHelp(self):
        helpType = input("\n" +
                         "What do you want help with?\n" +
                         "'controls'\n" +
                         "'gear'\n" +
                         "'specials'\n" +
                         "'consumables'\n").lower()
                
        match helpType:
            case "controls":
                input("\n" +
                      "'attack' or 'a' to attack an enemy\n" +
                      "'block' or 'b' to partially block the next three attacks\n" +
                      "'charge' or 'c' to increase the damage of your next attack, stacks\n" +
                      "'special' or 's' to use your weapon's special\n" +
                      "'use' or 'u' to use a consumable\n" +
                      "'accesory' or 'acc' to use your accesory\n" +
                      "'stats' to see your current stats\n" +
                      "'give up' to end your run\n" +
                      "\n" +
                      "Press enter to exit\n")
            case "gear":
                plr = self.player
                # Weapon
                print("")
                print(plr.weapon.getStatDisplay())
                print("")
                print(plr.armor.getStatDisplay())
                print("")
                print(str(plr.accesory.name) + ":\n" + (("Active: " + str(plr.accesory.useDesc)) if plr.accesory.canUse else "Can't be used") + "\n"
                       + (("Passive: " + str(plr.accesory.passiveDesc)) if plr.accesory.hasPassive else "Has no passive") + "\n"
                       + str(plr.accesory.strMod) + "x str\n" + str(plr.accesory.dexMod) + "x dex\n" + str(plr.accesory.conMod) + "x con\n" + str(plr.accesory.blkMod) + "x block charges\n" + str(plr.accesory.chrMod) + "x charge")
                input("\nPress enter to exit\n")
            case "specials":
                input("\n" + 
                      "Multi: Hits multiple enemies, nothing else\n" + 
                      "Weakening: The enemy's next attack does less damage, stacks\n" + 
                      "Fracturing: The enemy takes increased damage from your next attack\n" +
                      "Oneshot: Does increased damage the higher the enemy's health\n" + 
                      "Finisher: Does increased damage the lower the enemy's health\n" +
                       "\n" +
                      "Press enter to exit\n")
            case "consumables":
                input("\n" + 
                      "Heal Potion: Heals you to full health\n" +
                      "Strength Potion: Permanently raises strength by 2\n" +
                      "Dexterity Potion: Permanently raises dexterity by 2\n" + 
                      "Constitution Potion: Permanently raises constitution by 2\n" +
                      "Charge Potion: Permanently improves the damage boost of charge, immediately gives a large charge\n" +
                      "Block Potion: Permanently increases block charges on block, immediately gives a significant amount of block charges\n" +
                      "\n" +
                      "Press enter to exit\n")
                
                
    def getTarget(self, returnsIndex = False, totalTargets = 1):
        try:
            if len(self.enemies) > totalTargets:
                pIn = input("Which enemy would you like to target?\nEnter an index starting at 1\n")
                
                pIn = int(pIn)
                if pIn > 0 and pIn <= len(self.enemies): # Return entered enemy
                    return (self.enemies[pIn - 1]) if not returnsIndex else (pIn - 1)
                else: 
                    raise ValueError
            else:
                raise ValueError
        except ValueError: # Return first enemy
            return (self.enemies[0]) if not returnsIndex else 0


game = Game()

while True:
    game.emptyTerminal()
    print("Game Over\n")
    if game.stage.index > 0:
        print("Enter 'project damage' when choosing a class to see how much damage you will deal")
        print("Enter 'show run stats' when choosing a class to show extra run stats")
    if game.stage.index > 1:
        print("Enter 'show action damage' when choosing a class to see the damage each enemy does")
    if game.stage.index > 2:
        print("Enter 'show own dr' when choosing a class to see your own damage reduction")
    goOn = input("\nTry Again?\n")
    match goOn.lower(): # There are far too many of these, but its funny
        case "yes" | "y" | "ok" | "continue" | "try again" | "affirmative" | "yes please" | "indeed" | "certainly" | "sure" | "quite so" | "why not" | "lets do it" | "let's do it" | "go ahead" | "aight" | "k" | "kk" | "okie" | "okie dokie" | "hell yeah" | "yeah" | "most definitely" | "heck yeah" | "most certainly" | "i don't see why not" | "i dont see why not" | "i guess" | "i guess so" | "ig" | "for sure" | "yes sir" | "okie doki" | "bet" | "ight" | "yh" | "lets go" | "let's go" | "totally" | "mhm" | "mhm hm" | "mhm-hm" | "mhmhm" | "fo sho" | "try" | "for real" | "for real for real" | "fr" | "fr fr" | "frfr" | "thumbs up" | "👍" | "truly one of the best ideas of all time" | "truly one of the greatest ideas of all time" | "truly one of the most wonderful ideas of all time" | "truly one of the most wonderous ideas of all time" | "truly one of the most exquisite ideas of all time" | "truly one of the most beautiful ideas of all time" | "YES" | "agreed" | "absolutely":
            game.beginGame()
        case "a" | "b" | "c" | "s" | "":
            pass
        case _:
            break