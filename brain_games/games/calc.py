from random import randint


def brain_calc():
    number1 = randint(1, 10)
    number2 = randint(1, 10)
    operations = ['+', '-', '*']
    operation = operations[randint(0, 2)]
    correct_answer = str(eval(str(number1) + operation + str(number2)))
    print(f'Question: {number1} {operation} {number2}')
    return correct_answer
