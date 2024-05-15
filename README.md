# Battleship Game

## Overview

This Battleship game is a command-line implementation of the classic board game where two players take turns to guess the locations of each other's ships. The first player to sink all of the opponent's ships wins.

## Features

- Set up a board with a predefined number of ships.
- Make guesses on the opponent's board.
- Visual feedback for hits and misses.
- Simple and intuitive text-based interface.

## Classes and Methods

### Class: `Player`

#### `__init__(self, name)`
Initializes a player with a name, a personal board, and a guessing board.

#### `setup_board(self)`
Prompts the player to set up their ships on the board.

#### `make_guess(self, opponent_board)`
Prompts the player to make a guess on the opponent's board and returns the guessed position.

### Class: `Board`

#### `__init__(self)`
Initializes the board with a size of 10x10, five ships, and sets up the grid with empty spaces. Also, sets up a dictionary to map column letters to indices.

#### `setup_ships(self)`
Prompts the player to place ships on the board at specified positions.

#### `setup_position(self)`
Prompts the player to enter a valid row and column position and returns the corresponding indices.

#### `print_board(self)`
Prints the current state of the board.

### Class: `Game`

#### `__init__(self, player1_name, player2_name)`
Initializes the game with two players and sets up the game state.

#### `play(self)`
Runs the main game loop where players take turns to make guesses until all ships are sunk.

### Function: `print_title()`
Prints the title art of the game.

### Function: `main()`
Main function to start the game, get player names, and initiate the game play.

## How to Play

1. Run the script.
2. Enter the names for Player 1 and Player 2 when prompted.
3. Each player will take turns to set up their board by placing 5 ships.
4. Once the boards are set, players will take turns guessing the location of the opponent's ships.
5. The game continues until all ships of one player are sunk.
6. The player who sinks all the opponent's ships first wins.

## Example

### Starting the Game

![](https://media.giphy.com/media/SLET43izSdZk3kMP1Q/giphy.gif)

### Setting Up the Board

![](https://media.giphy.com/media/iKLWfTIEU3oQe0Lyka/giphy.gif)

### Making Guesses

![](https://media.giphy.com/media/JbOVu2Qpx6895ecBC0/giphy.gif)

## Dependencies

This game is implemented in Python and does not require any external libraries.

## Installation

1. Clone the repository or download the script.
2. Ensure you have Python installed (version 3.12.3 recommended).
3. Run the script using the command:
   ```sh
   python battleship.py

## License

This project is licensed under the MIT License.

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or new features.
