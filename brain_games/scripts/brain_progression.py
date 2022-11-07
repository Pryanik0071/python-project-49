#!/usr/bin/env python3
from brain_games.funcs import run_game
from brain_games.games.progression import progression


def main():
    """brain-progression game"""
    run_game(
        'What number is missing in the progression?',
        progression
    )


if __name__ == '__main__':
    main()
