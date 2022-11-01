from brain_games.cli import run_game
from brain_games.games.calc import calc


def main():
    run_game(
        'What is the result of the expression?',
        calc
    )


if __name__ == '__main__':
    main()
