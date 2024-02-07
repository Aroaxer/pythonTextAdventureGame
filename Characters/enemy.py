import random

from Characters.character import Character

class Enemy(Character):
    name = ""
    difficulty = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level

        match name: # Handles enemies by name
            # Stage 1
            case "Slime":
                self.difficulty = 1
                super().__init__(12, 10, 8, 5, "Basic Str")
            case "Skeleton":
                self.difficulty = 1
                super().__init__(10, 8, 14, 5, "Basic Dex")
            case "Zombie":
                self.difficulty = 1
                super().__init__(12, 12, 6, 6, "Basic Str")
            # Boss
            case "King Slime":
                self.difficulty = 3
                super().__init__(14, 14, 10, 10, "Basic Str")

            # Stage 2
            case "Bat":
                self.difficulty = 1
                super().__init__(4, 8, 12, 6, "Medium Dex")
            case "Goblin":
                self.difficulty = 2
                super().__init__(12, 10, 12, 7, "Medium Str")
            case "Goblin Archer":
                self.difficulty = 2
                super().__init__(7, 10, 14, 5, "Medium Dex")
            case "Cave Bear":
                self.difficulty = 3
                super().__init__(15, 15, 8, 8, "Medium Str")
            # Boss
            case "Goblin Brute":
                self.difficulty = 5
                super().__init__(16, 16, 12, 13, "Medium Str")

            # Stage 3
            case "Knight":
                self.difficulty = 3
                super().__init__(14, 13, 8, 8, "Advanced Str")
            case "Archer":
                self.difficulty = 3
                super().__init__(8, 12, 14, 6, "Advanced Dex")
            case "Peasant":
                self.difficulty = 1
                super().__init__(12, 16, 12, 8, "Medium Str")
            case "Gladiator":
                self.difficulty = 4
                super().__init__(16, 14, 12, 9, "Advanced Str")
            # Boss
            case "Royal Guard":
                self.difficulty = 7
                super().__init__(18, 14, 8, 16, "Advanced Str")

            # Stage 4
            case "Imp":
                self.difficulty = 1
                super().__init__(6, 10, 14, 7, "Advanced Dex")
            case "Hellhound":
                self.difficulty = 3
                super().__init__(14, 14, 6, 8, "Greater Str")
            case "Cambion":
                self.difficulty = 5
                super().__init__(16, 14, 10, 9, "Greater Str")
            case "Bone Devil":
                self.difficulty = 5
                super().__init__(10, 12, 16, 8, "Greater Dex")
            # Boss
            case "Cerberus":
                self.difficulty = 9
                super().__init__(20, 16, 8, 20, "Greater Str")
                
    def takeAction(self, game):
        roll = random.randint(0, 100)
        if roll > 50:
            self.attack(game.player)
            game.nextOutput += "The " + self.name + " Attacked!\n"
        elif roll > 25:
            self.block()
            game.nextOutput += "The " + self.name + " Blocked!\n"
        else:
            self.charge()
            game.nextOutput += "The " + self.name + " Charged its attack!\n"

    def isProf(self, armor):
        return True