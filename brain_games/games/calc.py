from random import randint, choice
import operator

import prompt

from brain_games.cli import lose_message


def calc(name):  # noqa: C901
    operations = {
        '-': operator.sub,
        '+': operator.add,
        '*': operator.mul
    }
    min_number, max_number = 1, 10
    a = randint(min_number, max_number)
    b = randint(min_number, max_number)
    operation = choice(list(operations.keys()))
    print('Question:', a, operation, b)
    answer = prompt.integer('Your answer: ')
    if answer != (correct_answer := operations[operation](a, b)):
        lose_message(
            answer=answer,
            correct_answer=correct_answer,
            name=name
        )
        return
    return True
