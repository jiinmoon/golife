""" main.py """
from gameoflife.game_of_life import GameBoard

from random import random


def main():
    """ for unittesting purposes only! """
    width = 10
    height = 10
    testBoard = GameBoard(width, height)
    testBoard.random_state()
    print(testBoard.render_board())
    testBoard.next_board_state()
    print(testBoard.render_board())


if __name__ == '__main__':
    main()
