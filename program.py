import actors
import random

from actors import Wizard, Creatures


def main():
    print_header()
    game_loop()


def print_header():
    print('--------------------------------')
    print('         Wizard Game \o/        ')
    print('--------------------------------')
    print()


def game_loop():

    creatures = [
        Creatures('Toad', 1),
        Creatures('Tiger', 12),
        Creatures('Bat', 3),
        Creatures('Dragon', 50),
        Creatures('Evil Wizard', 99)
    ]

    hero = Wizards('Gandolf', 75)

    while True:

        active_creature = random.choice(creatures)
        print("A {} of level {}  has appear from a dark and foggy forest ... .. .".format(
            active_creature.name, active_creature.level))
        print()

        cmd = input('Do you [a]ttack, [r]unaway, or look [a]round?')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print('Game Over !!!')
                break

        elif cmd == 'r':
            print('run away')
        elif cmd == 'l':
            print('look around')
        else:
            print('OK, we are exiting the game... bye bye')
            break


if __name__ == '__main__':
    main()
