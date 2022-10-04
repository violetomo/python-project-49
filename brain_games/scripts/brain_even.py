#!/usr/bin/env python3

from brain_games.cli import welcome_user
import prompt
from random import randint


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers = 0
    while correct_answers <= 2:
        number = randint(1, 100)
        print('Question: ', number)
        answer = prompt.string('Your answer: ')
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if answer == correct_answer:
            print('Correct!')
            correct_answers += 1
            next
        else:
            print("'" + answer + "'" + ' is wrong answer ;(. Correct answer was ' + "'" + correct_answer + "'" + ". Let's try again, " + name + "!")
            break
    if correct_answers == 3:
        print('Congratulations, ' + name + '!')


if __name__ == '__main__':
    main()
