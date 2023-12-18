#!/usr/bin/env/python

from brain_games.games import calc_game
from brain_games.logic_brain import play_game

def main():
    play_game(calc_game)


if __name__ == '__main__':
    main()