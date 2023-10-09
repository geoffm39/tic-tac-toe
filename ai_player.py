from board import Board


class AiPlayer:
    """
    AiPlayer class manages the moves of the AI player in a one player game using a minimax algorithm.
    """
    def __init__(self):
        """
        Constructor for the AiPlayer class, initialising a board object to use for the minimax algorithm
        """
        self.board = Board()

    def update_board(self, board: Board) -> None:
        """
        Update the board state to the current gameboard.
        :param board: (Board): current gameboard object to copy
        :return: None
        """
        self.board.array = board.get_board()

    def evaluate_board(self) -> int:
        """
        Evaluates the winning positions, returning the evaluation value depending on the winner or a draw
        :return: (int): The integer value representing the score for that board state relative to the AI player
        """
        if winning_positions := self.board.get_winning_positions():
            if self.board.array[winning_positions[0][0]][winning_positions[0][1]] == 'O':
                return 10
            elif self.board.array[winning_positions[0][0]][winning_positions[0][1]] == 'X':
                return -10
        else:
            return 0

    def get_available_positions(self) -> list:
        """
        Get a list of the available positions on the current board
        :return: (list): A list of tuples representing the indices of the available positions
        """
        available_positions = []
        for x in range(len(self.board.array)):
            for y in range(len(self.board.array[x])):
                if self.board.array[x][y] != 'X' and self.board.array[x][y] != 'O':
                    available_positions.append((x, y))
        return available_positions

    def game_over(self) -> bool:
        """
        Check if the current game has a winner or if there are no more moves.
        :return: (bool): True if the game is over
        """
        if self.board.get_winning_positions() or len(self.get_available_positions()) == 0:
            return True
        else:
            return False

    def minimax(self, moves: int, maximising_player: bool) -> int:
        """
        The minimax tree traversal algorithm used to find the optimal move for the AI player.  It uses recursion
        to iterate through each node of the tree representing the possible moves to find the optimal move.
        :param moves: (int): Counter that increments for each level of the tree,
        used for calculating the optimal evaluation value
        :param maximising_player: (bool): Boolean to state if the player is the maximising player, aiming for the
        best evaluation result
        :return: (int): The evaluation score of the position
        """
        if self.game_over():
            return self.evaluate_board()

        if maximising_player:
            max_val = float('-inf')
            for position in self.get_available_positions():
                original_value = self.board.array[position[0]][position[1]]
                self.board.array[position[0]][position[1]] = 'O'
                evaluation = self.minimax(moves + 1, False)
                self.board.array[position[0]][position[1]] = original_value
                max_val = max(max_val, evaluation - moves)
            return max_val
        else:
            min_val = float('inf')
            for position in self.get_available_positions():
                original_value = self.board.array[position[0]][position[1]]
                self.board.array[position[0]][position[1]] = 'X'
                evaluation = self.minimax(moves + 1, True)
                self.board.array[position[0]][position[1]] = original_value
                min_val = min(min_val, evaluation + moves)
            return min_val

    def get_best_move(self, board: Board) -> object:
        """
        Find the optimal move for the AI player from the current gameboard object
        :param board: (Board): the current gameboard object
        :return: (object): the string object position used for making the AI players move
        """
        self.update_board(board)
        best_eval = float('-inf')
        best_position = None

        if len(self.get_available_positions()) == 9:
            return '1'
        else:
            for position in self.get_available_positions():
                original_value = self.board.array[position[0]][position[1]]
                self.board.array[position[0]][position[1]] = 'O'
                position_eval = self.minimax(0, False)
                self.board.array[position[0]][position[1]] = original_value

                if position_eval > best_eval:
                    best_eval = position_eval
                    best_position = original_value
            return best_position
