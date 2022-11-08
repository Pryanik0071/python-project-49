#!/usr/bin/env python3
from brain_games.funcs import run_game
from brain_games.games.prime import prime


def main():
    """brain-prime game"""
    run_game(
        'Answer "yes" if given number is prime. Otherwise answer "no".',
        prime
    )


if __name__ == '__main__':
    main()
