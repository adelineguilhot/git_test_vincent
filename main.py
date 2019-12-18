import random


class Wizard:
    magic_dice = 12
    sword_dice = 8
    bow_dice = 10
    maximum_points_vie = 12

    def __init__(self, name):
        self.name = name
        self.current_life_points = self.maximum_points_vie

    def attack(self):
        sword = random.randint(1, self.sword_dice)
        magic = random.randint(1, self.magic_dice)
        bow = random.randint(1, self.bow_dice)
        print(sword)
        print(bow)
        print(magic)
        if bow > sword and bow > magic:
            weapon = "bow"
            attack_points = bow
            print("attaque par l'arme: %s; et lance %s de dégats !" % (weapon, attack_points))
        elif sword > bow and sword > magic:
            weapon = "sword"
            attack_points = sword
            print("attaque par l'arme: %s; et lance %s de dégats !" % (weapon, attack_points))
        else:
            weapon = "magic"
            attack_points = magic
            print("attaque par l'arme: %s; et lance %s de dégats !" % (weapon, attack_points))
        return weapon, attack_points

    def defend(self, weapon, attack_points):
        if weapon == "bow":
            bow = random.randint(1, self.bow_dice)
            if bow < attack_points:
                self.current_life_points -= attack_points
            print("defense par l'arme: %s; il vous reste %s de vie !" % (weapon, self.current_life_points))
        elif weapon == "sword":
            sword = random.randint(1, self.sword_dice)
            if sword < attack_points:
                self.current_life_points -= attack_points
            print("defense par l'arme: %s; il vous reste %s de vie !" % (weapon, self.current_life_points))
        if weapon == "magic":
            magic = random.randint(1, self.magic_dice)
            if magic < attack_points:
                self.current_life_points -= attack_points
            print("defense par l'arme: %s; il vous reste %s de vie !" % (weapon, self.current_life_points))


class Warrior:
    magic_dice = 8
    sword_dice = 12
    bow_dice = 10
    max_life_points = 16

    def __init__(self, name):
        self.name = name
        self.current_life_points = self.max_life_points

    def attack(self):
        sword = random.randint(1, self.sword_dice)
        magic = random.randint(1, self.magic_dice)
        bow = random.randint(1, self.bow_dice)
        print(sword)
        print(bow)
        print(magic)
        if bow > sword and bow > magic:
            weapon = "bow"
            attack_points = bow
            print("attaque par l'arme: %s; et lance %s de dégats !" % (weapon, attack_points))

        elif sword > bow and sword > magic:
            weapon = "sword"
            attack_points = sword
            print("attaque par l'arme: %s; et lance %s de dégats !" % (weapon, attack_points))

        else:
            weapon = "magic"
            attack_points = magic
            print("attaque par l'arme: %s; et lance %s de dégats !" % (weapon, attack_points))
        return weapon, attack_points

    def defend(self):
        if weapon == "bow":
            bow = random.randint(1, self.bow_dice)
            if bow < attack_points:
                self.current_life_points -= attack_points
                print("defense par l'arme: %s; il vous reste %s de vie !" % (weapon, self.current_life_points))
        elif weapon == "sword":
            sword = random.randint(1, self.sword_dice)
            if sword < attack_points:
                self.current_life_points -= attack_points
                print("defense par l'arme: %s; il vous reste %s de vie !" % (weapon, self.current_life_points))
        if weapon == "magic":
            magic = random.randint(1, self.magic_dice)
            if magic < attack_points:
                self.current_life_points -= attack_points
            print("defense par l'arme: %s; il vous reste %s de vie !" % (weapon, self.current_life_points))


class Archer:
    magic_dice = 10
    sword_dice = 8
    bow_dice = 12
    max_life_points = 12

    def __init__(self, name):
        self.name = name
        self.current_life_points = self.max_life_points

    def attack(self):
        sword = random.randint(1, self.sword_dice)
        magic = random.randint(1, self.magic_dice)
        bow = random.randint(1, self.bow_dice)
        print(sword)
        print(bow)
        print(magic)
        if bow > sword and bow > magic:
            weapon = "bow"
            attack_points = bow
            print("attaque par l'arme: %s; et lance %s de dégats !" % (weapon, attack_points))

        elif sword > bow and sword > magic:
            weapon = "sword"
            attack_points = sword
            print("attaque par l'arme: %s; et lance %s de dégats !" % (weapon, attack_points))
        else:
            weapon = "magic"
            attack_points = magic
            print("attaque par l'arme: %s; et lance %s de dégats !" % (weapon, attack_points))
        return weapon, attack_points

    def defend(self, weapon, attack_points):
        if weapon == "bow":
            bow = random.randint(1, self.bow_dice)
            if bow < attack_points:
                self.current_life_points -= attack_points
                print("defense par l'arme: %s; il vous reste %s de vie !" % (weapon, self.current_life_points))
        elif weapon == "sword":
            sword = random.randint(1, self.sword_dice)
            if sword < attack_points:
                self.current_life_points -= attack_points
                print("defense par l'arme: %s; il vous reste %s de vie !" % (weapon, self.current_life_points))
        if weapon == "magic":
            magic = random.randint(1, self.magic_dice)
            if magic < attack_points:
                self.current_life_points -= attack_points
                print("defense par l'arme: %s; il vous reste %s de vie !" % (weapon, self.current_life_points))


gandalf = Wizard("gandalf")
gimli = Warrior("gimli")
arthur = Archer("arthur")



# dans le cas ou gandalf attaque arthur
weapon, attack_points = gimli.attack()
print(gimli, weapon, attack_points)
arthur.defend(weapon, attack_points)
print(arthur, arthur.current_life_points)




