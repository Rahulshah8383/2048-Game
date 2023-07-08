from tkinter import Frame, Label, Button, CENTER
import time
import LogicsFinal
import constants as c

class Game2048(Frame):
    """
    The Game2048 class represents the main game window for the 2048 game.

    It extends the tkinter Frame class and handles the initialization of the game,
    updating the grid cells, and processing key events.

    Attributes:
        grid_cells (list): A 2D list representing the grid cells in the game.
        matrix (list): A 2D list representing the game matrix.
        commands (dict): A dictionary mapping key events to corresponding move methods.
    """

    def __init__(self):
        """Initialize the Game2048 object."""
        Frame.__init__(self)
        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>", self.key_down)
        self.commands = {
            c.KEY_UP: LogicsFinal.move_up,
            c.KEY_DOWN: LogicsFinal.move_down,
            c.KEY_LEFT: LogicsFinal.move_left,
            c.KEY_RIGHT: LogicsFinal.move_right
        }

        self.grid_cells = []
        self.init_grid()         # Initialize the grid cells
        self.init_matrix()       # Initialize the game matrix
        self.update_grid_cells() # Update the grid cells with the numbers from the matrix

        self.new_game_button = Button(self, text="New Game", command=self.start_new_game, bg="#8f7a66", fg="white", width=10, height=2)
        self.new_game_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.timer_label = Label(self, text="Time: 0s", font=("Verdana", 12))
        self.timer_label.grid(row=2, column=0, padx=10, pady=10)

        self.start_time = time.time()
        self.update_timer()

        self.mainloop()

    def init_grid(self):
        """Initialize the grid with empty cells."""
        background = Frame(self, bg=c.BACKGROUND_COLOR_GAME, width=c.SIZE, height=c.SIZE)
        background.grid()

        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                cell = Frame(background, bg=c.BACKGROUND_COLOR_CELL_EMPTY, width=c.SIZE / c.GRID_LEN,
                             height=c.SIZE / c.GRID_LEN)
                cell.grid(row=i, column=j, padx=c.GRID_PADDING, pady=c.GRID_PADDING)
                t = Label(master=cell, text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                          justify=CENTER, font=c.FONT, width=5, height=2)
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)

    def init_matrix(self):
        """Initialize the game matrix."""
        self.matrix = LogicsFinal.start_game()
        LogicsFinal.add_new_2(self.matrix)
        LogicsFinal.add_new_2(self.matrix)

    def update_grid_cells(self):
        """Update the grid cells with the numbers from the matrix."""
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(new_number),
                                                    bg=c.BACKGROUND_COLOR_DICT[new_number],
                                                    fg=c.CELL_COLOR_DICT[new_number])
        self.update_idletasks()

    def start_new_game(self):
        """Start a new game."""
        self.grid_cells[1][1].configure(text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
        self.grid_cells[1][2].configure(text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
        self.matrix = LogicsFinal.start_game()
        LogicsFinal.add_new_2(self.matrix)
        LogicsFinal.add_new_2(self.matrix)
        self.update_grid_cells()

    def update_timer(self):
        """Update the timer label with the elapsed time."""
        elapsed_time = int(time.time() - self.start_time)
        self.timer_label.configure(text=f"Time: {elapsed_time}s")
        self.timer_label.after(1000, self.update_timer)

    def start_new_game(self):
        """Start a new game."""
        self.grid_cells[1][1].configure(text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
        self.grid_cells[1][2].configure(text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
        self.matrix = LogicsFinal.start_game()
        LogicsFinal.add_new_2(self.matrix)
        LogicsFinal.add_new_2(self.matrix)
        self.update_grid_cells()

        self.start_time = time.time()  # Reset the start time

    def key_down(self, event):
        """Process key events for game controls."""
        key = repr(event.keysym)
        if key in self.commands:
            self.matrix, changed = self.commands[key](self.matrix)
            if changed:
                LogicsFinal.add_new_2(self.matrix)
                self.update_grid_cells()
                changed = False
                if LogicsFinal.get_current_state(self.matrix) == 'WON':
                    self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Win!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                if LogicsFinal.get_current_state(self.matrix) == 'LOST':
                    self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Lose!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)

gamegrid = Game2048()

# Create an instance of the Game2048 class to start the game
