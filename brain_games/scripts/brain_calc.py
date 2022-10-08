#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.logic import game_logic
from brain_games.games.calc import brain_calc


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    result = game_logic(brain_calc)
    if result is True:
        print(f'Congratulations, {name}!')
    else:
        print(f'Let\'s try again, {name}!')


if __name__ == '__main__':
    main()
