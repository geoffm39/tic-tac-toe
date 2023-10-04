from gameboard import print_board
from board import Board
from player import Player

import numpy

board = Board()

board_array = numpy.array([['X', ' ', ' '],
                           [' ', 'O', ' '],
                           [' ', ' ', 'X']])

print(board_array)

player1 = Player('geoff')
player2 = Player('Bob')

print_board(board_array, player1, player2)



