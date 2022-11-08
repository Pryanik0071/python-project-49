#!/usr/bin/env python3
from brain_games.funcs import run_game
from brain_games.games.even import even


def main():
    """brain-even game"""
    welcome_message = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_game(welcome_message, even)


if __name__ == '__main__':
    main()
