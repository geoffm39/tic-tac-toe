import numpy
import random

from art import logo
from gameboard import print_board
from board import Board
from player import Player


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
