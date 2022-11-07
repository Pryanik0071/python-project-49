from math import gcd as math_gcd

import prompt

from brain_games.cli import lose_message, question_message
from brain_games.funcs import get_random_number


def gcd(name):
    a = get_random_number()
    b = get_random_number()
    question_message(f'{a} {b}')
    answer = prompt.integer('Your answer: ')
    if answer != (correct_answer := math_gcd(a, b)):
        lose_message(
            answer=answer,
            correct_answer=correct_answer,
            name=name
        )
        return
    return True
