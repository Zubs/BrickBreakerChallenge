import unittest
import pygame
from src.ball import Ball
from src.paddle import Paddle

class TestBall(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.paddle = Paddle(self.screen)
        self.ball = Ball(self.paddle, self.screen)

    def test_show(self):
        self.ball.show()
        self.assertEqual(self.ball.position.x, self.screen.get_width() / 2)
        self.assertEqual(self.ball.position.y, self.screen.get_height() * 0.8)

    def test_move(self):
        initial_x = self.ball.position.x
        initial_y = self.ball.position.y
        self.ball.move()
        self.assertEqual(self.ball.position.x, initial_x + self.ball.velocity.x_vel)
        self.assertEqual(self.ball.position.y, initial_y + self.ball.velocity.y_vel)

    def test_collision_change(self):
        initial_y_vel = self.ball.velocity.y_vel
        self.ball.collision_change()
        self.assertEqual(self.ball.velocity.y_vel, -initial_y_vel)

    def test_boundries(self):
        initial_x_vel = self.ball.velocity.x_vel
        self.ball.position.x = -self.ball.ball_radius
        self.ball.position.y = 0
        self.ball.boundries()
        self.assertEqual(self.ball.velocity.x_vel, -initial_x_vel)
        self.assertEqual(self.ball.velocity.y_vel, self.ball.velocity.y_vel)

    def test_limit_vel(self):
        self.ball.velocity.x_vel = self.ball.velocity.max_x_vel + 10
        self.ball.limit_vel()
        self.assertEqual(self.ball.velocity.x_vel, self.ball.velocity.max_x_vel)

    def test_update(self):
        initial_x = self.ball.position.x
        initial_y = self.ball.position.y
        self.ball.update()
        self.assertEqual(self.ball.position.x, initial_x + self.ball.velocity.x_vel)
        self.assertEqual(self.ball.po