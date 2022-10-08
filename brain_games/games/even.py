from random import randint


def brain_even():
    number = randint(1, 100)
    print('Question:', number)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer
