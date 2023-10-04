import numpy


class Board:
    def __init__(self):
        self.array = numpy.array([[' ', ' ', ' '],
                                  [' ', ' ', ' '],
                                  [' ', ' ', ' ']])

    def set_position(self, row, col, val):
        self.array[row][col] = val
