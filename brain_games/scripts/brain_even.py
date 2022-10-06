#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.games.even import brain_even


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers = 0
    while correct_answers <= 2:
        answer = brain_even()
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
