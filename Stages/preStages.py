from Stages.stage import Stage
from Characters.enemy import Enemy

Forest = Stage(1, Enemy("King Slime", 2))

Caves = Stage(2, Enemy("Goblin Brute", 4))

Castle = Stage(3, Enemy("Royal Guard", 6))

Underworld = Stage(4, Enemy("Cerberus", 8))

Astral = Stage(5, Enemy("Astral Spirit", 10))

Infinite = Stage(6, None)