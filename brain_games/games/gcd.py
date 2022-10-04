import prompt
from random import randint
from math import gcd


def brain_gcd():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    print('Question: ', number1, number2)
    answer = prompt.string('Your answer: ')
    correct_answer = str(gcd(number1, number2))
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        return False
