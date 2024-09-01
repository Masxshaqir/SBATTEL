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

        
class PlayerBoard(BaseBoard):
    """Class for the player's board, derived from the BaseBoard class."""

    def __init__(self, grid_size, num_ships, player_name):
        """Initializes the player's name and calls the parent constructor."""
        super().__init__(grid_size, num_ships)  
        self.player_name = player_name  

    def display(self):
        """Displays the player's board."""
        print("{}'s Board:".format(self.player_name))  
        self.print_board()  

class ComputerBoard(BaseBoard):
    """Class for the computer's board, derived from the BaseBoard class."""

    def display(self):
        """Displays the computer's board with ships hidden."""
        print("Computer's Board:")  
        hidden_grid = [[' ' if cell == 'S' else cell for cell in row]  
                       for row in self.grid]
        self.print_hidden_board(hidden_grid)  

    def print_hidden_board(self, hidden_grid):
        """Prints the current state of the hidden grid."""
        print("   " + " ".join([str(i) for i in range(len(hidden_grid))]))   
        print("  " + "--" * len(hidden_grid))  
        row_number = 0
        for row in hidden_grid:  
            print("%d |%s|" % (row_number, "|".join(row)))  
            row_number += 1
        print("\n")  

        
def get_computer_input(grid_size):
    """Generates random row and column coordinates within the grid size,
    for the computer's move."""
    row = random.randint(0, grid_size - 1)  
    col = random.randint(0, grid_size - 1)  
    return row, col  
