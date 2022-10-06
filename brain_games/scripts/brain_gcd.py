#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.games.gcd import brain_gcd


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    correct_answers = 0
    while correct_answers <= 2:
        answer = brain_gcd()
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
