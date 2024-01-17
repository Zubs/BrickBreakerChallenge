"""
This module contains a Button class for use in a pygame application.
"""
import pygame
from src.rectangle import Rectangle
from src.text import Text

pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill((255, 255, 255))

class Button():
    """
    This class represents a Button in a pygame application.
    """
    def __init__(
        self,
        screen,
        color_button,
        rectangle = Rectangle(),
        text = Text()
    ):
        self.screen = screen
        self.color_button = color_button
        self.rectangle = rectangle
        self.text = text

    def show(self):
        """
        This method draws a rectangle on the screen representing the button.
        It also renders the text on the button.
        """
        pygame.draw.rect(
            self.screen,
            self.color_button,
            (
                (self.rectangle.x, self.rectangle.y),
                (self.rectangle.width, self.rectangle.length)
            )
        )
        font = pygame.font.Font('freesansbold.ttf', self.text.text_size)
        caption = font.render(
            self.text.text,
            True,
            self.text.color
        )
        self.screen.blit(caption, (int(self.rectangle.x + self.rectangle.width * 0.05),
                                   int(self.rectangle.y + self.rectangle.length * 0.2)))

    def is_over_mouse(self):
        """
        Check if the mouse is over the button.
        """
        x, y = pygame.mouse.get_pos()
        if (self.rectangle.x < x < self.rectangle.x + self.rectangle.width and
            self.rectangle.y < y < self.rectangle.y + self.rectangle.length):
            return True
        return False

    def change_color(
        self,
        change_color_button,
        change_color_text
    ):
        """
        This method changes the color of the button and the text on the button.

        Parameters:
        change_color_button (tuple): The RGB color to change the button to.
        change_color_text (tuple): The RGB color to change the text to.
        """
        pygame.draw.rect(
            self.screen,
            change_color_button,
            (
                (self.rectangle.x, self.rectangle.y),
                (self.rectangle.width, self.rectangle.length)
            )
        )
        font = pygame.font.Font('freesansbold.ttf', self.text.text_size)
        caption = font.render(
            self.text.text,
            True,
            change_color_text
        )
        self.screen.blit(
            caption,
            (int(self.rectangle.x + self.rectangle.width * 0.05),
            int(self.rectangle.y + self.rectangle.length * 0.2))
        )
