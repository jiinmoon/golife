""" main.py """


class GameBoard:
    def __init__(self):
        self.WIDTH = 0
        self.HEIGHT = 0
        self.BOARD_STATE = []

    def dead_state(self, width, height):
        """ returns non-trival dead state of size width * height """
        self.BOARD_STATE = [[0] * width for _ in range(height)]
        return self.BOARD_STATE

