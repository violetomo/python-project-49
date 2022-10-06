import prompt
from random import randint


def brain_progression():
    factor = randint(2, 11)
    progression = [i for i in range(randint(1, 11), 100, factor)]
    cut_progression = progression[0:randint(5, 11)]
    random_index = randint(0, len(cut_progression) - 1)
    correct_answer = str(cut_progression[random_index])
    cut_progression[random_index] = '..'
    print('Question:', " ".join(map(str, cut_progression)))
    answer = prompt.string('Your answer: ')
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        return False
