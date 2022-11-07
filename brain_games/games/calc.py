from random import choice
import operator

import prompt

from brain_games.cli import lose_message, question_message
from brain_games.funcs import get_random_number


def calc(name):  # noqa: C901
    operations = {
        '-': operator.sub,
        '+': operator.add,
        '*': operator.mul
    }
    a = get_random_number()
    b = get_random_number()
    operation = choice(list(operations.keys()))
    question_message(f'{a} {operation} {b}')
    answer = prompt.integer('Your answer: ')
    if answer != (correct_answer := operations[operation](a, b)):
        lose_message(
            answer=answer,
            correct_answer=correct_answer,
            name=name
        )
        return
    return True
