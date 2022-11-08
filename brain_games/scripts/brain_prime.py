#!/usr/bin/env python3
from brain_games.funcs import run_game
from brain_games.games.prime import prime


def main():
    """brain-prime game"""
    welcome_message = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    run_game(welcome_message, prime)


if __name__ == '__main__':
    main()
