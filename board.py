import numpy
from typing import Union

class Board:
    def __init__(self):
        self.array = numpy.array([[' ', ' ', ' '],
                                  [' ', ' ', ' '],
                                  [' ', ' ', ' ']])

    def get_position(self, position_num: str) -> Union[tuple, None]:
        row, col = numpy.where(self.array == position_num)
        if len(row) > 0:
            return row[0], col[0]
        else:
            return None

    def is_position(self, position_num: str) -> bool:
        if self.get_position(position_num):
            return True
        else:
            return False

    def set_position(self, position_num: str, player_num: int) -> None:
        row, col = self.get_position(position_num)
        if player_num == 1:
            self.array[row][col] = 'X'
        else:
            self.array[row][col] = 'O'
