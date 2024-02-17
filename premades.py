from Weapons.weapon import Weapon
from Armor.armor import Armor
from Playertypes.playertype import Playertype
from Accesories.accesory import Accesory


# Stages
stages = {
    "Forest" : [1, "King Slime", "The Forest"],
    "Caves" : [2, "Goblin Brute", "The Caves"],
    "Castle" : [3, "Royal Guard", "The Castle"],
    "Underworld" : [4, "Cerberus", "The Underworld"],
    "Astral" : [5, "Astral Spirit", "The Astral Plane"],
    "Celestia" : [6, "Lesser Deity", "Mount Celestia"],
    "Infinite" : [7, None, "The Infinite Realm"]
}

# Enemies
enemies = [
    ["Slime", "Skeleton", "Zombie"],
    ["Bat", "Goblin", "Goblin Archer", "Cave Bear"],
    ["Knight", "Archer", "Peasant", "Gladiator"],
    ["Imp", "Hellhound", "Cambion", "Bone Devil"],
    ["Githyanki Trainee", "Githyanki Warrior", "Githzerai Monk", "Astral Traveller"],
    ["Angel", "Seraph", "Archangel", "Ki-rin", "Demigod"],
    ["Infinity Warrior", "Infinity Knight", "Infinity Ranger", "Infinity Rogue"]
]


# Weapons
bronzeSword = Weapon("Bronze Sword", 6, "Melee", "Multi", 0.4, multi = 3)
ironSword = Weapon("Iron Sword", 8, "Melee", "Multi", 0.5, multi = 4)
steelSword = Weapon("Steel Sword", 10, "Melee", "Multi", 0.6, multi = 5)
mythrilSword = Weapon("Mythril Sword", 12, "Melee", "Multi", 0.7, multi = 6)
runicSword = Weapon("Runic Sword", 15, "Melee", "Multi", 0.8, multi = 7)
infusedSword = Weapon("Infused Sword", 18, "Melee", "Multy", 0.9, multi = 8)
whirlingBlade = Weapon("Whirling Blade", 13, "Melee", "Multi", 1.0, multi = -1)
bladeOfTheWind = Weapon("Blade of the Wind", 16, "Melee", "Multi", 1.0, multi = -1)

bronzeSpear = Weapon("Bronze Spear", 6, "Melee", "Weakening", 0.7)
ironSpear = Weapon("Iron Spear", 8, "Melee", "Weakening", 0.8)
steelSpear = Weapon("Steel Spear", 10, "Melee", "Weakening", 0.9)
mythrilSpear = Weapon("Mythril Spear", 12, "Melee", "Weakening", 1.0)
runicSpear = Weapon("Runic Spear", 15, "Melee", "Weakening", 1.0)
infusedSpear = Weapon("Infused Spear", 18, "Melee", "Weakening", 1.0, multi = 2)
steelHalberd = Weapon("Steel Halberd", 10, "Melee", "Weakening", 0.6, multi = 2)
mythrilHalberd = Weapon("Mythril Halberd", 12, "Melee", "Weakening", 0.6, multi = 3)
runicHalberd = Weapon("Runic Halberd", 15, "Melee", "Weakening", 0.7, multi = 4)
infusedHalberd = Weapon("Infused Halberd", 18, "Melee", "Weakening", 0.7, multi = 5)

bronzeAxe = Weapon("Bronze Axe", 6, "Melee", "Fracturing", 0.5)
ironAxe = Weapon("Iron Axe", 8, "Melee", "Fracturing", 0.5)
steelAxe = Weapon("Steel Axe", 10, "Melee", "Fracturing", 0.6)
mythrilAxe = Weapon("Mythril Axe", 12, "Melee", "Fracturing", 0.6)
runicAxe = Weapon("Runic Axe", 15, "Melee", "Fracturing", 0.7)
infusedAxe = Weapon("Infused Axe", 18, "Melee", "Fracturing", 0.8)
dualAxes = Weapon("Dual Axes", 17, "Melee", "Fracturing", 0.4, multi = 2)
ragnarokAxes = Weapon("Ragnarok Axes", 20, "Melee", "Fracturing", 0.4, multi = 4)

oakShortbow = Weapon("Oak Shortbow", 9, "Ranged", "Multi", 0.7, multi = 2)
ironShortbow = Weapon("Iron Shortbow", 12, "Ranged", "Multi", 0.7, multi = 2)
oakLongbow = Weapon("Oak Longbow", 15, "Ranged", "Multi", 0.8, multi = 2)
ironLongbow = Weapon("Iron Longbow", 18, "Ranged", "Multi", 0.8, multi = 2)
runicBow = Weapon("Runic Bow", 22, "Ranged", "Multi", 0.9, multi = 2)
infusedBow = Weapon("Infused Bow", 25, "Ranged", "Multi", 1.0, multi = 3)
trinityBow = Weapon("Trinity Bow", 25, "Ranged", "Multi", 0.7, multi = 3)
pentashotBow = Weapon("Pentashot Bow", 28, "Ranged", "Multi", 0.8, multi = 5)

crossbow = Weapon("Crossbow", 9, "Ranged", "Fracturing", 0.4)
ironCrossbow = Weapon("Iron Crossbow", 12, "Ranged", "Fracturing", 0.5)
heavyCrossbow = Weapon("Heavy Crossbow", 15, "Ranged", "Fracturing", 0.6)
steelCrossbow = Weapon("Steel Crossbow", 18, "Ranged", "Fracturing", 0.7)
runicCrossbow = Weapon("Runic Crossbow", 22, "Ranged", "Fracturing", 0.8)
infusedCrossbow = Weapon("Infused Crossbow", 25, "Ranged", "Fracturing", 0.9)
ballista = Weapon("Ballista", 18, "Ranged", "Fracturing", 0.6, multi = 5)
triballista = Weapon("Triballista", 22, "Ranged", "Fracturing", 0.7, multi = -1)

bronzeJavelin = Weapon("Bronze Javelin", 9, "Ranged", "Weakening", 0.7)
ironJavelin = Weapon("Iron Javelin", 12, "Ranged", "Weakening", 0.8)
steelJavelin = Weapon("Steel Javelin", 15, "Ranged", "Weakening", 0.9)
mythrilJavelin = Weapon("Mythril Javelin", 18, "Ranged", "Weakening", 1.0)
runicJavelin = Weapon("Runic Javelin", 22, "Ranged", "Weakening", 1.0)
infusedJavelin = Weapon("Infused Javelin", 25, "Ranged", "Weakening", 1.0, multi = 2)
steelKnives = Weapon("Steel Knives", 15, "Ranged", "Weakening", 0.6, multi = 2)
mythrilKnives = Weapon("Mythril Knives", 18, "Ranged", "Weakening", 0.6, multi = 3)
runicKnives = Weapon("Runic Knives", 22, "Ranged", "Weakening", 0.7, multi = 4)
infusedKnives = Weapon("Infused Knives", 25, "Ranged", "Weakening", 0.7, multi = 5)

silverBlade = Weapon("Silver Blade", 8, "Melee", "Oneshot", 0.0)
pureBlade = Weapon("Pure Blade", 10, "Melee", "Oneshot", 0.0)
holyBlade = Weapon("Holy Blade", 12, "Melee", "Oneshot", 0.0)
sacredBlade = Weapon("Sacred Blade", 15, "Melee", "Oneshot", 0.0, multi = 2)
heavenlyBlade = Weapon("Heavenly Blade", 18, "Melee", "Oneshot", 0.0, multi = 2)

flamingBow = Weapon("Flaming Bow", 12, "Ranged", "Finisher", 0.0)
crimsonBow = Weapon("Crimson Bow", 15, "Ranged", "Finisher", 0.0)
helfireBow = Weapon("Helfire Bow", 18, "Ranged", "Finisher", 0.0)
unholyBow = Weapon("Unholy Bow", 22, "Ranged", "Finisher", 0.0, multi = 2)
hellishBow = Weapon("Hellish Bow", 25, "Ranged", "Finisher", 0.0, multi = 2)


weaponTier = [
    [bronzeSword, bronzeSpear, bronzeAxe, oakShortbow, crossbow, bronzeJavelin],
    [ironSword, ironSpear, ironAxe, ironShortbow, ironCrossbow, ironJavelin, silverBlade, flamingBow],
    [steelSword, steelSpear, steelAxe, oakLongbow, heavyCrossbow, steelJavelin, steelHalberd, steelKnives, pureBlade, crimsonBow],
    [mythrilSword, mythrilSpear, mythrilAxe, ironLongbow, steelCrossbow, mythrilJavelin, mythrilHalberd, mythrilKnives, holyBlade, helfireBow],
    [runicSword, runicSpear, runicAxe, runicBow, runicCrossbow, runicJavelin, whirlingBlade, runicHalberd, dualAxes, trinityBow, ballista, runicKnives, sacredBlade, unholyBow],
    [infusedSword, infusedSpear, infusedAxe, infusedBow, infusedCrossbow, infusedJavelin, bladeOfTheWind, infusedHalberd, ragnarokAxes, pentashotBow, triballista, infusedKnives, heavenlyBlade, hellishBow]
]


# Armor
clothing = Armor("Clothing", 3, -2, "Light")
adventureGear = Armor("Adventure Gear", 5, 0, "Medium")

# Light
leatherArmor = Armor("Leather Armor", 3, -2, "Light")
studdedLeather = Armor("Studded Leather", 7, -1, "Light")
steelsilkArmor = Armor("Steelsilk Armor", 12, 0, "Light")
runicLeather = Armor("Runic Leather", 15, 1, "Light")
infusedLeather = Armor("Infused Leather", 18, 2, "Light")

shadowedCloak = Armor("Shadowed Cloak", -20, 1, "Light")
midnightCloak = Armor("Midnight Cloak", -10, 2, "Light")
purenightCloak = Armor("Purenight Cloak", 0, 3, "Light")

coatOfKnives = Armor("Coat of Knives", 10, -1, "Light")
cloakOfDaggers = Armor("Cloak of Daggers", 12, 0, "Light")
cloakOfBlades = Armor("Cloak of Blades", 15, 1, "Light")

# Medium
hideArmor = Armor("Hide Armor", 8, 0, "Medium")
scaleMail = Armor("Scale Mail", 13, 1, "Medium")
halfPlateArmor = Armor("Half Plate", 17, 2, "Medium")
runicMail = Armor("Runic Mail", 20, 3, "Medium")
infusedMail = Armor("Infused Mail", 24, 4, "Medium")

spikedMail = Armor("Spiked Mail", 10, 1, "Medium")
battleragerMail = Armor("Battlerager Mail", 15, 2, "Medium")
ragnarokMail = Armor("Ragnarok Mail", 21, 3, "Medium")

explorersLeathers = Armor("Explorer's Leathers", 15, 1, "Medium")
dungeoneersMail = Armor("Dungeoneer's Mail", 20, 2, "Medium")

adaptiveMail = Armor("Adaptive Mail", 15, 2, "Medium")

# Heavy
chainmailArmor = Armor("Chainmail", 10, 2, "Heavy")
splintArmor = Armor("Splint", 15, 3, "Heavy")
plateArmor = Armor("Plate", 20, 4, "Heavy")
runicPlate = Armor("Runic Plate", 25, 5, "Heavy")
infusedPlate = Armor("Infused Plate", 30, 6, "Heavy")

stonyPlate = Armor("Stony Plate", 10, 2, "Heavy")
overgrownPlate = Armor("Overgrown Plate", 17, 3, "Heavy")
yggdrasilPlate = Armor("Yggdrasil Plate", 25, 4, "Heavy")

holyPlate = Armor("Holy Plate", 12, 1, "Heavy")
sacredPlate = Armor("Sacred Plate", 22, 3, "Heavy")
heavenlyPlate = Armor("Heavenly Plate", 27, 4, "Heavy")

armorTier = [
    [leatherArmor, hideArmor, chainmailArmor],
    [studdedLeather, scaleMail, splintArmor, shadowedCloak, spikedMail, stonyPlate, holyPlate],
    [steelsilkArmor, halfPlateArmor, plateArmor, coatOfKnives, explorersLeathers, overgrownPlate, battleragerMail],
    [runicLeather, runicMail, runicPlate, midnightCloak, cloakOfDaggers, adaptiveMail, sacredPlate],
    [infusedLeather, infusedMail, infusedPlate, purenightCloak, cloakOfBlades, ragnarokMail, dungeoneersMail, yggdrasilPlate, heavenlyPlate]
]


# Accesories
oldAmulet = Accesory("Old Amulet")
crystalNecklace = Accesory("Crystal Necklace")
runicAmulet = Accesory("Runic Amulet")

ironGauntlets = Accesory("Iron Gauntlets")
steelGauntlets = Accesory("Steel Gauntlets")
steelsilkGloves = Accesory("Steelsilk Gloves")

runicSheath = Accesory("Runic Sheath")
mythicSheath = Accesory("Mythic Sheath")
runicQuiver = Accesory("Runic Quiver")
mythicQuiver = Accesory("Mythic Quiver")
 
ironShield = Accesory("Iron Shield")
towerShield = Accesory("Tower Shield")
runicShield = Accesory("Runic Shield")

accumulatorShield = Accesory("Accumulator Shield")

ritualDagger = Accesory("Ritual Dagger")
sacrificialBlade = Accesory("Sacrificial Blade")
ritualAltar = Accesory("Ritual Altar")

animatedShield = Accesory("Animated Shield")
energyAccumulator = Accesory("Energy Accumulator")
runicAccumulator = Accesory("Runic Accumulator")

recoveryJewel = Accesory("Recovery Jewel")
regenerativeCirclet = Accesory("Regenerative Circlet")
restorativeCrown = Accesory("Restorative Crown")

accTier = [
    [ironGauntlets, ironShield, recoveryJewel],
    [crystalNecklace, steelGauntlets, steelsilkGloves],
    [ritualDagger, animatedShield, energyAccumulator],
    [runicSheath, runicQuiver, regenerativeCirclet],
    [runicShield, runicAccumulator, runicAmulet, sacrificialBlade],
    [mythicSheath, mythicQuiver, accumulatorShield, ritualAltar, restorativeCrown]
]



# Consumables
consumables = [
    "Heal Potion",
    "Strength Potion",
    "Dexterity Potion",
    "Constitution Potion",
    "Charge Potion",
    "Block Potion"
]


# Player types
types = {
    "warrior": Playertype("Warrior", "Medium", "Melee", 6),
    "knight": Playertype("Knight", "Heavy", "Melee", 5),
    "ranger": Playertype("Ranger", "Medium", "Ranged", 5),
    "rogue": Playertype("Rogue", "Light", "Ranged", 4)
}