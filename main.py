"""
This is the main module for the BrickBreaker game. 
It creates an instance of the game and starts the game loop.
"""
from src.main import BrickBreaker

if __name__ == "__main__":
    game = BrickBreaker()
    game.game_loop()
