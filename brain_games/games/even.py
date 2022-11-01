from random import randint


import prompt


from brain_games.cli import lose_message


def even(name):
    min_number, max_number = 1, 399
    print(f'Question {(number := randint(min_number, max_number))}')
    answer = prompt.string('Your answer: ')
    if answer == (correct_answer := ('yes', 'no')[number % 2]):
        print('Correct!')
    else:
        lose_message(
            answer=answer,
            correct_answer=correct_answer,
            name=name
        )
        return
    return True
