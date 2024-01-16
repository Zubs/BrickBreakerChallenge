"""
This module defines a Rectangle class.
"""

class Rectangle:
    """Represents a rectangle with coordinates and dimensions."""
    def __init__(self, coordinates=(0, 0), dimensions=(100, 100)):
        self.x, self.y = coordinates
        self.width, self.length = dimensions
