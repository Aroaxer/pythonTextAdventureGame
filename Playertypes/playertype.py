

class Playertype():
    name = ""

    armors = []
    weapon = ""
    hpPerLevel = 0

    def __init__(self, name, bestArmor, weapon, hpPerLevel):
        self.name = name
        self.weapon = weapon
        self.hpPerLevel = hpPerLevel
        match bestArmor:
            case "Heavy":
                self.armors = ["Light", "Medium", "Heavy"]
            case "Medium":
                self.armors = ["Light", "Medium"]
            case "Light":
                self.armors = ["Light"]