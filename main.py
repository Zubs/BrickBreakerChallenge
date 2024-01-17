"""
This module contains the main game loop for a Brick Breaker game. 
It uses the pygame library to create the game window, handle events, 
and draw the game objects (ball, paddle, bricks). 
It also includes functions for handling collisions and displaying the game over screen.
"""

import pygame
from ball import Ball
from level import Level
from button import Button
from paddle import Paddle
from text import Text
from rectangle import Rectangle
from highscore import HighScore

class BrickBreaker:
    """
    This class contains the main game loop for a Brick Breaker game.
    """
    def __init__(self):
        pygame.init()
        self.screen_width = 1000
        self.screen_height = 750
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Brick Breaker")
        self.clock = pygame.time.Clock()
        self.background_color = (200, 200, 200)
        self.score = 0
        self.lives = 3
        self.player_level = 1 # Max level is 10
        self.over = False
        self.clicked_replay = False
        self.paused = False
        self.key_left = False
        self.key_right = False
        self.paddle = Paddle(self.screen, self.player_level)
        self.ball = Ball(self.paddle, self.screen, self.player_level)
        self.level = Level(self.screen, self.background_color, self.player_level)
        self.highscore = HighScore()

    def brick_collision(self, level: Level, ball: Ball):
        """
        Detects collision between the ball and the bricks in the level.
        If a collision is detected, it inverts the self.ball's y direction
        and adjusts its x velocity based on where it hit the brick.
        It also removes the hit brick from the self.level.
        """
        for _, brick in enumerate(self.level.brick.bricks):
            x, y, color = brick
            if (x < self.ball.position.x < (x + self.level.brick.length) and
                y < self.ball.position.y < (y + self.level.brick.width)):
                #increase score
                self.score += self.player_level
                # Invert the y direction
                self.ball.velocity.y_vel = -self.ball.velocity.y_vel
                center = x + self.level.brick.length / 2
                if x < self.ball.position.x < center:
                    ratio = (center - self.ball.position.x) / (self.level.brick.length / 2)
                    self.ball.velocity.x_vel += -self.ball.velocity.max_x_vel * ratio
                elif center < self.ball.position.x < (x + self.level.brick.length):
                    ratio = (self.ball.position.x - center) / (self.level.brick.length / 2)
                    self.ball.velocity.x_vel += self.ball.velocity.max_x_vel * ratio

                self.level.remove(brick)
                if not self.level.brick.bricks:  # Check if the list of bricks is empty
                    self.show_level_won()
                    pygame.display.update()
                    pygame.time.wait(3000)  # Wait for 3 seconds before continuing
                    return True  # Return a flag indicating the self.level is won

        return False
    
    def show_high_scores(self):
        font_size = int(self.screen_height * 0.025)
        text = pygame.font.Font("freesansbold.ttf", font_size)
        high_scores = self.highscore.get_high_scores()
        for i, score in enumerate(high_scores):
            score_text = text.render(
                f"{i+1}. {score}",
                True,
                (0, 0, 0)
            )
            self.screen.blit(score_text, (10, 10 + font_size * (i+3)))

    def show_gameover(self):
        """
        Displays the 'GAME OVER' message and the final score on the screen.
        """
        font_size = int(self.screen_height * 0.1)
        text = pygame.font.Font("freesansbold.ttf", font_size)
        gameover = text.render(
            "GAME OVER",
            True,
            (255, 23, 20)
        )
        text_width, text_height = text.size("GAME OVER")
        self.screen.blit(
            gameover,
            ((self.screen_width - text_width) / 2, (self.screen_height - text_height) / 2)
        )

        font_size = int(self.screen_height * 0.08)
        text = pygame.font.Font("freesansbold.ttf", font_size)
        score_text = text.render(
            f"Final Score: {self.score}",
            True,
            (255, 23, 20)
        )
        score_text_width, score_text_height = text.size(f"Final Score: {self.score}")
        self.screen.blit(
            score_text,
            (
                (self.screen_width - score_text_width) / 2,
                (self.screen_height - score_text_height) / 2 + text_height
            )
        )
        if self.highscore.add_score(self.score):
            new_high_score_text = text.render(
                "New High Score!!!",
                True,
                (50, 205, 50)
            )
            new_high_score_text_width, new_high_score_text_height = text.size("New High Score!!!")
            self.screen.blit(
                new_high_score_text,
                (
                    (self.screen_width - new_high_score_text_width) / 2,
                    (self.screen_height - new_high_score_text_height) / 2 + text_height + score_text_height
                )
            )
            # self.show_new_high_scores()

    def show_game_paused(self):
        """
        Displays the 'GAME PAUSED' message on the screen.
        """
        font_size = int(self.screen_height * 0.1)
        text = pygame.font.Font("freesansbold.ttf", font_size)
        paused = text.render(
            "PAUSED",
            True,
            (255, 23, 20)
        )
        text_width, text_height = text.size("PAUSED")
        self.screen.blit(
            paused,
            ((self.screen_width - text_width) / 2, (self.screen_height - text_height) / 2)
        )

    def show_score(self):
        """
        Displays the current score, lives, and player self.level on the screen.
        """
        font_size = int(self.screen_height * 0.025)
        text = pygame.font.Font("freesansbold.ttf", font_size)

        score_text = text.render(
            f"Score: {self.score}",
            True,
            (0, 0, 0)
        )
        self.screen.blit(score_text, (10, 10))

        lives_text = text.render(
            f"Lives: {self.lives}",
            True,
            (0, 0, 0)
        )
        self.screen.blit(lives_text, (10, 10 + font_size))

        player_level_text = text.render(
            f"Level: {self.player_level}",
            True,
            (0, 0, 0)
        )
        self.screen.blit(player_level_text, (10, 10 + font_size * 2))

    def reset_game(self, player_level: int = 1):
        """
        Resets the game to its initial state.
        """
        self.lives = 3
        self.player_level = player_level
        self.over = False
        self.clicked_replay = False
        self.paused = False
        self.key_left = False
        self.key_right = False

        self.paddle = Paddle(self.screen, self.player_level)
        self.ball = Ball(self.paddle, self.screen, self.player_level)
        self.level = Level(self.screen, self.background_color, self.player_level)

    def show_level_won(self):
        """
        Displays the 'LEVEL WON' message on the screen.
        """
        font_size = int(self.screen_height * 0.1)
        text = pygame.font.Font("freesansbold.ttf", font_size)
        level_won_text = text.render(
            f"Level {self.player_level} WON",
            True,
            (50, 205, 50)
        )
        text_width, text_height = text.size(f"Level {self.player_level} WON")
        self.screen.blit(
            level_won_text,
            ((self.screen_width - text_width) / 2, (self.screen_height - text_height) / 2)
        )
        self.reset_game(self.player_level + 1)

    def game_loop(self):
        """
        Main game loop.
        """
        while True:
            while True:
                self.clock.tick(30)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.paused = not self.paused
                        if event.key == pygame.K_LEFT:
                            self.key_left = True
                        if event.key == pygame.K_RIGHT:
                            self.key_right = True
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT:
                            self.paddle.stop()
                            self.key_left = False
                        if event.key == pygame.K_RIGHT:
                            self.paddle.stop()
                            self.key_right = False

                if not self.paused:
                    # GAME LOGIC
                    # self.paddle movement switches
                    if self.key_left is True:
                        self.paddle.move_left()
                    if self.key_right is True:
                        self.paddle.move_right()

                    # self.ball machanics
                    self.ball.update()

                    ball_bottom = self.ball.position.y + self.ball.ball_radius
                    ball_within_paddle = self.paddle.paddle_x < self.ball.position.x < (
                        self.paddle.paddle_x + self.paddle.length)

                    if (
                        self.paddle.paddle_y + 10 > ball_bottom > self.paddle.paddle_y and
                        ball_within_paddle
                    ):
                        self.ball.collision_change()
                    # brick collision
                    if self.brick_collision(self.level, self.ball):
                        break

                    # self.paddle boundries
                    self.paddle.boundries()
                    if self.ball.position.y > self.screen_height:
                        self.show_gameover()
                        self.over = True
                        # REPLAY BUTTON
                        button_dimensions = Rectangle((450, 550), (130, 45))
                        button_text = Text("REPLAY", 30, (200, 250, 255))
                        replay_button = Button(
                            self.screen,
                            (80, 45, 200),
                            button_dimensions,
                            button_text
                        )
                        state = 'original'

                        while True:
                            replay_button.show()

                            for event in pygame.event.get():
                                if replay_button.is_over_mouse() is True:
                                    if event.type == pygame.MOUSEBUTTONUP:
                                        self.clicked_replay = True
                                    state = 'changed'
                                elif replay_button.is_over_mouse() is False:
                                    state = 'original'
                                if event.type == pygame.QUIT:
                                    pygame.quit()

                            if state == 'changed':
                                replay_button.change_color((80, 240, 80), (14, 37, 100))

                            if self.clicked_replay is True:
                                self.reset_game()
                                break

                            pygame.display.update()

                    self.screen.fill(self.background_color)
                    self.show_score()
                    self.paddle.show()
                    self.level.show()

                    self.ball.show()
                    if self.over is True:
                        break

                    pygame.display.update()
                else:
                    while self.paused:
                        self.show_game_paused()

                        state = 'original'
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_SPACE:
                                        self.paused = not self.paused
                                        break
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                            if not self.paused:
                                break

                            pygame.display.update()

if __name__ == "__main__":
    game = BrickBreaker()
    game.game_loop()
