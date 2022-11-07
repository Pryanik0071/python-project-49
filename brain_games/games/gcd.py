from math import gcd as math_gcd
from random import randint

import prompt

from brain_games.cli import lose_message


def gcd(name):
    min_number, max_number = 1, 100
    a = randint(min_number, max_number)
    b = randint(min_number, max_number)
    print('Question:', a, b)
    answer = prompt.integer('Your answer: ')
    if answer != (correct_answer := math_gcd(a, b)):
        lose_message(
            answer=answer,
            correct_answer=correct_answer,
            name=name
        )
        return
    return True
