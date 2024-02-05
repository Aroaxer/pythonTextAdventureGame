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

    def __init__(self) -> None:
        self.beginGame()

    def setupPlayer(self):
        choice = lower("""What class would you like to play as?
                       Warrior - 14 str 16 con 12 dex
                       Knight - 16 str 14 con 8 dex
                       Ranger - 10 str 16 con 14 dex
                       Rogue - 8 str 12 con 16 dex""")
        choice = lower(choice)
        self.player = Player(preTypes.types[choice])

    def genEnemy(self, isBoss = False):
        if isBoss:
            pass
        else:
            return preEnemies.enemies[stage - 1][random.randint(0, len(preEnemies.enemies[stage - 1]))]
    
    def beginGame(self):
        self.stage = preStages.Forest
        self.player = self.setupPlayer()
        self.difficulty = 1

        self.enemies = self.stage.getEncounter(self.difficulty)

        self.mainLoop()

    def mainLoop(self):
        inResult = self.takePlayerInput()

        return self.mainLoop() # Loops

    def takePlayerInput(self):
        input = input("What would you like to do?\n")
        return handlePlayerInput(input)

    def handlePlayerInput(self, input):
        match lower(input):
            case "attack" | "a":
                target = self.getTarget()
                self.player.attack(target)
                return "Attack"
                
    def getTarget(self, targetsFriendly = False, returnsIndex = False):
        if targetsFriendly:
            pass
        else:
            input = input("Which enemy would you like to target?\nEnter an index starting at 1\n")
            return (enemies[input - 1]) if not returnsIndex else (input - 1)


game = Game()