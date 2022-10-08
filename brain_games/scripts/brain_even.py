#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.logic import game_logic
from brain_games.games.even import brain_even


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    result = game_logic(brain_even)
    if result is True:
        print(f'Congratulations, {name}!')
    else:
        print(f'Let\'s try again, {name}!')


if __name__ == '__main__':
    main()
