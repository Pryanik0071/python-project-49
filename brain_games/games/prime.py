from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 50


def is_prime(number: int) -> True or False:
    """Return True if number is prime, else return False"""
    for _ in range(2, int(number ** 0.5 + 1)):
        if number % _ == 0:
            return False
    return True


def game():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    return number, ('no', 'yes')[is_prime(number)]
