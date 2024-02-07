from Weapons.weapon import Weapon

bronzeSword = Weapon("Bronze Sword", 6, "Melee", "Sweep")
ironSword = Weapon("Iron Sword", 8, "Melee", "Sweep")
steelSword = Weapon("Steel Sword", 10, "Melee", "Sweep")
mythrilSword = Weapon("Mythril Sword", 12, "Melee", "Sweep")
runicSword = Weapon("Runic Sword", 15, "Melee", "Sweep")


bronzeSpear = Weapon("Bronze Spear", 6, "Melee", "Weakening")
ironSpear = Weapon("Iron Spear", 8, "Melee", "Weakening")
steelSpear = Weapon("Steel Spear", 10, "Melee", "Weakening")
mythrilSpear = Weapon("Mythril Spear", 12, "Melee", "Weakening")
runicSpear = Weapon("Runic Spear", 15, "Melee", "Weakening")


bronzeAxe = Weapon("Bronze Axe", 6, "Melee", "Fracturing")
ironAxe = Weapon("Iron Axe", 8, "Melee", "Fracturing")
steelAxe = Weapon("Steel Axe", 10, "Melee", "Fracturing")
mythrilAxe = Weapon("Mythril Axe", 12, "Melee", "Fracturing")
runicAxe = Weapon("Runic Axe", 15, "Melee", "Fracturing")


oakShortbow = Weapon("Oak Shortbow", 9, "Ranged", "Pierce")
ironShortbow = Weapon("Iron Shortbow", 12, "Ranged", "Pierce")
oakLongbow = Weapon("Oak Longbow", 15, "Ranged", "Pierce")
ironLongbow = Weapon("Iron Longbow", 18, "Ranged", "Pierce")
runicBow = Weapon("Runic Bow", 22, "Ranged", "Pierce")


crossbow = Weapon("Crossbow", 9, "Ranged", "Fracturing")
ironCrossbow = Weapon("Iron Crossbow", 12, "Ranged", "Fracturing")
heavyCrossbow = Weapon("Heavy Crossbow", 15, "Ranged", "Fracturing")
steelCrossbow = Weapon("Steel Crossbow", 18, "Ranged", "Fracturing")
runicCrossbow = Weapon("Runic Crossbow", 22, "Ranged", "Fracturing")


bronzeJavelin = Weapon("Bronze Javelin", 9, "Ranged", "Weakening")
ironJavelin = Weapon("Iron Javelin", 12, "Ranged", "Weakening")
steelJavelin = Weapon("Steel Javelin", 15, "Ranged", "Weakening")
mythrilJavelin = Weapon("Mythril Javelin", 18, "Ranged", "Weakening")
runicJavelin = Weapon("Runic Javelin", 22, "Ranged", "Weakening")


tierOne = [bronzeSword, bronzeSpear, bronzeAxe, oakShortbow, crossbow, bronzeJavelin]
tierTwo = [ironSword, ironSpear, ironAxe, ironShortbow, ironCrossbow, ironJavelin]
tierThree = [steelSword, steelSpear, steelAxe, oakLongbow, heavyCrossbow, steelJavelin]
tierFour = [mythrilSword, mythrilSpear, mythrilAxe, ironLongbow, steelCrossbow, mythrilJavelin]
tierFive = [runicSword, runicSpear, runicAxe, runicBow, runicCrossbow, runicJavelin]

