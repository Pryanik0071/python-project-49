import prompt

from brain_games.cli import lose_message, question_message
from brain_games.funcs import get_random_number


def even(name):
    number = get_random_number()
    question_message(number)
    answer = prompt.string('Your answer: ')
    if answer != (correct_answer := ('yes', 'no')[number % 2]):
        lose_message(
            answer=answer,
            correct_answer=correct_answer,
            name=name
        )
        return
    return True
