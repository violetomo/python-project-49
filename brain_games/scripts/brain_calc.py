#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.games.calc import brain_calc


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    correct_answers = 0
    while correct_answers <= 2:
        answer = brain_calc()
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
