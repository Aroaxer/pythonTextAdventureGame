from Armor.armor import Armor

clothing = Armor("Clothing", 3, -2, "Light")

leatherArmor = Armor("Leather Armor", 3, -2, "Light")
studdedLeather = Armor("Studded Leather", 7, -1, "Light")
steelsilkArmor = Armor("Steelsilk Armor", 12, 0, "Light")
runicLeather = Armor("Runic Leather", 15, 1, "Light")

hideArmor = Armor("Hide Armor", 8, 0, "Medium")
scaleMail = Armor("Scale Mail", 13, 1, "Medium")
halfPlateArmor = Armor("Half Plate", 17, 2, "Medium")
runicMail = Armor("Runic Mail", 20, 3, "Medium")

chainmailArmor = Armor("Chainmail", 10, 2, "Heavy")
splintArmor = Armor("Splint", 15, 3, "Heavy")
plateArmor = Armor("Plate", 20, 4, "Heavy")
runicPlate = Armor("Runic Plate", 25, 5, "Heavy")

tierOne = [leatherArmor, hideArmor, chainmailArmor]
tierTwo = [studdedLeather, scaleMail, splintArmor]
tierThree = [steelsilkArmor, halfPlateArmor, plateArmor]
tierFour = [runicLeather, runicMail, runicPlate]
