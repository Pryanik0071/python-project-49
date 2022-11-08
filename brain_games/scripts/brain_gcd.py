#!/usr/bin/env python3
from brain_games.core import run_game
from brain_games.games.gcd import gcd


def main():
    """brain-gcd game"""
    message = 'Find the greatest common divisor of given numbers.'
    run_game(message, gcd)


if __name__ == '__main__':
    main()
