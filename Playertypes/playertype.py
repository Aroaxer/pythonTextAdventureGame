

class Playertype():
    name = ""

    armors = []
    weapon = ""
    hpPerLevel = 0

    def __init__(self, name, bestArmor, weapon, hpPerLevel):
        self.name = name
        self.weapon = weapon
        self.hpPerLevel = hpPerLevel
        match self.bestArmor:
            case "Heavy":
                armors = ["Light", "Medium", "Heavy"]
            case "Medium":
                armors = ["Light", "Medium"]
            case "Light":
                armors = ["Light"]