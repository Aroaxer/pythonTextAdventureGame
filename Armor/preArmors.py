from Armor.armor import Armor

clothing = Armor("Clothing", 3, 0, "Light")

leatherArmor = Armor("Leather Armor", 4, 1, "Light")
studdedLeather = Armor("Studded Leather", 8, 1, "Light")
steelsilkArmor = Armor("Steelsilk Armor", 14, 2, "Light")
runicLeather = Armor("Runic Leather", 17, 3, "Light")

hideArmor = Armor("Hide Armor", 8, 1, "Medium")
scaleMail = Armor("Scale Mail", 13, 2, "Medium")
halfPlateArmor = Armor("Half Plate", 17, 3, "Medium")
runicMail = Armor("Runic Mail", 20, 4, "Medium")

chainmailArmor = Armor("Chainmail", 10, 1, "Heavy")
splintArmor = Armor("Splint", 15, 2, "Heavy")
plateArmor = Armor("Plate", 20, 4, "Heavy")
runicPlate = Armor("Runic Plate", 25, 5, "Heavy")

tierOne = [leatherArmor, hideArmor, chainmailArmor]
tierTwo = [studdedLeather, scaleMail, splintArmor]
tierThree = [steelsilkArmor, halfPlateArmor, plateArmor]
tierFour = [runicLeather, runicMail, runicPlate]
