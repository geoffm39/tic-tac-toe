import numpy


class Board:
    def __init__(self):
        self.array = numpy.array([[' ', ' ', ' '],
                                  [' ', ' ', ' '],
                                  [' ', ' ', ' ']])

    #  todo SHOULD THERE BE A GET FUNCTION AS WELL??
    def check_position(self, position_num) -> tuple:
        # indices = numpy.where(self.array == position_num)
        # print(indices)
        # if len(indices) > 0:
        #     print(f'{indices[0]}{indices[1]}')
        row, col = numpy.where(self.array == position_num)
        if len(row) > 0:
            return row[0], col[0]

    def set_position(self, row, col, player_num):
        if player_num == 1:
            self.array[row][col] = 'X'
        else:
            self.array[row][col] = 'O'
