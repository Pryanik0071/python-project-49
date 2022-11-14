from brain_games import cli


ROUNDS_NUMBER = 3


def run_game(game):
    name = cli.welcome_user()
    status = True
    print(game.RULES)
    for _ in range(ROUNDS_NUMBER):
        question, correct_answer = game.game()
        print(f'Question: {question}')
        if not (status := is_correct_answer(correct_answer)):
            break
        print('Correct!')
    cli.end_game_message(status, name)


def is_correct_answer(correct_answer: str) -> True or False:
    """Check answer with correct_answer and return True or False"""
    if (answer := cli.answer_message()) != correct_answer:
        cli.wrong_answer_message(answer, correct_answer)
        return False
    return True
