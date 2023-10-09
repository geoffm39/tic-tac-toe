import numpy as np
from typing import Union


class Board:
    """
    Board class represents the gameboard, controlling its state and providing values to other classes and modules.
    """
    def __init__(self):
        """
        Constructor for the Board class, assigning the starting numpy array for the board object.
        """
        self.array = np.array([['1', '2', '3'],
                               ['4', '5', '6'],
                               ['7', '8', '9']], dtype=object)

    def get_position(self, position_num: str) -> Union[tuple, None]:
        """
        Takes a string value to find the index of that value in the array.
        :param position_num: (str): value of the array position
        :return: (tuple, None): returns the index values of the poistion as a tuple, or None if no
         position exists with that value
        """
        row, col = np.where(self.array == position_num)
        if len(row) > 0:
            return row[0], col[0]
        else:
            return None

    def is_position(self, position_num: str) -> bool:
        """
        Checks if the value is in the gameboard array.
        :param position_num: (str): the value to check
        :return: (bool): True if the value is in the array
        """
        if self.get_position(position_num):
            return True
        else:
            return False

    def set_position(self, position_num: str, player_num: int) -> None:
        """
        Sets the position in the array with the value to the chosen player.
        :param position_num: (str):
        :param player_num:
        :return:
        """
        row, col = self.get_position(position_num)
        if player_num == 1:
            self.array[row][col] = 'X'
        else:
            self.array[row][col] = 'O'

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

    def is_board_full(self) -> bool:
        for x in range(len(self.array)):
            for y in range(len(self.array[x])):
                if self.array[x][y] != 'X' and self.array[x][y] != 'O':
                    return False
        return True

    def clear_board(self) -> None:
        self.array = np.array([['1', '2', '3'],
                               ['4', '5', '6'],
                               ['7', '8', '9']], dtype=object)

    def get_board(self) -> np.ndarray:
        return np.copy(self.array)
