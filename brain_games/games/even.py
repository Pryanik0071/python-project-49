from brain_games.cli import question_message, answer_message
from brain_games.funcs import get_random_number, check_answer


def even():
    number = get_random_number()
    question_message(number)
    answer = answer_message(str)
    return check_answer(answer, ('yes', 'no')[number % 2])
