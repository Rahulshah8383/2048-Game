# 2048 Game
This is a Python implementation of the popular game 2048. The game is played on a 4x4 grid, where the player's goal is to combine tiles with the same number to reach the 2048 tile. The game continues until the player reaches the 2048 tile or there are no more valid moves left.

## How to Play
- Use the arrow keys (up, down, left, right) to move the tiles in the respective direction.
- When two tiles with the same number touch, they merge into one tile with the sum of their values.
- After each move, a new '2' tile will randomly appear on the grid in an empty space.
- Continue merging tiles and strategically planning your moves to reach the 2048 tile.
- The goal is to create a tile with the value of 2048.
- The game is over when there are no more possible moves or when the goal is reached.

## Features
- Start a new game and initialize the game grid.
- Add a new '2' tile to the game grid at a random empty position.
- Perform moves in four directions: up, down, left, and right.
- Merge adjacent tiles of the same value.
- Compress the game grid by shifting tiles to the left and filling empty spaces with zeros.
- Check the current state of the game (won, game not over, or lost).
- Randomness in tile generation to ensure a varied game experience.

## Screenshot

p align="center">
  <img src="https://cloud.githubusercontent.com/assets/1175750/8614312/280e5dc2-26f1-11e5-9f1f-5891c3ca8b26.png" alt="Screenshot"/>
</p>

That screenshot is fake, by the way. I never reached 2048 :smile:


## Dependencies
This game has no external dependencies. It is written in Python and uses only the standard library.

## Contributing
Contributions to improve the game are welcome! If you find any issues or have suggestions for new features, feel free to open an issue or submit a pull request.

Please ensure that your contributions adhere to the repository's code style and follow the existing conventions.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

Have fun playing 2048! Strategize your moves and aim for the elusive 2048 tile. If you have any questions or need further assistance, please feel free to reach out.