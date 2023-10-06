import numpy as np
from player import Player
from util import clear_console

# set ANSI codes for X player as red
RED_TEXT = "\033[91m"
RED_BG = "\033[41m"
# set ANSI codes for O player as blue
BLUE_TEXT = "\033[94m"
BLUE_BG = "\033[44m"
# set ANSI code for the numbers
DARK_GREY_TEXT = "\033[40;90m"
# set ANSI code to reset colors
RESET = "\033[0m"

# todo: add parameter boolean to state if winning position
def set_color(val: np.ndarray[str]) -> str:
    """
    Take the string value from an array and change the color depending on the value.
    :param val: (ndarray[str]): The string value from an array to check
    :return: (str) Colored string
    """
    if val == 'X':
        return f"{RED_TEXT}{val}{RESET}"
    elif val == 'O':
        return f"{BLUE_TEXT}{val}{RESET}"
    else:
        return f"{DARK_GREY_TEXT}{val}{RESET}"


# todo: chould i add a paramater 'winner' with a default value of None? if has value (list of indices) use to format
def format_board(current_board: np.ndarray, player1: Player, player2: Player) -> str:
    """
    Takes the current game board array, and both player objects to return a
    formatted string to be used as the gameboard output.
    :param current_board: (ndarray): The current board array to use for creating the string
    :param player1: (Player): Player object to set to player X
    :param player2: (Player): Player object to set to player O
    :return: (str): Formatted gameboard string
    """
    board_string = (
        f"{set_color(current_board[0][0])} | {set_color(current_board[0][1])} | {set_color(current_board[0][2])}"
        f"     {RED_TEXT}{player1.name}{RESET}\n"
        f"---------     Score: {player1.score}\n"
        f"{set_color(current_board[1][0])} | {set_color(current_board[1][1])} | {set_color(current_board[1][2])}\n"
        f"---------     {BLUE_TEXT}{player2.name}{RESET}\n"
        f"{set_color(current_board[2][0])} | {set_color(current_board[2][1])} | {set_color(current_board[2][2])}"
        f"     Score: {player2.score}\n")
    return board_string


def print_board(current_board: np.ndarray, player1: Player, player2: Player):
    clear_console()
    print(f"{format_board(current_board, player1, player2)}")

# todo should i use this function instead as a clear_input_numbers() for when game is over??
# def set_input_numbers(current_board: np.ndarray) -> np.ndarray:
#     """
#     Take the current game board array and set the blank values to the input values for the player input.
#     :param current_board: (ndarray): The current board array to set the input numbers to
#     :return: (ndarray): The array with the input values inserted
#     """
#     updated_board = current_board
#     input_values = np.array([['1', '2', '3'],
#                                 ['4', '5', '6'],
#                                 ['7', '8', '9']])
#     for x in range(len(updated_board)):
#         for y in range(len(updated_board[x])):
#             if updated_board[x][y] == ' ':
#                 updated_board[x][y] = input_values[x][y]
#     return updated_board
