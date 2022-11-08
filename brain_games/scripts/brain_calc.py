#!/usr/bin/env python3
from brain_games.core import run_game
from brain_games.games.calc import calc


def main():
    """brain-calc game"""
    message = 'What is the result of the expression?'
    run_game(message, calc)


if __name__ == '__main__':
    main()
