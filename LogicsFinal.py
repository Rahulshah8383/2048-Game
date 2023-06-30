import random

def start_game():
    """
    Initialize the game grid with a 4x4 matrix filled with zeros.

    Returns:
        list: The initialized game grid.
    """
    mat = []
    for i in range(4):
        mat.append([0] * 4)
    return mat

def add_new_2(mat):
    """
    Add a new '2' tile to the game grid at a random empty position.

    Parameters:
        mat (list): The game grid.

    Returns:
        None
    """
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    while mat[r][c] != 0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    mat[r][c] = 2

def reverse(mat):
    """
    Reverse the order of elements in each row of the game grid.

    Parameters:
        mat (list): The game grid.

    Returns:
        list: The game grid with reversed rows.
    """
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][4 - j - 1])

    return new_mat

def transpose(mat):
    """
    Transpose the game grid (rows become columns and columns become rows).

    Parameters:
        mat (list): The game grid.

    Returns:
        list: The transposed game grid.
    """
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat

def merge(mat):
    """
    Merge adjacent tiles of the same value in each row of the game grid.

    Parameters:
        mat (list): The game grid.

    Returns:
        tuple: A tuple containing the merged game grid and a flag indicating if any merge occurred.
    """
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] = mat[i][j] * 2
                mat[i][j + 1] = 0
                changed = True
    return mat, changed

def compress(mat):
    """
    Compress the game grid by shifting all tiles to the left and filling empty spaces with zeros.

    Parameters:
        mat (list): The game grid.

    Returns:
        tuple: A tuple containing the compressed game grid and a flag indicating if any compression occurred.
    """
    changed = False
    new_mat = []
    for i in range(4):
        new_mat.append([0] * 4)

    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if j != pos:
                    changed = True
                pos += 1
    return new_mat, changed

def move_up(grid):
    """
    Perform a move upwards on the game grid.

    Parameters:
        grid (list): The game grid.

    Returns:
        tuple: A tuple containing the updated game grid after the move and a flag indicating if any tiles moved.
    """
    transposed_grid = transpose(grid)
    new_grid, changed1 = compress(transposed_grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid, _ = compress(new_grid)
    final_grid = transpose(new_grid)
    return final_grid, changed

def move_down(grid):
    """
    Perform a move downwards on the game grid.

    Parameters:
        grid (list): The game grid.

    Returns:
        tuple: A tuple containing the updated game grid after the move and a flag indicating if any tiles moved.
    """
    transposed_grid = transpose(grid)
    reversed_grid = reverse(transposed_grid)
    new_grid, changed1 = compress(reversed_grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid, _ = compress(new_grid)
    final_reversed_grid = reverse(new_grid)
    final_grid = transpose(final_reversed_grid)
    return final_grid, changed

def move_right(grid):
    """
    Perform a move to the right on the game grid.

    Parameters:
        grid (list): The game grid.

    Returns:
        tuple: A tuple containing the updated game grid after the move and a flag indicating if any tiles moved.
    """
    reversed_grid = reverse(grid)
    new_grid, changed1 = compress(reversed_grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid, _ = compress(new_grid)
    final_grid = reverse(new_grid)
    return final_grid, changed

def move_left(grid):
    """
    Perform a move to the left on the game grid.

    Parameters:
        grid (list): The game grid.

    Returns:
        tuple: A tuple containing the updated game grid after the move and a flag indicating if any tiles moved.
    """
    new_grid, changed1 = compress(grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid, _ = compress(new_grid)
    return new_grid, changed

def get_current_state(mat):
    """
    Get the current state of the game based on the game grid.

    Parameters:
        mat (list): The game grid.

    Returns:
        str: The current state of the game ('WON', 'GAME NOT OVER', or 'LOST').
    """
    # Check if 2048 tile is present
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return 'WON'
    # Check if any empty cells are present
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return 'GAME NOT OVER'
    # Check for any adjacent equal tiles (except last row and last column)
    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i + 1][j] or mat[i][j] == mat[i][j + 1]:
                return 'GAME NOT OVER'
    # Check for any adjacent equal tiles in the last row
    for j in range(3):
        if mat[3][j] == mat[3][j + 1]:
            return 'GAME NOT OVER'
    # Check for any adjacent equal tiles in the last column
    for i in range(3):
        if mat[i][3] == mat[i + 1][3]:
            return 'GAME NOT OVER'

    return 'LOST'
