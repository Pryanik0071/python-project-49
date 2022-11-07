from random import randint


def get_random_number():
    min_number, max_number = 1, 100
    return randint(min_number, max_number)
