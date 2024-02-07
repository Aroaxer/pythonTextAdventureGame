import random

from Characters import preEnemies
from Characters.enemy import Enemy

class Stage():
    index = 0
    boss = None

    def getEnemies(self):
            return preEnemies.enemies[self.index]
    enemies = property(fget = getEnemies)

    def __init__(self, stage, boss) -> None:
        self.index = stage - 1
        self.boss = boss

    def getRandEnemy(self, level):
        return Enemy(preEnemies.enemies[self.index][random.randint(0, len(preEnemies.enemies[self.index]) - 1)], level)

    def getEncounter(self, challenge):
        enemsToReturn = []
        origChal = challenge
        while challenge > 0:
            counter = 0
            didGetEnem = False
            while counter < 25:
                tryEnemy = self.getRandEnemy(origChal)
                if tryEnemy.difficulty <= challenge:
                    enemsToReturn.append(tryEnemy)
                    challenge -= tryEnemy.difficulty
                    didGetEnem = True
                    break
                counter += 1
            if not didGetEnem: break
        return enemsToReturn
