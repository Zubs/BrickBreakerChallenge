"""
This module defines the Text class, which represents a piece of text with a size and color.
"""

class Text:
    """
    This class represents a piece of text with a size and color.
    """
    def __init__(self, text='Click Here', text_size=10, color=(0, 0, 0)):
        self.text = text
        self.text_size = text_size
        self.color = color
