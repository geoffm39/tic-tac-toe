import numpy


class Board:
    def __init__(self):
        self.board_array = numpy.array([[' ', ' ', ' '],
                                        [' ', ' ', ' '],
                                        [' ', ' ', ' ']])

    def set_position(self, row, col, val):
        self.board_array[row][col] = val
