from random import randint

from brain_games.cli import (welcome_user,
                             wrong_answer_message,
                             end_game_message)


MIN_NUMBER = 1
MAX_NUMBER = 100
ROUNDS_NUMBER = 3


def run_game(game_message: str, game):
    name = welcome_user()
    status = True
    print(game_message)
    for _ in range(ROUNDS_NUMBER):
        status = game()
        if not status:
            break
        print('Correct!')
    end_game_message(status, name)


def get_random_number(min_number: int = MIN_NUMBER,
                      max_number: int = MAX_NUMBER) -> int:
    """Return random number from range(min_number to max_number)"""
    return randint(min_number, max_number)


def check_answer(answer, correct_answer) -> True or None:
    """Check answer with correct_answer and return True or False"""
    if answer != correct_answer:
        wrong_answer_message(answer, correct_answer)
        return
    return True


def is_prime(number: int) -> True or False:
    """Return True if number is prime, else return False"""
    for _ in range(2, int(number ** 0.5 + 1)):
        if number % _ == 0:
            return False
    return True


def get_random_progression(len_: int) -> list:
    """Returns a random progression of given length"""
    start = get_random_number()
    step = get_random_number(1)
    i = 0
    progression_list = []
    while i < len_:
        progression_list.append(str(start + step * i))
        i += 1
    return progression_list
