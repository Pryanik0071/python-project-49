import prompt


NUMBER_OF_ROUNDS = 3


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULE)
    for _ in range(NUMBER_OF_ROUNDS):
        question, correct_answer = game.get_question_and_correct_answer()
        print(f'Question: {question}')
        if (answer := prompt.string('Your answer: ')) != correct_answer:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            break
        print('Correct!')
    else:
        print(f'Congratulations, {name}!')
