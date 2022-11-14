from brain_games.cli import question_message, answer_message
from brain_games.core import get_random_number, check_answer, is_prime


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game():
    number = get_random_number()
    question_message(number)
    answer = answer_message(str)
    return check_answer(answer, ('no', 'yes')[is_prime(number)])
