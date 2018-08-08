import random


class Creatures:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return "Creature: {} of level {}".format(
            self.name, self.level
        )

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creatures):

    def attack(self, creature):
        print("The Wizard {} attacks {}!".format(
            self.name, creature.name
        ))

        my_roll = self.get_defensive_roll()
        creature_roll = Creatures.get_defensive_roll()

        print("You roll {}...".format(my_roll))
        print("{} rolls {} ...".format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print("The wizard has handily defeated {}".format(creature.name))
            return True
        else:
            print("The Wizard has been Defeated by the creature !!!")
            return False


class SmallAnimal(Creatures):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll/2