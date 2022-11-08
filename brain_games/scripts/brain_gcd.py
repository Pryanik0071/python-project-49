#!/usr/bin/env python3
from brain_games.funcs import run_game
from brain_games.games.gcd import gcd


def main():
    """brain-gcd game"""
    welcome_message = 'Find the greatest common divisor of given numbers.'
    run_game(welcome_message, gcd)


if __name__ == '__main__':
    main()
