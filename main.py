""" main.py """
from gameoflife.game_of_life import GameBoard

from random import random
from time import sleep

import curses as curse

DISPLAY_DELAY = 0.5

def main():
    """ for unittesting purposes only! """
    width = 20
    height = 20
    testBoard = GameBoard(width, height)
    testBoard.random_state()
    stdScr = curse.initscr()
    curse.noecho()
    curse.cbreak()
    while True:
        testBoard.next_board_state()
        msg = testBoard.render_board()
        try:
            stdScr.addstr(0, 0, msg)
            stdScr.refresh()
            sleep(0.5)
        finally:
            curse.echo()
            curse.nocbreak()
            curse.endwin()
        


if __name__ == '__main__':
    main()
