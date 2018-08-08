import actors
import random
import time

from actors import Wizard, Creatures,SmallAnimal


def main():
    print_header()
    game_loop()


def print_header():
    print('--------------------------------')
    print('''         _                  _ 
                     (_)                | |
            __      ___ ______ _ _ __ __| |
            \ \ /\ / / |_  / _` | '__/ _` |
             \ V  V /| |/ / (_| | | | (_| |
              \_/\_/ |_/___\__,_|_|  \__,_|
                
    ''')
    print('         Wizard Game \o/        ')
    print('--------------------------------')
    print()


def game_loop():
    creatures = [
        SmallAnimal('Toad', 1),
        Creatures('Tiger', 12),
        Creatures('Bat', 3),
        Creatures('Dragon', 50),
        Creatures('Evil Wizard', 99)
    ]

    hero = Wizard('Gandolf', 75)

    while True:

        active_creature = random.choice(creatures)

        print("A {} of level {}  has appear from a dark and foggy forest ... .. .".format(
            active_creature.name, active_creature.level))
        print()

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook round?')

        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The Wizard has been knock out !!!")
                # print('Game Over !!!')
                time.sleep(5)
                print("Wizard woke up and ready again")

        elif cmd == 'r':
            print('run away')
        elif cmd == 'l':
            print('the hero {} looks around and see others creatures to attack'.format(
                hero.name
            ))
            for c in creatures:
                print(' * A {} of level {}'.format(c.name, c.level))
        else:
            print('OK, we are exiting the game... bye bye')
            break

        if not creatures:
            print("The wizard has defeated all the creatures")
            break

        print()


if __name__ == '__main__':
    main()
