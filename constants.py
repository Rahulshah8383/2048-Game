"""
Constants for the 2048 game.
"""

# Size of the game window
# Change this value to modify the overall size of the game window.
SIZE = 400

# Number of rows and columns in the grid
# Change this value to modify the size of the grid.
GRID_LEN = 4

# Padding between cells in the grid
# Change this value to modify the spacing between cells in the grid.
GRID_PADDING = 10

# Background color of the game window
# Change this value to modify the background color of the game window.
BACKGROUND_COLOR_GAME = "#92877d"

# Background color of empty cells in the grid
# Change this value to modify the background color of empty cells in the grid.
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"

# Background color dictionary for non-empty cells in the grid
# Modify this dictionary to change the background color of different numbers in the grid.
BACKGROUND_COLOR_DICT = {
    2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
    16: "#f59563", 32: "#f67c5f", 64: "#f65e3b",
    128: "#edcf72", 256: "#edcc61", 512: "#edc850",
    1024: "#edc53f", 2048: "#edc22e",
    4096: "#eee4da", 8192: "#edc22e", 16384: "#f2b179",
    32768: "#f59563", 65536: "#f67c5f",
}

# Cell color dictionary for numbers in the grid
# Modify this dictionary to change the font color of different numbers in the grid.
CELL_COLOR_DICT = {
    2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2",
    32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2",
    256: "#f9f6f2", 512: "#f9f6f2", 1024: "#f9f6f2",
    2048: "#f9f6f2",
    4096: "#776e65", 8192: "#f9f6f2", 16384: "#776e65",
    32768: "#776e65", 65536: "#f9f6f2",
}

# Font settings for numbers in the grid
# Change these values to modify the font style and size of numbers in the grid.
FONT = ("Verdana", 30, "bold")

# Keyboard keys for game controls
# Change these values to modify the keyboard keys for different game controls.
KEY_UP = "'Up'"
KEY_DOWN = "'Down'"
KEY_LEFT = "'Left'"
KEY_RIGHT = "'Right'"
