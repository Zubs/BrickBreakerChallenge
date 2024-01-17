# Brick Breaker Game

This is a simple implementation of the classic Brick Breaker game using Pygame.

## Prerequisites

- Python 3.x: The game is written in Python 3. Make sure you have it installed on your system.

- Pygame: Pygame is a set of Python modules designed for writing video games. You can install it using pip: `pip install pygame`.

## How to Run the Game

1. Clone the repository: `git clone <repository_url>`.
2. Navigate to the repository: `cd <repository_name>`.
3. Run the main.py file: `python main.py`.

## Files

- `main.py`: This is the main file where the game loop is implemented. It initializes the game objects like the paddle, ball, and bricks. It also handles the game mechanics like paddle movement, ball movement, and collision detection.

- `paddle.py`: This file contains the Paddle class. The paddle's position, movement, and display on the screen are handled in this class.

## Game Objects

- `Paddle`: The paddle is controlled by the player to bounce the ball and prevent it from falling off the screen. The paddle can move left or right.

- `Ball`: The ball moves around the screen, bouncing off the walls and the paddle. The ball's movement and collision mechanics are handled in this class.

- `Bricks`: The bricks are the targets in the game. The player's goal is to break all the bricks by hitting them with the ball.

## Game Mechanics

- `Paddle Movement`: The paddle can move left or right. The movement is controlled by the player.

- `Ball Movement`: The ball moves in a straight line until it hits a wall, the paddle, or a brick. When the ball hits a wall or the paddle, it bounces back. When the ball hits a brick, the brick is destroyed, and the ball bounces back.

- `Collision Detection`: The game checks for collisions between the ball and the other game objects. If the ball hits the paddle or a brick, it bounces back. If the ball hits the bottom of the screen, the game is over.

- `Game Over`: The game ends when the ball hits the bottom of the screen. A game over message is displayed, and the player is given the option to replay the game.

- `Level`: The level is a collection of bricks. The game has 10 levels, and each level has a different arrangement of bricks.

- `Pause/Resume`: The game can be paused by pressing the space bar. Pressing the space bar again will resume the game.

## To Do
- [ ] Increase ball speed by level
