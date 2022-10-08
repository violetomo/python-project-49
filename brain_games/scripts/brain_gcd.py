#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.logic import game_logic
from brain_games.games.gcd import brain_gcd


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    result = game_logic(brain_gcd)
    if result is True:
        print(f'Congratulations, {name}!')
    else:
        print(f'Let\'s try again, {name}!')


if __name__ == '__main__':
    main()
