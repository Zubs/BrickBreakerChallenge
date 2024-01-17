import unittest
import pygame
from unittest.mock import patch
from src.button import Button
from src.rectangle import Rectangle
from src.text import Text

class TestButton(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.rectangle = Rectangle((50, 50), (200, 100))
        self.text = Text('Test Button', 32, (255, 255, 255))
        self.button = Button(self.screen, (0, 0, 255), self.rectangle, self.text)

    def test_show(self):
        self.button.show()
        self.assertEqual(self.button.rectangle.x, 50)
        self.assertEqual(self.button.rectangle.y, 50)
        self.assertEqual(self.button.rectangle.width, 200)
        self.assertEqual(self.button.rectangle.length, 100)
        self.assertEqual(self.button.text.text, 'Test Button')
        self.assertEqual(self.button.text.text_size, 32)
        self.assertEqual(self.button.text.color, (255, 255, 255))

    @patch('pygame.mouse.get_pos')
    def test_is_over_mouse(self, mock_get_pos):
        mock_get_pos.return_value = (75, 75)
        self.assertTrue(self.button.is_over_mouse())
        mock_get_pos.return_value = (300, 300)
        self.assertFalse(self.button.is_over_mouse())

    def test_change_color(self):
        self.button.change_color((255, 0, 0), (0, 255, 0))
        self.assertEqual(self.button.color_button, (0, 0, 255))
        self.assertEqual(self.button.text.color, (255, 255, 255))

if __name__ == '__main__':
    unittest.mai