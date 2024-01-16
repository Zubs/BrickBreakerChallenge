"""
This module contains the Level class for a game. 
It uses the pygame library and handles the creation, 
display, and removal of bricks in the game.
"""
import random
import pygame
from brick import Brick

class Level():
    """
    This class represents a level in the game. 
    It handles the creation, display, and removal of bricks.
    """
    brick_colors = [
        (200, 50, 80),
        (45, 80, 240),
        (46, 235, 70),
        (150, 50, 180),
        (230, 170, 80),
        (60, 230, 220),
        (180, 210, 80)
    ]

    def __init__(
        self,
        screen: pygame.Surface,
        background_color: tuple
    ):
        self.screen = screen
        self.brick = Brick(int(screen.get_width() * 0.8) // 9)
        self.background_color = background_color

        for i in range(
            10,
            self.brick.rows * self.brick.width,
            self.brick.width
        ):
            for j in range(
                int(screen.get_width() * 0.1),
                int(screen.get_width() * 0.9 - self.brick.length) + 1,
                self.brick.length
            ):
                self.brick.bricks.append([j, i])
                self.brick.random_color.append(random.choice(self.brick_colors))

    def show(self):
        """
        This method draws each brick in the game on the screen. 
        It cycles through the colors in brick_colors for each row of bricks.
        """
        num = 1
        color_index = 1
        for item in self.brick.bricks:
            brick_size = (self.brick.length - self.brick.spacing,
                          self.brick.width - self.brick.spacing)
            pygame.draw.rect(
                self.screen,
                self.brick_colors[color_index-1],
                ((item[0], item[1]), brick_size)
            )
            num += 1
            if num > color_index * self.brick.rows_bricks:
                color_index += 1

    def update(self, cordinate):
        """
        This method updates the screen by drawing a rectangle at the given coordinate.
        The rectangle's color is the same as the background, 
        effectively erasing any brick that was there.
        """
        brick_size = (self.brick.length - self.brick.spacing, self.brick.width - self.brick.spacing)
        pygame.draw.rect(
            self.screen,
            self.background_color,
            (cordinate, brick_size)
        )

    def remove(self, brick):
        """
        This method removes a specified brick from the bricks list.
        """
        self.brick.bricks.remove(brick)
