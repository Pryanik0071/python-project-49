from random import randint

RULES = 'What number is missing in the progression?'
MIN_NUMBER = 1
MAX_NUMBER = 100
MIN_LEN = 5
MAX_LEN = 10
MAX_STEP = 25


def get_progression(len_progression: int, start: int, step: int) -> list:
    """Returns a progression of given length"""
    i = 0
    progression = []
    while i < len_progression:
        progression.append(str(start + step * i))
        i += 1
    return progression


def get_question_and_correct_answer():
    len_progression = randint(MIN_LEN, MAX_LEN)
    start = randint(MIN_NUMBER, MAX_NUMBER)
    step = randint(1, MAX_STEP)
    index = randint(0, len_progression - 1)
    progression = get_progression(len_progression, start, step)
    correct_answer = progression[index]
    progression[index] = '..'
    progression_str = ' '.join(progression)
    return progression_str, correct_answer
