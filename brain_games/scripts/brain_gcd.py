#!/usr/bin/env python3
from brain_games.funcs import run_game
from brain_games.games.gcd import gcd


def main():
    """brain-gcd game"""
    run_game(
        'Find the greatest common divisor of given numbers.',
        gcd
    )


if __name__ == '__main__':
    main()
