class Player:
    def __init__(self, name: str, player_num: int, is_cpu: bool):
        self.name = name
        self.player_num = player_num
        self.is_cpu = is_cpu
        self.score = 0

    def increase_score(self):
        self.score += 1
