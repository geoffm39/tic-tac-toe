import random

from art import logo
from gameboard import print_board
from board import Board
from player import Player
from util import clear_console


board = Board()
current_player = None

logo()
print("Welcome to Tic-Tac-Toe!")
print("Player 1 is 'X' and Player 2 is 'O'.")
print("The starting player is random!")
if input("1 player or 2 player game? (1/2)") == '1':
    player1 = Player(input("Enter first player's name: "), False)
    player2 = Player('CPU', True)
else:
    player1 = Player(input("Enter first player's name: "), False)
    player2 = Player(input("enter second player's name: "), False)
# todo: NEED RESPONSE AND LOOP HERE IF NOT 1 OR 2 SELECTED
# TODO: I THINK MAYBE MAKE METHODS WITH RECURSION FOR THESE CHOICES (INCLUDING BELLOW)
# TODO: PERHAPS SOME KIND OF TEMPLATE????

continue_playing = True
while continue_playing:
    if random.randint(1, 2) == 1:
        current_player = 1
    else:
        current_player = 2
    winner = False
    while not winner:
        print_board(board.array, player1, player2)
        print(f"Player {current_player}, it's your move!")
        choice = input("Pick an available number: ")
        choosing_position = True
        while choosing_position:
            if board.is_position(choice):
                choosing_position = False
                board.set_position(choice, current_player)
                if winning_positions := board.get_winning_positions():
                    winner = True
                    if current_player == 1:
                        player1.increase_score()
                    else:
                        player2.increase_score()
                    print_board(board.array, player1, player2, winning_positions)
                    print(f"Player {current_player} has won the round!")
                    making_choice = True
                    while making_choice:
                        another_game = input("Play another round? (y/n)").lower()
                        if another_game == 'y':
                            board.clear_board()
                            making_choice = False
                        elif another_game == 'n':
                            clear_console()
                            print(f"Final Scores:\nPlayer 1: {player1.score}\nPlayer 2: {player2.score}")
                            if player1.score > player2.score:
                                print("Player 1 Wins!")
                            elif player1.score < player2.score:
                                print("Player 2 Wins!")
                            else:
                                print("It was a draw!")
                            making_choice = False
                            continue_playing = False
                        else:
                            clear_console()
                            print("Invalid response. Try again.")
                else:
                    print_board(board.array, player1, player2)
                    if current_player == 1:
                        current_player = 2
                    else:
                        current_player = 1
            else:
                print_board(board.array, player1, player2)
                print(f"Player {current_player}, that is not a valid move!")
                choice = input("Pick an available number: ")
