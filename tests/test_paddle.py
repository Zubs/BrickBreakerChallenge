# import unittest
# from src.paddle import Paddle

# class TestPaddle(unittest.TestCase):
#     def setUp(self):
#         self.paddle = Paddle()

#     def test_move_left(self):
#         initial_x = self.paddle.paddle_x
#         self.paddle.move_left()
#         self.assertEqual(self.paddle.paddle_x, initial_x - self.paddle.velocity)

#     def test_move_right(self):
#         initial_x = self.paddle.paddle_x
#         self.paddle.move_right()
#         self.assertEqual(self.paddle.paddle_x, initial_x + self.paddle.velocity)

# if __name__ == '__m