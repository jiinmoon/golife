""" golife.py

Usage:

    python3 golife.py 

"""

from gameoflife.game_of_life import GameBoard

from random import random
from time import sleep

import argparse
import curses
import json

class Screen():
    def __init__(self):
        self.screen = curses.initscr()
        self.y, self.x = self.screen.getmaxyx()
        curses.noecho()
        curses.nocbreak()

    def display(self, msg):
        self.screen.addstr(0, 0, msg)
        self.screen.refresh()

    def clean_up(self):
        curses.echo()
        curses.nocbreak()
        curses.endwin()


def create_parser():
    parser = argparse.ArgumentParser(
            description="simulates Game of Life"
    )
    # positional argument
    parser.add_argument(
            "mode",
            choices=["random", "template", "gif"],
            help="specify running mode"
    )
    # optional argument
    parser.add_argument(
            "--width",
            type=int,
            help="specify the width of the board"
    )
    parser.add_argument(
            "--height",
            type=int,
            help="specify the height of the board"
    )
    parser.add_argument(
            "--path",
            help="specify the path of template file"
    )
    parser.add_argument(
            "--out",
            help="Specify the name of output .gif file"
    )
    return parser

def evaluate_running_mode(args):
    # which mode is it running?
    if args.mode == "random":
        run_in_random_mode(args)
    elif args.mode == "template":
        run_in_template_mode(args)
    else:
        run_in_gif_mode(args)

def run_in_random_mode(args):
    """ continuously run in random mode """
    stdScr = Screen()
    width = 5
    height = 5
    if args.width and (1 <= args.width < stdScr.x):
        width = args.width
    if args.height and (1 <= args.height < stdScr.y):
        height = args.height
    testBoard = GameBoard(width, height)
    testBoard.random_state()
    display_to_terminal(stdScr, testBoard)

def is_valid_template_board(board, max_height, max_width):
    template_height = len(board)
    template_width = len(board[0])
    return (1 <= template_height < max_height) and \
            (1 <= template_width < max_width)

def display_to_terminal(stdScr, testBoard):
    while True:
        testBoard.next_board_state()
        msg = testBoard.render_board()
        try:
            stdScr.display(msg)
            sleep(0.5)
        finally:
            stdScr.clean_up()

def run_in_template_mode(args):
    """ continuously run with the given template board. """
    stdScr = Screen()
    template_board = None
    if not args.path:
        print("Path to a template is required. Refer to usage.")
        stdScr.clean_up()
        exit()

    with open(args.path, 'r') as f:
        template_json = json.load(f)
        template_board = template_json["template"]
    
    if not is_valid_template_board(template_board, stdScr.x, stdScr.y):
        print("invalid template format or " + \
                "template exceeds height/width limit.")
        stdScr.clean_up()
        exit()

    testBoard = GameBoard()
    testBoard.set_board(template_board)
    display_to_terminal(stdScr, testBoard) 

def run_in_gif_mode(args):
    """ export outputin .gif for specified duration. """
    pass

def main():
    parser = create_parser()
    args = parser.parse_args()
    evaluate_running_mode(args)


if __name__ == '__main__':
    main()
