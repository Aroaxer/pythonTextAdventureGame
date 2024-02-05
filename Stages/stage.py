import random

from Characters.Enemies import preEnemies

class Stage():
    index = 0

    def getEnemies(self, isRandom):
        if isRandom:
            return preEnemies.enemies[self.index][random.randint(0, len(preEnemies.enemies[self.index]) - 1)]
        else:
            return preEnemies.enemies[self.index]
    enemies = property(fget = getEnemies(False))
    randEnemy = property(fget = getEnemies(True))

    def __init__(self, stage) -> None:
        self.index = stage - 1

    def getEncounter(self, challenge):
        enemsToReturn = []
        while challenge > 0:
            counter = 0
            didGetEnem = False
            while counter < 25:
                tryEnemy = self.randEnemy
                if tryEnemy.difficulty <= challenge:
                    enemsToReturn.append(tryEnemy)
                    challenge -= tryEnemy.difficulty
                    didGetEnem = True
                    break
                counter += 1
            if not didGetEnem: break
        return enemsToReturn
