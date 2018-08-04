import random

class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self,creature):
        print("The Wizard {} attacks {}!".format(
            self.name, creature.name
        ))

        my_roll = random.randint(1, 12) * self.level
        creature_roll = random.randint(1, 12) * creature.level

        print("You roll {}...".format(my_roll))
        print("{} rolls {} ...".format(creature.name,creature_roll))

        if my_roll >= creature_roll:
            print("The wizard has handily defeated {}".format(creature.name))
            return True
        else:
            print("The Wizard has been Defeated by the creature !!!")
            return False

class Creatures:
    def __init__(self, name, level):
        self.name = name
        self.level = level
