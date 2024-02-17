import random

from Characters.character import Character

class Enemy(Character):
    name = ""
    difficulty = 0
    actions = 1

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
                super().__init__(10, 8, 14, 4, "Basic Dex")
            case "Zombie":
                self.difficulty = 1
                super().__init__(12, 12, 6, 6, "Basic Str")
            # Boss
            case "King Slime":
                self.difficulty = 3
                self.actions = 2
                super().__init__(14, 14, 10, 11, "Basic Str")

            # Stage 2
            case "Bat":
                self.difficulty = 1
                super().__init__(4, 8, 12, 5, "Basic Dex")
            case "Goblin":
                self.difficulty = 2
                super().__init__(12, 10, 12, 6, "Medium Str")
            case "Goblin Archer":
                self.difficulty = 2
                super().__init__(7, 10, 14, 4, "Medium Dex")
            case "Cave Bear":
                self.difficulty = 3
                super().__init__(16, 14, 8, 6, "Medium Str")
            # Boss
            case "Goblin Brute":
                self.difficulty = 5
                self.actions = 2
                super().__init__(16, 16, 12, 14, "Medium Str")

            # Stage 3
            case "Knight":
                self.difficulty = 3
                super().__init__(14, 13, 8, 7, "Advanced Str")
            case "Archer":
                self.difficulty = 3
                super().__init__(8, 12, 14, 4, "Advanced Dex")
            case "Peasant":
                self.difficulty = 1
                super().__init__(12, 16, 12, 5, "Medium Str")
            case "Gladiator":
                self.difficulty = 4
                super().__init__(16, 14, 12, 8, "Advanced Str")
            # Boss
            case "Royal Guard":
                self.difficulty = 7
                self.actions = 3
                super().__init__(18, 14, 8, 17, "Advanced Str")

            # Stage 4
            case "Imp":
                self.difficulty = 1
                super().__init__(6, 10, 14, 6, "Advanced Dex")
            case "Hellhound":
                self.difficulty = 3
                super().__init__(14, 14, 6, 9, "Greater Str")
            case "Cambion":
                self.difficulty = 5
                super().__init__(16, 14, 10, 8, "Greater Str")
            case "Bone Devil":
                self.difficulty = 5
                super().__init__(10, 12, 16, 7, "Greater Dex")
            # Boss
            case "Cerberus":
                self.difficulty = 9
                self.actions = 3
                super().__init__(20, 16, 8, 20, "Greater Str")

            # Stage 5
            case "Githyanki Trainee":
                self.difficulty = 1
                super().__init__(14, 12, 12, 7, "Greater Str")
            case "Githyanki Warrior":
                self.difficulty = 4
                super().__init__(16, 14, 12, 9, "Runic Str")
            case "Githzerai Monk":
                self.difficulty = 4
                super().__init__(10, 14, 16, 8, "Runic Dex")
            case "Astral Traveller":
                self.difficulty = 7
                super().__init__(18, 18, 18, 10, "Runic Str")
            # Boss
            case "Astral Spirit":
                self.difficulty = 11
                self.actions = 4
                super().__init__(18, 20, 22, 23, "Runic Dex")

            # Stage 6
            case "Angel":
                self.difficulty = 2
                super().__init__(18, 16, 16, 8, "Runic Str")
            case "Seraph":
                self.difficulty = 5
                super().__init__(14, 16, 20, 10, "Infused Dex")
            case "Archangel":
                self.difficulty = 5
                super().__init__(20, 18, 16, 11, "Infused Str")
            case "Ki-rin":
                self.difficulty = 7
                super().__init__(16, 20, 16, 13, "Infused Dex")
            case "Demigod":
                self.difficulty = 8
                self.actions = 2
                super().__init__(22, 20, 12, 12, "Infused Str")
            # Boss
            case "Lesser Deity":
                self.difficulty = 13
                self.actions = 4
                super().__init__(24, 20, 20, 26, "Infused Str")
            
            # Stage 7
            case "Infinity Warrior":
                self.difficulty = 5
                super().__init__(16, 18, 12, 13, "Runic Str")
            case "Infinity Knight":
                self.difficulty = 5
                super().__init__(18, 16, 12, 12, "Runic Str")
            case "Infinity Ranger":
                self.difficulty = 5
                super().__init__(12, 18, 16, 12, "Runic Dex")
            case "Infinity Rogue":
                self.difficulty = 5
                super().__init__(12, 16, 18, 11, "Runic Dex")
                
                
    def takeAction(self, game):
        counter = 0
        while counter < self.actions:
            roll = random.randint(0, 100)
            if roll > 40:
                tempHp = game.player.hp
                self.attack(game.player)
                if not game.extraSettings["printDmgOnAction"]:
                    game.nextOutput += "The " + self.name + " Attacked!\n"
                else:
                    game.nextOutput += "The " + self.name + " Attacked for " + str(tempHp - game.player.hp) + " damage!\n"
                game.player.armor.reactive(game, self, (tempHp - game.player.hp))
            else:
                self.charge()
                game.nextOutput += "The " + self.name + " Charged its attack!\n"
            counter += 1

    def isProf(self, armor):
        return True