import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def wrong_answer_message(answer, correct_answer):
    print(f"'{answer}' is wrong answer ;(. "
          f"Correct answer was '{correct_answer}'.")


def lose_message(name):
    print(f"Let's try again, {name}!")


def question_message(message):
    print(f"Question: {message}")


def answer_message(type_):
    dict_ = {
        int: prompt.integer,
        str: prompt.string
    }
    return dict_.get(type_)('Test Your answer: ')
