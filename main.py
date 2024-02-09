import random

from Characters.player import Player
from Playertypes import preTypes
from Stages import preStages
from Weapons import preWeapons
from Armor import preArmors
from Consumables import consumable as cns

class Game():
    player = None
    enemies = []

    possibleLoot = []

    nextOutput = ""

    stage = 0
    difficulty = 0
    encountersComplete = 0

    def __init__(self) -> None:
        self.beginGame()

    def setupPlayer(self):
        succeeded = False
        while not succeeded:
            try:
                self.emptyTerminal()
                choice = input("What class would you like to play as?\n" +
                            "Warrior - 14 str 16 con 12 dex\n" +
                            "Knight - 16 str 14 con 8 dex\n" +
                            "Ranger - 10 str 16 con 14 dex\n" +
                            "Rogue - 8 str 12 con 16 dex\n").lower()
                self.player = Player(preTypes.types[choice])
                succeeded = True
            except Exception:
                pass

    def beginGame(self):
        self.emptyTerminal()
        self.nextOutput = ""

        self.possibleLoot = []
        self.possibleLoot.extend(preWeapons.tierOne)
        self.possibleLoot.extend(preWeapons.tierTwo)
        self.possibleLoot.extend(preArmors.tierOne)

        self.stage = preStages.Forest
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
        for enemy in self.enemies:
            print(enemy.name + ": " + str(round(enemy.hp)) + " health")
    
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
            match self.stage: # Move to next stage after every boss
                case preStages.Forest:
                    self.stage = preStages.Caves
                    self.nextOutput += "\nYou advance to the Caves!\n"

                    self.possibleLoot = self.removeMatches(self.possibleLoot, preWeapons.tierOne)

                    self.possibleLoot.extend(preWeapons.tierThree)
                    self.possibleLoot.extend(preArmors.tierTwo)
                case preStages.Caves:
                    self.stage = preStages.Castle
                    self.nextOutput += "\nYou advance to the Castle!\n"

                    self.possibleLoot = self.removeMatches(self.possibleLoot, preWeapons.tierTwo)
                    self.possibleLoot = self.removeMatches(self.possibleLoot, preArmors.tierOne)

                    self.possibleLoot.extend(preWeapons.tierFour)
                    self.possibleLoot.extend(preArmors.tierThree)
                case preStages.Castle:
                    self.stage = preStages.Underworld
                    self.nextOutput += "\nYou advance to the Underworld!\n"

                    self.possibleLoot = self.removeMatches(self.possibleLoot, preWeapons.tierThree)
                    self.possibleLoot = self.removeMatches(self.possibleLoot, preArmors.tierTwo)

                    self.possibleLoot.extend(preWeapons.tierFive)
                    self.possibleLoot.extend(preArmors.tierFour)
                case preStages.Underworld:
                    self.stage = preStages.Astral
                    self.nextOutput += "\nYou advance to the Astral Plane!\n"
                    
                    self.possibleLoot = self.removeMatches(self.possibleLoot, preWeapons.tierFour)
                    self.possibleLoot = self.removeMatches(self.possibleLoot, preArmors.tierThree)
                case preStages.Astral:
                    self.stage = preStages.Infinite
                    self.nextOutput += "\nYou advance to the Infinite Realm!\n"
                case preStages.Infinite:
                    self.difficulty += 1
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
        while cycles < self.difficulty + 4:
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
        if roll > (30 if self.stage != preStages.Infinite else 90):
            return self.possibleLoot[random.randint(0, len(self.possibleLoot) - 1)]
        else:
            return cns.Consumable(cns.consumables[random.randint(0, len(cns.consumables) - 1)])

    def takePlayerInput(self):
        pIn = input("What would you like to do?\n")
        return self.handlePlayerInput(pIn)

    def handlePlayerInput(self, pIn):
        match (pIn).lower():
            case "attack" | "a":
                target = self.getTarget()
                self.player.attack(target)
                self.nextOutput += "You attacked the " + target.name + "!\n"
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
                choice = input("Which item would you like to use?\nEnter an index starting at one\nEnter cancel to cancel")
                if choice.lower() != "cancel":
                    try:
                        self.player.inventory[int(choice) - 1].use(self)
                    except Exception:
                        self.nextOutput += "Couldn't find an item at that index\n\n"
                return "No Move"
            case "pd":
                target = self.getTarget()
                damage = self.player.weapon.dealDamage(self.player)
                damage *= self.player.chargeMult
                damage = (target.armor.reduceDamage(damage, target) / (target.blockPower if target.blockCharges > 0 else 1))

                self.nextOutput += "You would deal " + str(damage) + " damage to that target!\n"
                self.nextOutput += "Special: " + str(damage * self.player.weapon.specMult) + " damage\n"
                return "No Move"
            case "get stats" | "stats" | "see stats":
                self.nextOutput += ("\n" + str(self.player.bStr) + " Str\n" + str(self.player.bCon) + " Con\n"
                      + str(self.player.bDex) + " Dex\n\n")
                return "No Move"
            
            case _:
                return "No Move"
                
    def getTarget(self, targetsFriendly = False, returnsIndex = False):
        if targetsFriendly:
            pass # May or may not end up using this
        else:
            try:
                if len(self.enemies) > 1:
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
    goOn = input("Try Again?\n")
    match goOn.lower():
        case "yes" | "y" | "ok" | "continue" | "try again":
            game.beginGame()
        case _:
            break