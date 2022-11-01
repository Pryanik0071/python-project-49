import random

import prompt

from brain_games.cli import welcome_user


def calc(name):  # noqa: C901
    print('What is the result of the expression?')
    operations = ('-', '+', '*')
    for _ in range(3):
        a, b = random.randint(1, 10), random.randint(1, 10)
        operation = random.choice(operations)
        print('Question:', a, operation, b)
        answer = prompt.integer('Your answer: ')
        if operation == '+':
            if answer == a + b:
                print('Correct!')
            else:
                print(f"'{answer}' is wrong answer ;(. "
                      f"Correct answer was '{a + b}'.")
                print(f"Let's try again, {name}!")
                break
        elif operation == '-':
            if answer == a - b:
                print('Correct!')
            else:
                print(f"'{answer}' is wrong answer ;(. "
                      f"Correct answer was '{a - b}'.")
                print(f"Let's try again, {name}!")
                break
        elif operation == '*':
            if answer == a * b:
                print('Correct!')
            else:
                print(f"'{answer}' is wrong answer ;(. "
                      f"Correct answer was '{a * b}'.")
                print(f"Let's try again, {name}!")
                break
    else:
        print(f'Congratulations, {name}!')


def main():
    name = welcome_user()
    calc(name)


if __name__ == '__main__':
    main()
