#!/usr/bin/env python3
from brain_games.funcs import run_game
from brain_games.games.even import even


def main():
    """brain-even game"""
    run_game(
        'Answer "yes" if the number is even, otherwise answer "no".',
        even
    )


if __name__ == '__main__':
    main()
