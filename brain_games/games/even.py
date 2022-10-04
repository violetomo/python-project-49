import prompt
from random import randint


def brain_even():
    number = randint(1, 100)
    print('Question: ', number)
    answer = prompt.string('Your answer: ')
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        return False
