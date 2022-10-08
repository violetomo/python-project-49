from random import randint


def brain_prime():
    number = randint(1, 100)
    print('Question:', number)
    k = 0
    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            k += 1
    if k == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer
