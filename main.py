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

pygame.init()

SCR_WIDTH = 800
SCR_HEIGHT = 600

screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
pygame.display.set_caption("Brick Breaker")

def brick_collision(level: Level, ball: Ball):
    """
    Detects collision between the ball and the bricks in the level.
    If a collision is detected, it inverts the ball's y direction
    and adjusts its x velocity based on where it hit the brick.
    It also removes the hit brick from the level.
    """
    for _, brick in enumerate(level.brick.bricks):
        x, y = brick
        # if (x < ball.position.x < (x + level.brick.length) and
        #         y > ball.position.y > (y + level.brick.width)):
        if (x < ball.position.x < (x + level.brick.length) and 
            y < ball.position.y < (y + level.brick.width)):
            # Invert the y direction
            ball.velocity.y_vel = -ball.velocity.y_vel
            center = x + level.brick.length/2
            if x < ball.position.x < center:
                ratio = (center - ball.position.x) / (level.brick.length / 2)
                ball.velocity.x_vel += -ball.velocity.max_x_vel * ratio
            elif center < ball.position.x < (x + level.brick.length):
                ratio = (ball.position.x - center) / (level.brick.length / 2)
                ball.velocity.x_vel += ball.velocity.max_x_vel * ratio

            level.remove(brick)

def show_gameover():
    """
    Displays the 'GAME OVER' message on the screen.
    """
    text = pygame.font.Font("freesansbold.ttf", int(SCR_HEIGHT * 0.1))
    gameover = text.render(
        "GAME OVER",
        True,
        (255, 23, 20)
    )
    screen.blit(gameover, (int(SCR_WIDTH * 0.25), int(SCR_HEIGHT * 0.4)))

clock = pygame.time.Clock()
background_color = (200, 200, 200)
while True:
    # initial positions
    paddle = Paddle(screen)
    ball = Ball(paddle, screen)
    level = Level(screen, background_color)
    # pylint: disable=invalid-name
    over = False
    clicked_replay = False

    # paddle movement switches
    key_left = False
    key_right = False

    while True:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    key_left = True
                if event.key == pygame.K_RIGHT:
                    key_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    paddle.stop()
                    key_left = False
                if event.key == pygame.K_RIGHT:
                    paddle.stop()
                    key_right = False

        # GAME LOGIC

        # paddle movement switches
        if key_left is True:
            paddle.move_left()
        if key_right is True:
            paddle.move_right()

        # ball machanics
        ball.update()

        ball_bottom = ball.position.y + ball.ball_radius
        ball_within_paddle = paddle.paddle_x < ball.position.x < (
            paddle.paddle_x + paddle.length)

        if paddle.paddle_y + 10 > ball_bottom > paddle.paddle_y and ball_within_paddle:
            ball.collision_change()
        # brick collision
        brick_collision(level, ball)

        # paddle boundries
        paddle.boundries()
        if ball.position.y > SCR_HEIGHT:
            show_gameover()
            over = True
            # REPLAY BUTTON
            button_dimensions = Rectangle((260, 350), (150, 60))
            button_text = Text("REPLAY", 30, (200, 250, 255))
            replay_button = Button(
                screen,
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
                            clicked_replay = True
                        state = 'changed'
                    elif replay_button.is_over_mouse() is False:
                        state = 'original'
                    if event.type == pygame.QUIT:
                        pygame.quit()
                if state == 'changed':
                    replay_button.change_color((80, 240, 80), (14, 37, 100))
                if clicked_replay is True:
                    break
                pygame.display.update()

        screen.fill(background_color)
        paddle.show()
        level.show()

        ball.show()
        if over is True:
            break

        pygame.display.update()
