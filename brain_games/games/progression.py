from brain_games.cli import question_message, answer_message
from brain_games.core import (get_random_number,
                              check_answer,
                              get_random_progression)


MIN_LEN = 5
MAX_LEN = 10


def progression():
    len_progression = get_random_number(MIN_LEN, MAX_LEN)
    index = get_random_number(0, len_progression - 1)
    progression_list = get_random_progression(len_progression)
    correct_answer = int(progression_list[index])
    progression_list[index] = '..'
    progression_str = ' '.join(progression_list)
    question_message(f'{progression_str}')
    answer = answer_message(int)
    return check_answer(answer, correct_answer)
