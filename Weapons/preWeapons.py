from Weapons.weapon import Weapon

bronzeSword = Weapon("Bronze Sword", 6, "Melee", "Sweep", 0.4)
ironSword = Weapon("Iron Sword", 8, "Melee", "Sweep", 0.5)
steelSword = Weapon("Steel Sword", 10, "Melee", "Sweep", 0.6)
mythrilSword = Weapon("Mythril Sword", 12, "Melee", "Sweep", 0.7)
runicSword = Weapon("Runic Sword", 15, "Melee", "Sweep", 0.8)


bronzeSpear = Weapon("Bronze Spear", 6, "Melee", "Weakening", 0.7)
ironSpear = Weapon("Iron Spear", 8, "Melee", "Weakening", 0.7)
steelSpear = Weapon("Steel Spear", 10, "Melee", "Weakening", 0.8)
mythrilSpear = Weapon("Mythril Spear", 12, "Melee", "Weakening", 0.8)
runicSpear = Weapon("Runic Spear", 15, "Melee", "Weakening", 0.9)


bronzeAxe = Weapon("Bronze Axe", 6, "Melee", "Fracturing", 0.5)
ironAxe = Weapon("Iron Axe", 8, "Melee", "Fracturing", 0.6)
steelAxe = Weapon("Steel Axe", 10, "Melee", "Fracturing", 0.7)
mythrilAxe = Weapon("Mythril Axe", 12, "Melee", "Fracturing", 0.8)
runicAxe = Weapon("Runic Axe", 15, "Melee", "Fracturing", 0.9)


oakShortbow = Weapon("Oak Shortbow", 9, "Ranged", "Pierce", 0.7)
ironShortbow = Weapon("Iron Shortbow", 12, "Ranged", "Pierce", 0.7)
oakLongbow = Weapon("Oak Longbow", 15, "Ranged", "Pierce", 0.8)
ironLongbow = Weapon("Iron Longbow", 18, "Ranged", "Pierce", 0.8)
runicBow = Weapon("Runic Bow", 22, "Ranged", "Pierce", 0.9)


crossbow = Weapon("Crossbow", 9, "Ranged", "Fracturing", 0.5)
ironCrossbow = Weapon("Iron Crossbow", 12, "Ranged", "Fracturing", 0.6)
heavyCrossbow = Weapon("Heavy Crossbow", 15, "Ranged", "Fracturing", 0.7)
steelCrossbow = Weapon("Steel Crossbow", 18, "Ranged", "Fracturing", 0.8)
runicCrossbow = Weapon("Runic Crossbow", 22, "Ranged", "Fracturing", 0.9)


bronzeJavelin = Weapon("Bronze Javelin", 9, "Ranged", "Weakening", 0.7)
ironJavelin = Weapon("Iron Javelin", 12, "Ranged", "Weakening", 0.7)
steelJavelin = Weapon("Steel Javelin", 15, "Ranged", "Weakening", 0.8)
mythrilJavelin = Weapon("Mythril Javelin", 18, "Ranged", "Weakening", 0.8)
runicJavelin = Weapon("Runic Javelin", 22, "Ranged", "Weakening", 0.9)


tierOne = [bronzeSword, bronzeSpear, bronzeAxe, oakShortbow, crossbow, bronzeJavelin]
tierTwo = [ironSword, ironSpear, ironAxe, ironShortbow, ironCrossbow, ironJavelin]
tierThree = [steelSword, steelSpear, steelAxe, oakLongbow, heavyCrossbow, steelJavelin]
tierFour = [mythrilSword, mythrilSpear, mythrilAxe, ironLongbow, steelCrossbow, mythrilJavelin]
tierFive = [runicSword, runicSpear, runicAxe, runicBow, runicCrossbow, runicJavelin]

