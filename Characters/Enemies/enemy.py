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
                super.__init__(12, 10, 6, 3)
            case "Skeleton":
                self.difficulty = 2
                super.__init__(10, 8, 12, 3)
            case "Zombie":
                self.difficulty = 2
                super.__init__(10, 12, 6, 3)
            # Boss
            case "King Slime":
                self.difficulty = 5
                super.__init__(13, 13, 7, 6)

            # Stage 2