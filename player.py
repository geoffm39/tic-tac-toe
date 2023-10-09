class Player:
    """
    Player class represents the player objects in the game.
    """
    def __init__(self, name: str, player_num: int, is_computer: bool):
        """
        Constructor for the Player class, assigning the attributes for the player.
        :param name: (str): Name of the player
        :param player_num: (int): player number. 1 or 2
        :param is_computer: (bool): Boolean to state if the player is a computer
        """
        self.name = name
        self.player_num = player_num
        self.is_computer = is_computer
        self.score = 0

    def increase_score(self) -> None:
        """
        Increase the score of the player by 1.
        :return: None
        """
        self.score += 1
