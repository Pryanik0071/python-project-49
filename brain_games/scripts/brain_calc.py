#!/usr/bin/env python3
from brain_games.funcs import run_game
from brain_games.games.calc import calc


def main():
    """brain-calc game"""
    run_game(
        'What is the result of the expression?',
        calc
    )


if __name__ == '__main__':
    main()
