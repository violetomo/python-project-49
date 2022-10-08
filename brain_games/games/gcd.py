from random import randint
from math import gcd


def brain_gcd():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    print('Question:', number1, number2)
    correct_answer = str(gcd(number1, number2))
    return correct_answer
