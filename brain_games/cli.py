import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def run_game(game_message, game):
    name = welcome_user()
    rounds_number = 3
    print(game_message)
    for _ in range(rounds_number):
        if not game(name):
            # lose_message(
            #     answer=answer,
            #     correct_answer=correct_answer,
            #     name=name
            # )
            break
        print('Correct!')
    else:
        print(f'Congratulations, {name}!')


def lose_message(answer, correct_answer, name):
    print(f"'{answer}' is wrong answer ;(. "
          f"Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {name}!")


def question_message(message: str) -> None:
    print(f"Question: {message}")
