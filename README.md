
# The Battleships Game

A classic Battleships game where the player competes against the computer to sink each other's ships. The game features a variable grid size, a customizable number of ships, and player input for making guesses. The objective is to sink all of the opponent's ships before they sink yours.

## Game Flow
- The game begins by asking the user for their name, grid size, and the number of ships.
- The player and computer boards are initialized with random ship placement.
- The game loop starts, with turns alternating between the player and computer.
- On the player's turn, they input their guess (row and column) for a ship on the computer's board.
- The computer's turn consists of randomly generated guesses.
- The game continues until either the user or the computer has no remaining ships.
- The result is displayed, showing whether the user or computer has won the game.

## Error Handling
- The Battleships game includes built-in error handling to manage incorrect user inputs, ensuring a smooth gameplay experience. If the user provides invalid input when prompted, the game will display an appropriate error message and ask the user to try again.

### Examples of Error Handling
- **Grid size input**: If the user enters a non-numeric input or a number outside the valid range (3-15), the game will display an error message and prompt the user to enter a valid grid size.
- **Number of ships input**: If the user enters a non-numeric input or a number outside the valid range (1 to the grid size), the game will display an error message and prompt the user to enter a valid number of ships.
- **Row and column guesses**: If the user enters non-numeric input, input outside the grid size, or guesses a location they have already tried, the game will display an error message and prompt the user to enter valid row and column coordinates.

### Implementation
- The error handling is implemented using "try-except" blocks and "while" loops in the code. This ensures that the game will continue to ask for valid input until the user provides it, preventing the game from crashing or entering an undefined state due to incorrect user input.

## Features
- Customizable grid size (3 to 15)
- Customizable number of ships (1 to the grid size)
- Display of player and computer boards with relevant symbols
- Randomized ship placement for both player and computer
- User input for row and column guesses
- Randomized computer guesses
- Hit and miss feedback for both player and computer
- Scoring and ship tracking
- Win/lose game result

## Symbols
- **S**: Ship
- **X**: Hit
- **0**: User Miss on Computer's Grid
- **#**: Computer Hit

## Future Features
- Allow the player to choose the positions of their ships.
- Introduce ships of different sizes for more complex gameplay.

## Data Model 
The data model consists of classes and functions that represent game elements and their interactions. The primary classes used are `BaseBoard`, `PlayerBoard`, and `ComputerBoard`. The game also has utility functions to handle user input and computer input.

### Classes
- **BaseBoard**: This is the base class for the game board, containing common properties and methods for both the player's and computer's boards. The class initializes the grid size, number of ships, creates the grid, and places the ships on the grid. It also contains a method to print the current state of the grid.

- **PlayerBoard**: This class is derived from the `BaseBoard` class and represents the player's board. It initializes the player's name and calls the parent constructor. The class also contains a method to display the player's board.

- **ComputerBoard**: This class is derived from the `BaseBoard` class and represents the computer's board. It contains a method to display the computer's board with ships hidden and a method to print the current state of the hidden grid.

### Utility Functions
- **get_computer_input(grid_size)**: This function generates random row and column coordinates within the grid size for the computer's move.
- **get_user_input(grid_size)**: This function prompts the user for row and column coordinates within the grid size. It includes error handling to ensure the input is valid.

### Game Data Flow
The game's data model primarily flows through the main game loop, where the player and computer take turns interacting with their respective game boards. During each turn, the user input or computer input is used to update the state of the game boards. The game continues until either the user or the computer has no remaining ships.

## Validator and Testing
- The code was passed through the PEP8 Python Validator with no errors found.
- Invalid inputs are handled by displaying an appropriate error message and prompting the user to try again.
- The game was tested in a local terminal and in the Code Institute Haruku Terminal.

## Bugs
- No bugs were found during testing.

## Deployment

This project was designed to be run in a local or educational terminal environment.

### Steps for Running Locally
- Ensure Python 3.6 or above is installed on your system.
- Clone the repository or download the code files.
- Navigate to the project directory.
- Run the game by executing `python battleships_game.py` in your terminal.

## Credits 
- Code Institute for providing the deployment terminal and educational resources.
- Wikipedia for information on the classic Battleships game.
