"""
This module defines a Paddle class for a Pygame application.
The Paddle can be moved left or right and has boundary checks.
"""

import pygame

class Paddle():
    """
    This class represents a Paddle in a Pygame application.
    The Paddle can be moved left or right and has boundary checks.
    """
    paddle_color = (80, 50, 30)
    paddle_thickness = 20

    def __init__(self, screen: pygame.Surface, player_level: int = 1):
        """
        This method initializes the Paddle object with a specified screen.
        """
        self.player_level = player_level
        self.paddle_x = int(screen.get_width() * 0.45)
        self.paddle_y = int(screen.get_height() * 0.95)
        self.length = 410 - (self.player_level * 30)
        self.screen = screen
        self.velocity = 0

    def show(self):
        """
        This method draws the paddle on the screen with a specified thickness.
        """
        pygame.draw.rect(self.screen, self.paddle_color, ((
            self.paddle_x, self.paddle_y), (self.length, self.paddle_thickness)))

    def move_left(self):
        """
        This method moves the paddle to the left by decreasing the x-coordinate.
        The velocity of the paddle is set to 15.
        """
        self.velocity = 15
        self.paddle_x += -self.velocity

    def move_right(self):
        """
        This method moves the paddle to the right by increasing the x-coordinate.
        The velocity of the paddle is set to 15.
        """
        self.velocity = 15
        self.paddle_x += self.velocity

    def stop(self):
        """
        This method stops the paddle by setting the velocity to 0.
        """
        self.velocity = 0

    def boundries(self):
        """
        This method checks and adjusts the paddle's position if it hits the screen boundaries.
        """
        if self.paddle_x >= (self.screen.get_width() - self.length):
            self.paddle_x = self.screen.get_width() - self.length
        elif self.paddle_x <= 0:
            self.paddle_x = 0
