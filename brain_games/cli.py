import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def wrong_answer_message(answer, correct_answer):
    print(f"'{answer}' is wrong answer ;(. "
          f"Correct answer was '{correct_answer}'.")


def end_game_message(status: bool, name: str):
    if status:
        print(f"Congratulations, {name}!")
        return
    print(f"Let's try again, {name}!")


def answer_message():
    return prompt.string('Your answer: ')
