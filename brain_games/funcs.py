from random import randint

from brain_games.cli import welcome_user, lose_message


MIN_NUMBER = 1
MAX_NUMBER = 100
ROUNDS_NUMBER = 3


def get_random_number(min_number=MIN_NUMBER, max_number=MAX_NUMBER):
    return randint(min_number, max_number)


def check_answer(answer, correct_answer):
    if answer != correct_answer:
        return {
            'status': False,
            'answer': answer,
            'correct_answer': correct_answer
        }
    return {'status': True}


def run_game(game_message, game):
    name = welcome_user()
    print(game_message)
    for _ in range(ROUNDS_NUMBER):
        status = game()
        if not status.get('status'):
            lose_message(
                answer=status.get('answer'),
                correct_answer=status.get('correct_answer'),
                name=name
            )
            break
        print('Correct!')
    else:
        print(f'Congratulations, {name}!')
