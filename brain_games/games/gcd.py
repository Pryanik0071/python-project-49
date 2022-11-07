from math import gcd as math_gcd

import prompt

from brain_games.cli import question_message
from brain_games.funcs import get_random_number, check_answer


def gcd():
    a = get_random_number()
    b = get_random_number()
    question_message(f'{a} {b}')
    answer = prompt.integer('Your answer: ')
    return check_answer(answer, math_gcd(a, b))
