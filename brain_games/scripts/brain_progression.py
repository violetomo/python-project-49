#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.games.progression import brain_progression


def main():
    name = welcome_user()
    print('What number is missing in the progression?')
    correct_answers = 0
    while correct_answers <= 2:
        answer = brain_progression()
        if answer is True:
            correct_answers += 1
            next
        else:
            print(f"Let's try again, {name}!")
            break
    if correct_answers == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
