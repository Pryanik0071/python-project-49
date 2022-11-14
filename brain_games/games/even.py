from random import randint


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def game():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    return number, ('yes', 'no')[number % 2]
