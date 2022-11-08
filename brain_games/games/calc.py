from random import choice
import operator

from brain_games.cli import question_message, answer_message
from brain_games.core import get_random_number, check_answer


def calc():  # noqa: C901
    operations = {
        '-': operator.sub,
        '+': operator.add,
        '*': operator.mul
    }
    a = get_random_number()
    b = get_random_number()
    operation = choice(list(operations.keys()))
    question_message(f'{a} {operation} {b}')
    answer = answer_message(int)
    return check_answer(answer, operations[operation](a, b))
