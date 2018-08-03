
def main():
    print_header()
    game_loop()


def print_header():
    print('--------------------------------')
    print('         Wizard Game \o/        ')
    print('--------------------------------')
    print()


def game_loop():

    while True:
        cmd = input('Do you [a]ttack, [r]unaway, or look [a]round?')
        if cmd == 'a':
            print('attack')
        elif cmd == 'r':
            print('run away')
        elif cmd == 'l':
            print('look around')
        else:
            print('OK, we are exiting the game... bye bye')
            break


if __name__ == '__main__':
    main()
