"""
This module defines the Ball class for a game. It includes methods for moving the ball,
detecting collisions, and drawing the ball on the screen.
"""
import pygame

from src.paddle import Paddle
from src.position import Position
from src.velocity import Velocity

class Ball():
    """
    This class represents a ball in a game. It includes methods for moving the ball,
    detecting collisions, and drawing the ball on the screen.
    """
    color = (50, 40, 255)

    def __init__(
        self,
        paddle: Paddle,
        screen: pygame.Surface,
        player_level: int = 1
    ):
        """
        This method initializes the Ball object with a specified paddle, screen, and player level.
        """
        self.player_level = player_level
        self.position = Position(int(screen.get_width() / 2), int(screen.get_height() * 0.8))
        self.velocity = Velocity(8, -8)
        self.ball_radius = 21.2 - (1.2 * self.player_level)
        self.paddle = paddle
        self.screen = screen

    def show(self):
        """
        This method draws a circle on the screen representing the ball.
        """
        position = (self.position.x, self.position.y)
        pygame.draw.circle(
            self.screen,
            self.color,
            position,
            self.ball_radius
        )

    def move(self):
        """
        This method updates the ball's position based on its velocity.
        Basically moving it.
        """
        self.position.x += self.velocity.x_vel
        self.position.y += self.velocity.y_vel

    def collision_change(self):
        """
        This method changes the ball's direction based on its collision with the paddle.
        It also adjusts the x velocity based on where the ball hits the paddle.
        """
        center = self.paddle.paddle_x + self.paddle.length / 2
        left_end = self.paddle.paddle_x
        right_end = self.paddle.paddle_x + self.paddle.length
        self.velocity.y_vel = -self.velocity.y_vel

        if left_end < self.position.x < center:
            ratio = (center - self.position.x) / (self.paddle.length / 2)
            self.velocity.x_vel += -self.velocity.max_x_vel * ratio
        elif center < self.position.x < right_end:
            ratio = (self.position.x - center) / (self.paddle.length / 2)
            self.velocity.x_vel += self.velocity.max_x_vel * ratio

    def boundries(self):
        """
        This method checks if the ball has hit the boundaries of the screen.
        If it has, it reverses the direction of the ball.
        """
        if self.position.y <= (0 + self.ball_radius):
            self.velocity.y_vel = -self.velocity.y_vel
        if self.position.x <= (0 + self.ball_radius):
            self.velocity.x_vel = -self.velocity.x_vel
        if self.position.x >= (self.screen.get_width() - self.ball_radius):
            self.velocity.x_vel = -self.velocity.x_vel

    def limit_vel(self):
        """
        This method limits the ball's x velocity to its maximum value.
        If the ball's x velocity exceeds the maximum, it sets the x velocity to the maximum.
        """
        if -self.velocity.max_x_vel > self.velocity.x_vel:
            self.velocity.x_vel = -self.velocity.max_x_vel
        elif self.velocity.x_vel > self.velocity.max_x_vel:
            self.velocity.x_vel = self.velocity.max_x_vel

    def update(self):
        """
        This method updates the ball's position, 
        checks for boundary collisions, 
        and limits the velocity.
        """
        self.move()
        self.boundries()
        self.limit_vel()
