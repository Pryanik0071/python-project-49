from random import randint

import prompt

from brain_games.cli import welcome_user


def even(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        print(f'Question {(number := randint(1, 399))}')
        answer = prompt.string('Your answer: ')
        if answer == (correct_answer := ('yes', 'no')[number % 2]):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')


def main():
    name = welcome_user()
    even(name)


if __name__ == '__main__':
    main()
