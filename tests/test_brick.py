import unittest
import pygame
from src.brick import Brick

class TestBrick(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.brick = Brick(length=50)

    def test_initial_attributes(self):
        self.assertEqual(self.brick.player_level, 5)
        self.assertEqual(self.brick.rows, 5)
        self.assertEqual(self.brick.rows_bricks, 10)
        self.assertEqual(self.brick.length, 50)
        self.assertEqual(self.brick.width, 40)
        self.assertEqual(self.brick.spacing, 4)
        self.assertEqual(self.brick.bricks, [])
        self.assertEqual(self.brick.random_color, [])

if __name__ == '__main__':
    unittest.main()
