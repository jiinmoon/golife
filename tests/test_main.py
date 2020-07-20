""" testing suite """
from gameoflife.game_of_life import GameBoard

import pytest

@pytest.fixture()
def test_board():
    # setup
    yield GameBoard()
    # teardown
    #print('Good Bye')

class Test_Game:
    def test_GameBoard_creation_null(self, test_board):
        # test whether board object exist.
        assert test_board and \
                test_board.WIDTH == 0 and \
                test_board.HEIGHT == 0

    def test_GameBoard_creation_init(self):
        # test for correct height and width in new board.
        width = 5
        height = 5
        test_board = GameBoard(width, height)
        assert test_board.WIDTH == width and \
                test_board.HEIGHT == height
        assert test_board.BOARD_STATE == [[0] * width for _ in range(height)]

    def test_GameBoard_dead_state(self, test_board):
        # new values for dead_state() test
        width = 5
        height = 5
        return_board_state = test_board.dead_state(width, height)
        assert test_board.WIDTH == width and \
                test_board.WIDTH == height
        assert return_board_state and \
                return_board_state == [[0] * width for _ in range(height)]

    def test_GameBoard_set_state(self, test_board):
        initial_state = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
        ]
        return_board_state = test_board.set_board(initial_state)
        assert return_board_state == initial_state

    def test_GameBoard_next_state_1(self, test_board):
        initial_state = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        expected_next_state = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        test_board.set_board(initial_state)
        return_next_state = test_board.next_board_state()
        assert return_next_state == expected_next_state

    def test_GameBoard_next_state_1(self, test_board):
        # dead cell with 3 neighbour should become alive.
        initial_state = [
            [0, 0, 1],
            [0, 1, 1],
            [0, 0, 0],
        ]
        expected_next_state = [
            [0, 1, 1],
            [0, 1, 1],
            [0, 0, 0],
        ]
        test_board.set_board(initial_state)
        return_next_state = test_board.next_board_state()
        assert return_next_state == expected_next_state
 
    def test_GameBoard_next_state_2(self, test_board):
        # live cell with 0 or 1 neighbour should become alive.
        initial_state = [
            [1, 0, 1],
            [0, 0, 0],
            [0, 0, 0],
        ]
        expected_next_state = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        test_board.set_board(initial_state)
        return_next_state = test_board.next_board_state()
        assert return_next_state == expected_next_state

    def test_GameBoard_next_state_3(self, test_board):
        # live cell with more than 3 neighbour should die.
        initial_state = [
            [1, 1, 1],
            [0, 1, 1],
            [0, 0, 0],
        ]
        expected_next_state = [
            [1, 0, 1],
            [1, 0, 1],
            [0, 0, 0],
        ]
        test_board.set_board(initial_state)
        return_next_state = test_board.next_board_state()
        assert return_next_state == expected_next_state

    def test_GameBoard_next_next_state_1(self, test_board):
        initial_state = [
            [1, 1, 1],
            [0, 1, 1],
            [0, 0, 0],
        ]
        expected_next_state = [
            [1, 0, 1],
            [1, 0, 1],
            [0, 0, 0],
        ]
        expected_next_next_state = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        test_board.set_board(initial_state)
        return_next_state = test_board.next_board_state()
        return_next_next_state = test_board.next_board_state()
        #print(return_next_state)
        #print(return_next_next_state)
        assert return_next_state == expected_next_state
        assert return_next_next_state == expected_next_next_state
