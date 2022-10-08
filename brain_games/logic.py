import prompt


def game_logic(game):
    correct_answers = 0
    while correct_answers <= 2:
        res = game()
        answer = prompt.string('Your answer: ')
        if answer == res:
            correct_answers += 1
            print('Correct!')
            next
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{res}'.")
            break
    if correct_answers == 3:
        return True
