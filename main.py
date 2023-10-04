import numpy
from gameboard import GameBoard

board_array = numpy.array([[' ', ' ', ' '],
                           [' ', ' ', ' '],
                           [' ', ' ', ' ']])

# board = GameBoard(board_array)
#
# board.print_board()
#
# board_array[0][0] = 'X'
#
# board.update_board(board_array)
# board.print_board()


class Test:
    def __init__(self):
        self.board_array = numpy.array([[' ', ' ', ' '],
                                        [' ', ' ', ' '],
                                        [' ', ' ', ' ']])

    def set_pos(self, row, col, val):
        self.board_array[row][col] = val


bob = Test()

# print(bob.board_array)
#
# bob.set_pos(0, 0, 'X')
# print(bob.board_array)

board = GameBoard(bob)
board.print_board()

bob.set_pos(0, 0, 'X')

board.update_board(bob)
board.print_board()