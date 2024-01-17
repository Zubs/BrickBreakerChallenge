"""
This module defines the Brick class used for creating brick objects in a game.
"""

# Adding this so the class can have all 7 attributes
# pylint: disable=too-many-instance-attributes
class Brick:
    """
    This class represents a Brick object with certain attributes like rows, length, etc.
    """
    def __init__(
        self,
        length,
        player_level = 5,
        rows_bricks = 10,
        width = 40,
    ):
        self.player_level = player_level
        self.rows = player_level if player_level > 5 else 5
        self.rows_bricks = rows_bricks
        self.length = length
        self.width = width
        self.spacing = 4
        self.bricks = []
        self.random_color = []
