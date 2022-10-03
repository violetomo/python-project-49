#!/usr/bin/env python3

from brain_games.cli import welcome_user
import prompt
from random import randint


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    right_answers = 0
    while right_answers <= 2:
        number = randint(1, 100)
        print('Question: ', number)
        answer = prompt.string('')
        if answer == 'yes' and number % 2 == 0 or answer == 'no' and number % 2 == 1:
            print('Correct!')
            right_answers += 1
            next
        else:
            if answer == 'yes':
                print("'yes' is wrong answer ;(. Correct answer was 'no'. Let's try again, " + name + "!")
            elif answer == 'no':
                print("'no' is wrong answer ;(. Correct answer was 'yes'. Let's try again, " + name + "!")
            else:
                print("'" + answer + "'" + " is wrong answer ;(. Let's try again, " + name + "!")
            break
    if right_answers == 3:
        print('Congratulations, ' + name + '!')


if __name__ == '__main__':
    even_or_not()
