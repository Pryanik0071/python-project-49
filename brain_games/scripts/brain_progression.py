#!/usr/bin/env python3
from brain_games.funcs import run_game
from brain_games.games.progression import progression


def main():
    """brain-progression game"""
    message = 'What number is missing in the progression?'
    run_game(message, progression)


if __name__ == '__main__':
    main()
