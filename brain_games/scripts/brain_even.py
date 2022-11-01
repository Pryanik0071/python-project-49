from brain_games.cli import run_game
from brain_games.games.even import even


def main():
    run_game(
        'Answer "yes" if the number is even, otherwise answer "no".',
        even
    )


if __name__ == '__main__':
    main()
