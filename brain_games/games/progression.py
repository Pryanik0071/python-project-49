from random import randint

RULES = 'What number is missing in the progression?'
MIN_NUMBER = 1
MAX_NUMBER = 100
MIN_LEN = 5
MAX_LEN = 10
MAX_STEP = 25


def get_random_progression(len_: int) -> list:
    """Returns a random progression of given length"""
    start = randint(MIN_NUMBER, MAX_NUMBER)
    step = randint(1, MAX_STEP)
    i = 0
    progression_list = []
    while i < len_:
        progression_list.append(str(start + step * i))
        i += 1
    return progression_list


def game():
    len_progression = randint(MIN_LEN, MAX_LEN)
    index = randint(0, len_progression - 1)
    progression_list = get_random_progression(len_progression)
    correct_answer = progression_list[index]
    progression_list[index] = '..'
    progression_str = ' '.join(progression_list)
    return f'{progression_str}', correct_answer
