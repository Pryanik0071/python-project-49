import prompt

from brain_games.cli import question_message
from brain_games.funcs import get_random_number, check_answer


def progression():
    len_progression = get_random_number(5, 10)
    start = get_random_number()
    step = get_random_number(1)
    index = get_random_number(0, len_progression - 1)
    progression_list = []
    i = 0
    while i < len_progression:
        progression_list.append(str(start + step * i))
        i += 1
    correct_answer = progression_list[index]
    progression_list[index] = '..'
    progression_ = ' '.join([str(_) for _ in progression_list])
    question_message(f'{progression_}')
    answer = prompt.integer('Your answer: ')
    return check_answer(answer, int(correct_answer))
