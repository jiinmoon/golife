""" main.py """
from random import random

class GameBoard:
    def __init__(self, width=0, height=0):
        self.WIDTH = width
        self.HEIGHT = height
        self.BOARD_STATE = [[0] * width for _ in range(height)]

    def dead_state(self, width=0, height=0):
        """ 
        Resets the board state with given width and height. If the width and
        height is not specified or 0, then previous values are retained.

        Returns non-trival dead state of size width * height 
        """
        if width and height:
            self.WIDTH = width
            self.HEIGHT = height
        self.BOARD_STATE = [[0] * width for _ in range(height)]
        return self.BOARD_STATE

    def _get_random_cell_state(self):
        return int(random() < 0.5)

    def random_state(self):
        """
        Randomizes the board state.

        Returns randomized board state.
        """
        for row in range(self.HEIGHT):
            for col in range(self.WIDTH):
                self.BOARD_STATE[row][col] = self._get_random_cell_state()
        return self.BOARD_STATE

    def render_board(self):
        """
        Renders the current board state for human readable format.

        Returns board state in pretty print format.
        """
        top_bottom = '+' + '-' * self.WIDTH + '+' + '\n'
        mid = []
        trans_table = {'0': ' ', '1': '#'}
        for row in range(self.HEIGHT):
            current_row = self.BOARD_STATE[row]
            current_row = ''.join(map(lambda x: str(x), current_row))
            current_row = current_row.translate(trans_table)
            current_row = '|' + current_row + '|' + '\n'
            mid.append(current_row)
        return top_bottom + ''.join(mid) + top_bottom

def main():
    """ for unittesting! """
    width = 25
    height = 25
    testBoard = GameBoard(width, height)
    print(testBoard.render_board())
    testBoard.random_state()
    print(testBoard.render_board())

if __name__ == '__main__':
    main()
