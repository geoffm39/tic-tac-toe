import numpy as np
from typing import Union


class Board:
    def __init__(self):
        self.array = np.array([['1', '2', '3'],
                               ['4', '5', '6'],
                               ['7', '8', '9']], dtype=object)

    def get_position(self, position_num: str) -> Union[tuple, None]:
        row, col = np.where(self.array == position_num)
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

    # def is_winner(self):

    def get_winning_positions(self) -> Union[list, None]:
        if self.array[0][0] == self.array[1][1] and self.array[1][1] == self.array[2][2]:
            return [(0, 0), (1, 1), (2, 2)]
        if self.array[2, 0] == self.array[1][1] and self.array[1][1] == self.array[0, 2]:
            return [(2, 0), (1, 1), (0, 2)]
        for i in range(len(self.array)):
            if np.all(self.array[i, :] == self.array[i, 0]):
                return [(i, 0), (i, 1), (i, 2)]
            if np.all(self.array[:, i] == self.array[0, i]):
                return [(0, i), (1, i), (2, i)]

