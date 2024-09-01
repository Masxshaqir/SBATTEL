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
def create_grid(self):
        """Creates and returns an empty grid of the specified size."""
        return [[' ' for _ in range(self.grid_size)]  
                for _ in range(self.grid_size)]
def place_ships(self):
        """Randomly places the specified number of ships on the grid."""
        for _ in range(self.num_ships):  
            row = random.randint(0, self.grid_size - 1)  
            col = random.randint(0, self.grid_size - 1)  
            while self.grid[row][col] == 'S':  
                row = random.randint(0, self.grid_size - 1)  
                col = random.randint(0, self.grid_size - 1)  
            self.grid[row][col] = 'S'  

    def print_board(self):
        """Prints the current state of the grid."""
        print("   " + " ".join([str(i) for i in range(len(self.grid))]))  
        print("  " + "--" * len(self.grid))  
        row_number = 0
        for row in self.grid:  
            print("%d |%s|" % (row_number, "|".join(row)))  
            row_number += 1
        print("\n")  
