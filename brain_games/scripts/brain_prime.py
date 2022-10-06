#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.games.prime import brain_prime


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    correct_answers = 0
    while correct_answers <= 2:
        answer = brain_prime()
        if answer == True:
            correct_answers += 1
            next
        else:
            print(f"Let's try again, {name}!")
            break
    if correct_answers == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
