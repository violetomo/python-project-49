#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.logic import game_logic
from brain_games.games.prime import brain_prime


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    result = game_logic(brain_prime)
    if result is True:
        print(f'Congratulations, {name}!')
    else:
        print(f'Let\'s try again, {name}!')


if __name__ == '__main__':
    main()
