# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

class BaseBoard:
    """Base class for the game board,
    containing common properties and methods."""

    def __init__(self, grid_size, num_ships):
        """Initializes the grid size, number of ships,
        grid, and places the ships on the grid."""
        self.grid_size = grid_size 
        self.num_ships = num_ships  
        self.grid = self.create_grid()  
        self.place_ships() 
