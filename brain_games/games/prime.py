import prompt
from random import randint


def brain_prime():
    number = randint(1, 100)
    print('Question:', number)
    answer = prompt.string('Your answer: ')
    k = 0
    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            k += 1
    if k == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        return False
