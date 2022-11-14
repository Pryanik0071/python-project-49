from math import gcd as math_gcd

from brain_games.cli import question_message, answer_message
from brain_games.core import get_random_number, check_answer


RULES = 'Find the greatest common divisor of given numbers.'


def game():
    a = get_random_number()
    b = get_random_number()
    question_message(f'{a} {b}')
    answer = answer_message(int)
    return check_answer(answer, math_gcd(a, b))
