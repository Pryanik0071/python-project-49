import prompt

from brain_games.cli import question_message
from brain_games.funcs import get_random_number, check_answer


def even():
    number = get_random_number()
    question_message(number)
    answer = prompt.string('Your answer: ')
    return check_answer(answer, ('yes', 'no')[number % 2])
