#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.logic import game_logic
from brain_games.games.progression import brain_progression


def main():
    name = welcome_user()
    print('What number is missing in the progression?')
    result = game_logic(brain_progression)
    if result is True:
        print(f'Congratulations, {name}!')
    else:
        print(f'Let\'s try again, {name}!')


if __name__ == '__main__':
    main()
