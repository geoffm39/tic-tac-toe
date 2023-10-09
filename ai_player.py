from board import Board


class AiPlayer:
    def __init__(self, player_num):
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
                if self.board.array[x][y] != 'X' or self.board.array[x][y] != 'O':
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
                original_value = self.board.array[position[0]][position[1]].copy()
                self.board.array[position[0]][position[1]] = 'O'
                evaluation = self.minimax(moves + 1, False)
                self.board.array[position[0]][position[1]] = original_value
                max_val = max(max_val, evaluation)
            return max_val
        else:
            min_val = float('inf')
            for position in self.get_available_positions():
                original_value = self.board.array[position[0]][position[1]].copy()
                self.board.array[position[0]][position[1]] = 'X'
                evaluation = self.minimax(moves + 1, True)
                self.board.array[position[0]][position[1]] = original_value
                min_val = min(min_val, evaluation)
            return min_val
