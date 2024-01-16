"""
This module defines the Velocity class.
This represents a 2D velocity vector with a maximum x velocity.
"""
class Velocity:
    """
    This class represents a 2D velocity vector with a maximum x velocity.
    """
    def __init__(self, x_vel, y_vel, max_x_vel = 10):
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.max_x_vel = max_x_vel
