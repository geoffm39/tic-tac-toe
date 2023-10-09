"""
The gameboard module is used to format the gameboard state and scores for the console output.
"""

import numpy as np
from player import Player
from util import clear_console

# set ANSI code for white text
WHITE_TEXT = "\033[97m"
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
def set_color(current_board: np.ndarray, winning_positions: list = None) -> np.ndarray:
    """
    Take the current board and format the values to the appropriate color text and background.
    :param current_board: (ndarray): The array of the current board state
    :param winning_positions: (list): A list of tuples representing the winning position
    indices of the array. Default is None
    :return: (str): The array with the formatted string objects
    """
    current_board = current_board
    for x in range(len(current_board)):
        for y in range(len(current_board[x])):
            if winning_positions:
                if (x, y) in winning_positions:
                    if current_board[x][y] == 'X':
                        current_board[x][y] = f"{RED_BG}{WHITE_TEXT}{current_board[x][y]}{RESET}"
                    else:
                        current_board[x][y] = f"{BLUE_BG}{WHITE_TEXT}{current_board[x][y]}{RESET}"
                else:
                    if current_board[x][y] == 'X':
                        current_board[x][y] = f"{RED_TEXT}{current_board[x][y]}{RESET}"
                    elif current_board[x][y] == 'O':
                        current_board[x][y] = f"{BLUE_TEXT}{current_board[x][y]}{RESET}"
                    else:
                        current_board[x][y] = f"{DARK_GREY_TEXT}{current_board[x][y]}{RESET}"
            else:
                if current_board[x][y] == 'X':
                    current_board[x][y] = f"{RED_TEXT}{current_board[x][y]}{RESET}"
                elif current_board[x][y] == 'O':
                    current_board[x][y] = f"{BLUE_TEXT}{current_board[x][y]}{RESET}"
                else:
                    current_board[x][y] = f"{DARK_GREY_TEXT}{current_board[x][y]}{RESET}"
    return current_board


def format_board(current_board: np.ndarray, player1: Player, player2: Player, winning_positions: list = None) -> str:
    """
    Takes the current game board array, and both player objects to return a
    formatted string to be used as the gameboard output using ANSI colors.
    :param current_board: (ndarray): The current board array to use for creating the string
    :param player1: (Player): Player object to set to player X
    :param player2: (Player): Player object to set to player O
    :param winning_positions: (list): List of tuples representing the winning positions on the array
    :return: (str): Formatted gameboard string
    """
    current_board = set_color(current_board, winning_positions)
    board_string = (
        f"{current_board[0][0]} | {current_board[0][1]} | {current_board[0][2]}"
        f"     {RED_TEXT}{player1.name}{RESET}\n"
        f"---------     Score: {player1.score}\n"
        f"{current_board[1][0]} | {current_board[1][1]} | {current_board[1][2]}\n"
        f"---------     {BLUE_TEXT}{player2.name}{RESET}\n"
        f"{current_board[2][0]} | {current_board[2][1]} | {current_board[2][2]}"
        f"     Score: {player2.score}\n")
    return board_string


def print_board(current_board: np.ndarray, player1: Player, player2: Player, winning_positions=None) -> None:
    """
    Clear the console then print the formatted gameboard along with scores
    :param current_board: (ndarray): array of current board state
    :param player1: (Player): player 1 object
    :param player2: (Player): payer 2 object
    :param winning_positions: (list): List of tuples representing the winning positions on the array
    :return:
    """
    clear_console()
    print(f"{format_board(current_board, player1, player2, winning_positions)}")
