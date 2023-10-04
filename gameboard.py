# set ANSI codes for X player as red
RED_TEXT = "\033[91m"
RED_BG = "\033[41m"
# set ANSI codes for O player as blue
BLUE_TEXT = "\033[94m"
BLUE_BG = "\033[44m"
# set ANSI code to reset colors
RESET = "\033[0m"


class GameBoard:
    def __init__(self, test):
        board_array = test.board_array
        self.game_board = (f"{board_array[0][0]} | {board_array[0][1]} | {board_array[0][2]}\n"
                           f"---------\n"
                           f"{board_array[1][0]} | {board_array[1][1]} | {board_array[1][2]}\n"
                           f"---------\n"
                           f"{board_array[2][0]} | {board_array[2][1]} | {board_array[2][2]}\n")

    def update_board(self, test):
        board_array = test.board_array
        self.game_board = (f"{board_array[0][0]} | {board_array[0][1]} | {board_array[0][2]}\n"
                           f"---------\n"
                           f"{board_array[1][0]} | {board_array[1][1]} | {board_array[1][2]}\n"
                           f"---------\n"
                           f"{board_array[2][0]} | {board_array[2][1]} | {board_array[2][2]}\n")

    def print_board(self):
        print(self.game_board)
