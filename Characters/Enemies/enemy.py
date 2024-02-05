from Characters.character import Character

class Enemy(Character):
    name = ""
    difficulty = 0

    def __init__(self, name):
        self.name = name

        match name: # Handles enemies by name
            # Stage 1
            case "Slime":
                self.difficulty = 1
                super.__init__(12, 10, 8, 3)
            case "Skeleton":
                self.difficulty = 2
                super.__init__(10, 8, 14, 3)
            case "Zombie":
                self.difficulty = 2
                super.__init__(12, 12, 6, 3)
            # Boss
            case "King Slime":
                self.difficulty = 3
                super.__init__(14, 14, 10, 6)

            # Stage 2
            case "Bat":
                self.difficulty = 1
                super.__init__(4, 8, 12, 4)
            case "Goblin":
                self.difficulty = 2
                super.__init__(12, 10, 12, 4)
            case "Goblin Archer":
                self.difficulty = 2
                super.__init__(7, 10, 14, 3)
            case "Cave Bear":
                self.difficulty = 3
                super.__init__(15, 15, 8, 5)
            # Boss
            case "Goblin Brute":
                self.difficulty = 5
                super.__init__(16, 16, 12, 7)
                
    def takeAction(self, game):
        self.attack(game.player)