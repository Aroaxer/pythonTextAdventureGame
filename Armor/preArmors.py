from Armor.armor import Armor

clothing = Armor("Clothing", 3, -2, "Light")

leatherArmor = Armor("Leather Armor", 3, -2, "Light")
studdedLeather = Armor("Studded Leather", 7, -2, "Light")
steelsilkArmor = Armor("Steelsilk Armor", 12, -1, "Light")
runicLeather = Armor("Runic Leather", 15, -1, "Light")

hideArmor = Armor("Hide Armor", 8, 0, "Medium")
scaleMail = Armor("Scale Mail", 13, 0, "Medium")
halfPlateArmor = Armor("Half Plate", 17, 1, "Medium")
runicMail = Armor("Runic Mail", 20, 2, "Medium")

chainmailArmor = Armor("Chainmail", 10, 0, "Heavy")
splintArmor = Armor("Splint", 15, 1, "Heavy")
plateArmor = Armor("Plate", 20, 2, "Heavy")
runicPlate = Armor("Runic Plate", 25, 3, "Heavy")

tierOne = [leatherArmor, hideArmor, chainmailArmor]
tierTwo = [studdedLeather, scaleMail, splintArmor]
tierThree = [steelsilkArmor, halfPlateArmor, plateArmor]
tierFour = [runicLeather, runicMail, runicPlate]
