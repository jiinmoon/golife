""" unittests """
from gameoflife.game_of_life import GameBoard

def test_GameBoard_creation():
    # test whether board object exist.
    TestBoard = GameBoard()
    assert TestBoard and \
            TestBoard.WIDTH == 0 and \
            TestBoard.HEIGHT == 0

    # test for correct height and width.
    width = 5
    height = 5
    TestBoard = GameBoard(width, height)
    assert TestBoard.WIDTH == width and \
            TestBoard.HEIGHT == height
    assert TestBoard.BOARD_STATE == [[0] * width for _ in range(height)]

    # new values for dead_state() test
    width = 4
    height = 4
    return_board_state = TestBoard.dead_state(width, height)
    assert TestBoard.WIDTH == width and \
            TestBoard.WIDTH == height
    assert return_board_state and \
            return_board_state == [[0] * width for _ in range(height)]

