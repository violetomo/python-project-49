import prompt
from random import randint


def brain_calc():
    number1 = randint(1, 10)
    number2 = randint(1, 10)
    operations = ['+', '-', '*']
    operation = operations[randint(0, 2)]
    correct_answer = str(eval(str(number1) + operation + str(number2)))
    print(f'Question: {number1} {operation} {number2}')
    answer = prompt.string('Your answer: ')
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        return False
