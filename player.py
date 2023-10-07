class Player:
    def __init__(self, name, cpu):
        self.name = name
        self.score = 0
        self.cpu = None

    def increase_score(self):
        self.score += 1
