from pdtypes import Choice, Score


class Player:
    """
    A representation of a player.
    They have choice and recognise the result of their choice

    Returns:
        None: None
    """

    def __init__(self, name: str):
        """Create a player by name"""

        """Choice"""
        self.choice = Choice.COOPORATE

        """Score"""
        self.score = Score.SUCKER

        """Name"""
        self.name = name

    def choose(self, choice=Choice.COOPORATE):
        """
        Make a choice to COOPORATE and DEFECT

        Args:
            choice (optional): Accepts Choice.COOPORATE or Choice.DEFECT. Defaults to Choice.COOPORATE.
        """
        self.choice = choice

    def __str__(self) -> str:
        return f"{self.name} chose {self.choice[1]} resulting in {self.score[1]}"


# ===================================================

# newp = Player("PlayerA")
# newp.choose(Choice.DEFECT)
# print(Choice.COOPORATE)
# print(newp.choice)
# print(newp)
