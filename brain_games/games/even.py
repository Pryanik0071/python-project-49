from random import randint


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_even(number: int) -> True or False:
    """Return True if number is even, else return False"""
    return not bool(number % 2)


def game():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_even(number) else 'no'
    return str(number), correct_answer
