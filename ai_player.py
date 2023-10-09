from board import Board


class AiPlayer:
    def __init__(self):
        self.board = Board()

    def update_board(self, board: Board) -> None:
        self.board.array = board.get_board()

    def evaluate_board(self) -> int:
        if winning_positions := self.board.get_winning_positions():
            if self.board.array[winning_positions[0][0]][winning_positions[0][1]] == 'O':
                return 10
            elif self.board.array[winning_positions[0][0]][winning_positions[0][1]] == 'X':
                return -10
        else:
            return 0

    def get_available_positions(self) -> list:
        available_positions = []
        for x in range(len(self.board.array)):
            for y in range(len(self.board.array[x])):
                if self.board.array[x][y] != 'X' and self.board.array[x][y] != 'O':
                    available_positions.append((x, y))
        return available_positions

    def game_over(self) -> bool:
        if self.board.get_winning_positions():
            return True
        else:
            return False

    def minimax(self, moves: int, maximising_player: bool) -> int:
        if self.game_over():
            return self.evaluate_board()

        if maximising_player:
            max_val = float('-inf')
            for position in self.get_available_positions():
                original_value = self.board.array[position[0]][position[1]]
                self.board.array[position[0]][position[1]] = 'O'
                evaluation = self.minimax(moves + 1, False)
                self.board.array[position[0]][position[1]] = original_value
                max_val = max(max_val, evaluation)
            return max_val
        else:
            min_val = float('inf')
            for position in self.get_available_positions():
                original_value = self.board.array[position[0]][position[1]]
                self.board.array[position[0]][position[1]] = 'X'
                evaluation = self.minimax(moves + 1, True)
                self.board.array[position[0]][position[1]] = original_value
                min_val = min(min_val, evaluation)
            return min_val

    def get_best_move(self, board: Board) -> object:
        self.update_board(board)
        best_eval = float('-inf')
        best_position = None

        for position in self.get_available_positions():
            original_value = self.board.array[position[0]][position[1]]
            self.board.array[position[0]][position[1]] = 'O'
            position_eval = self.minimax(0, False)
            self.board.array[position[0]][position[1]] = original_value

            if position_eval > best_eval:
                best_eval = position_eval
                best_position = original_value
        print(best_position)
        return best_position
