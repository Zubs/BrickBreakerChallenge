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
        rows = 10,
        rows_bricks = 10,
        width = 40,
        spacing = 4
    ):
        self.rows = rows
        self.rows_bricks = rows_bricks
        self.length = length
        self.width = width
        self.spacing = spacing
        self.bricks = []
        self.random_color = []
