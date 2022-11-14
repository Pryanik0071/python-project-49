from math import gcd as math_gcd
from random import randint


RULES = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 100


def game():
    a = randint(MIN_NUMBER, MAX_NUMBER)
    b = randint(MIN_NUMBER, MAX_NUMBER)
    return f'{a} {b}', str(math_gcd(a, b))
