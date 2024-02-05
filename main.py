import random
import math

from Characters.player import Player
from Characters.Enemies.enemy import Enemy
from Playertypes import preTypes
from Characters.Enemies import preEnemies
from Stages import preStages

class Game():
    player = None
    enemies = []

    stage = 0
    difficulty = 0
    encountersComplete = 0

    def __init__(self) -> None:
        self.beginGame()

    def setupPlayer(self):
        choice = ("""What class would you like to play as?
                       Warrior - 14 str 16 con 12 dex
                       Knight - 16 str 14 con 8 dex
                       Ranger - 10 str 16 con 14 dex
                       Rogue - 8 str 12 con 16 dex""").lower()
        choice = (choice).lower()
        self.player = Player(preTypes.types[choice])

    def beginGame(self):
        self.stage = preStages.Forest
        self.player = self.setupPlayer()
        self.difficulty = 1
        self.encountersComplete = 0

        self.enemies = self.stage.getEncounter(self.difficulty)

        self.mainLoop()

    def mainLoop(self):
        inResult = self.takePlayerInput()

        if len(self.enemies) == 0:
            self.completeEncounter()

        return self.mainLoop() # Loops
    
    def completeEncounter(self):
        self.encountersComplete += 1

        if (self.encountersComplete + 1) % 5 == 0:
            self.difficulty += 1
            # TODO: Should also drop items here

        if self.encountersComplete % 10 == 0:
            match self.stage: # Move to next stage after every boss
                case preStages.Forest:
                    self.stage = preStages.Caves
                case preStages.Caves:
                    pass
                
        # Get next encounter
        if (self.encountersComplete + 1) % 10 != 0:
            self.enemies = self.stage.getEncounter(self.difficulty)
        else: # Boss
            self.enemies = [self.stage.boss]

    def takePlayerInput(self):
        input = input("What would you like to do?\n")
        return self.handlePlayerInput(input)

    def handlePlayerInput(self, input):
        match (input).lower():
            case "attack" | "a":
                target = self.getTarget()
                self.player.attack(target)
                return "Attack"
                
    def getTarget(self, targetsFriendly = False, returnsIndex = False):
        if targetsFriendly:
            pass # May or may not end up using this
        else:
            input = input("Which enemy would you like to target?\nEnter an index starting at 1\n")
            if input > 0 and input <= len(self.enemies):
                return (self.enemies[input - 1]) if not returnsIndex else (input - 1)
            else: # TODO: Bad index handling
                pass


game = Game()