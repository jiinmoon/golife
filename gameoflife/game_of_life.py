""" main.py """
from random import random

class GameBoard:
    def __init__(self, width=0, height=0):
        self.WIDTH = width
        self.HEIGHT = height
        self.BOARD_STATE = [[0] * width for _ in range(height)]

    def _is_live_cell(self, row, col):
        """
        Checks whether the current cell is alive or dead.

        1. Any live cell with 0 or 1 live neighbors becomes dead.
        2. Any live cell with 2 or 3 live neighbors stays alive.
        3. Any live cell with more than 3 live neighbors becomes dead.
        4. Any live cell with exactly 3 live neighbors becomes alive.

        Returns True is alive; False otherwise.
        """
        is_live = False
        # 9 neighbours to check for each cell.
        candidates = [
                (row-1, col-1), (row-1, col), (row-1, col+1), # top
                (row, col-1), (row, col+1),                 # mid
                (row+1, col-1), (row+1, col), (row+1, col+1)  # bottom 
        ]
        live_neighbours_count = 0 
        for candidate in candidates:
            if not self._is_valid_cell(candidate):
                continue
            r, c = candidate[0], candidate[1]
            if self.BOARD_STATE[r][c]:
                live_neighbours_count += 1

        if (self.BOARD_STATE[row][col] and 2 <= live_neighbours_count <= 3) or \
            (not self.BOARD_STATE[row][col] and live_neighbours_count) == 3:
            is_live = True
        #print(self.BOARD_STATE[row][col], live_neighbours_count, is_live)
        return is_live
        
    def _is_valid_cell(self, candidate):
        row, col = candidate[0], candidate[1]
        return (row >= 0 and row < self.HEIGHT) and \
                (col >= 0 and col < self.WIDTH)
    
    def _get_random_cell_state(self):
        return int(random() < 0.5)


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

    def next_board_state(self):
        """
        Computes the next board state based on current.

        Returns next board state.
        """
        temp_board = [[0] * self.WIDTH for _ in range(self.HEIGHT)]
        for row in range(self.HEIGHT):
            for col in range(self.WIDTH):
                temp_state = 0
                if self._is_live_cell(row, col):
                    temp_state = 1
                temp_board[row][col] = temp_state
        self.BOARD_STATE = temp_board
        return self.BOARD_STATE

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
        trans_table = str.maketrans('01', ' #')
        for row in range(self.HEIGHT):
            current_row = self.BOARD_STATE[row]
            current_row = ''.join(map(lambda x: str(x), current_row))
            current_row = current_row.translate(trans_table)
            current_row = '|' + current_row + '|' + '\n'
            mid.append(current_row)
        return top_bottom + ''.join(mid) + top_bottom

    def set_board(self, board):
        """
        Given a pre-initialized board, set the current board state to match.

        Return new board state matching the given board.
        """
        self.HEIGHT = len(board)
        self.WIDTH = len(board[0])
        self.BOARD_STATE = board
        return self.BOARD_STATE


def main():
    """ for unittesting! """
    width = 10
    height = 10
    testBoard = GameBoard(width, height)
    testBoard.random_state()
    print(testBoard.render_board())
    testBoard.next_board_state()
    print(testBoard.render_board())


if __name__ == '__main__':
    main()
