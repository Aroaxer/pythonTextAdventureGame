import random
import math

from Characters.player import Player
from Characters.enemy import Enemy
from Playertypes import preTypes
from Characters import preEnemies

class Game():
    player = None
    enemies = []

    stage = 0

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
        self.stage = 1
        self.player = self.setupPlayer()
        self.enemies.append(self.genEnemy())

        self.mainLoop()

    def mainLoop(self):
        inResult = self.takePlayerInput()

        return self.mainLoop()

    def takePlayerInput(self):
        input = input("What would you like to do?\n")
        return handlePlayerInput(input)

    def handlePlayerInput(self, input):
        match lower(input):
            case "attack" | "a":
                target = self.getTarget()
                self.player.attack(target)
                return "Attack"
                
    def getTarget(self, targetsFriendly = False):
        if targetsFriendly:
            pass
        else:
            input = input("Which enemy would you like to target?\nEnter an index starting at 1\n")
            return enemies[input - 1]


game = Game()