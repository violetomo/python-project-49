#!/usr/bin/env python3

from brain_games.cli import welcome_user
import prompt
from random import randint


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    correct_answers = 0
    while correct_answers <= 2:
        number1 = randint(1, 10)
        number2 = randint(1, 10)
        operations = ['+', '-', '*']
        operation = operations[randint(0, 2)]
        correct_answer = str(eval(str(number1) + operation + str(number2)))
        print(f'Question: {number1} {operation} {number2}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            correct_answers += 1
            next
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'. Let's try again, {name}!")
            break
    if correct_answers == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
