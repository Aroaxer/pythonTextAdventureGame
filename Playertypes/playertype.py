

class Playertype():
    name = ""

    armor = ""
    weapon = ""
    hpPerLevel = 0

    def __init__(self, name, armor, weapon, hpPerLevel):
        self.name = name
        self.weapon = weapon
        self.hpPerLevel = hpPerLevel
        self.armor = armor