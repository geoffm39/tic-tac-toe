"""
Main script for running the game
"""

import random

from art import logo
from gameboard import print_board
from board import Board
from player import Player
from util import clear_console
from ai_player import AiPlayer


board = Board()
ai_player = AiPlayer()
current_player = None

logo()
print("Welcome to Tic-Tac-Toe!")
print("Player 1 is 'X' and Player 2 is 'O'.")
print("The starting player is random!")

while True:  # choose 1 or 2 player
    user_input = input("1 player or 2 player game? (1/2)")
    if user_input == '1':
        player1 = Player(input("Enter first player's name: "), 1, False)
        player2 = Player('CPU', 2, True)
        break
    elif user_input == '2':
        player1 = Player(input("Enter first player's name: "), 1, False)
        player2 = Player(input("enter second player's name: "), 2, False)
        break
    else:
        clear_console()
        print("Invalid input. Try again.")

continue_playing = True
while continue_playing:  # game loop
    if random.randint(1, 2) == 1:  # select a random player to start
        current_player = player1
    else:
        current_player = player2

    game_over = False
    while not game_over:  # match loop
        if not current_player.is_computer:  # human player move
            print_board(board.get_board(), player1, player2)
            print(f"Player {current_player.player_num}, it's your move!")
            choice = input("Pick an available number: ")
            choosing_position = True

            while choosing_position:
                if board.is_position(choice):
                    choosing_position = False
                    board.set_position(choice, current_player.player_num)
                else:
                    print_board(board.get_board(), player1, player2)
                    print(f"Player {current_player.player_num}, that is not a valid move!")
                    choice = input("Pick an available number: ")
        else:  # AI player move
            board.set_position(str(ai_player.get_best_move(board)), current_player.player_num)

        if board.get_winning_positions() is not None or board.is_board_full():  # if match over
            game_over = True
            if winning_positions := board.get_winning_positions():
                if current_player == player1:
                    player1.increase_score()
                else:
                    player2.increase_score()
                print_board(board.get_board(), player1, player2, winning_positions)
                print(f"Player {current_player.player_num} has won the round!")
            else:
                print_board(board.get_board(), player1, player2)
                print("The round is a draw!")

            while True:
                user_input = input("Play another round? (y/n)").lower()
                if user_input == 'y':
                    board.clear_board()
                    break
                elif user_input == 'n':
                    clear_console()
                    print(f"Final Scores:\n{player1.name}: {player1.score}\n{player2.name}: {player2.score}")
                    if player1.score > player2.score:
                        print(f"{player1.name} Wins!")
                    elif player1.score < player2.score:
                        print(f"{player2.name} Wins!")
                    else:
                        print("It was a draw!")
                    continue_playing = False
                    break
                else:
                    clear_console()
                    print("Invalid input. Try again.")
        else:
            print_board(board.get_board(), player1, player2)
            if current_player == player1:
                current_player = player2
            else:
                current_player = player1
