# asked chatgpt to do sudoku example lol
import tkinter as tk
from tkinter import messagebox

# Constants
WIDTH = 500
ROW = 9  # You can set this to 4 or 9 depending on the grid size
initial_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
# Initialize the main Tkinter window
root = tk.Tk()
root.title("Sudoku Game")

# Create a canvas for drawing the grid
canvas = tk.Canvas(root, width=WIDTH, height=WIDTH, bg="white")
canvas.grid(padx=5, pady=5)
width = WIDTH-5
cell_size = width / ROW
# Draw the grid lines
def draw_board():
    for i in range(ROW + 1):
        line_width = 3 if i % 3 == 0 else 1  # Thicker lines for every 3 rows/columns
        # Vertical lines
        canvas.create_line(i * cell_size+5, 5, i * cell_size+5, width+5, width=line_width)
        # Horizontal lines
        canvas.create_line(5, i * cell_size+5, width+5, i * cell_size+5, width=line_width)

# Function to check if the board is complete and valid
# Function to check if the board is complete and valid
def is_valid(board, row, col, num):
    # Check the row
    for i in range(ROW):
        if board[row][i] == num:
            return False
    # Check the column
    for i in range(ROW):
        if board[i][col] == num:
            return False
    # Check the 3x3 box
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False
    return True

# Function to check if the board is complete
def is_complete():
    for row in range(ROW):
        for col in range(ROW):
            num = int(cells[row][col].get() or 0)
            if num == 0 or not is_valid(board, row, col, num):
                return False
    return True

# Callback for cell input validation
def validate_input(row, col, text):
    if text.isdigit() and 1 <= int(text) <= 9:
        num = int(text)
        if is_valid(board, row, col, num):
            board[row][col] = num
            return True
        else:
            messagebox.showerror("Error", "Invalid move!")
            return False
    elif text == "":
        board[row][col] = 0
        return True
    return False
def solve_sudoku(board):
    for row in range(ROW):
        for col in range(ROW):
            if board[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0  # Reset on backtrack
                return False  # Trigger backtracking
    return True

# Function to automatically fill the board using the solver
def auto_solve():
    board_copy = [row[:] for row in initial_board]  # Copy the initial board for solving
    if solve_sudoku(board_copy):
        for i in range(ROW):
            for j in range(ROW):
                cells[i][j].delete(0, tk.END)
                cells[i][j].insert(0, str(board_copy[i][j]))
        messagebox.showinfo("Solved", "The puzzle has been solved!")
    else:
        messagebox.showerror("Unsolvable", "No solution exists for this puzzle.")


# Place cells in the grid (labels for fixed numbers and entry fields for empty cells)
cells = []
board = [row[:] for row in initial_board]  # Copy initial board for gameplay
for i in range(ROW):
    row = []
    for j in range(ROW):
        x0, y0 = j * cell_size, i * cell_size  # Top-left corner of the cell
        if initial_board[i][j] != 0:
            # Fixed cells as text on canvas
            canvas.create_text(
                x0 + cell_size / 2 + 5, y0 + cell_size / 2 + 5,
                text=str(initial_board[i][j]),
                font=("Arial", 20),
                fill="black"
            )
            row.append(None)
        else:
            # Editable cells
            entry = tk.Entry(root, width=2, font=("Arial", 20), justify="center", bg="white", borderwidth=0, highlightthickness=0)
            entry_window = canvas.create_window(x0 + cell_size / 2 + 5, y0 + cell_size / 2 + 5, window=entry, anchor="center")
            # Validation command for each cell
            vcmd = (root.register(validate_input), i, j, '%P')
            entry.config(validate="key", validatecommand=vcmd)
            row.append(entry)
    cells.append(row)

# Button to check if the solution is complete
def check_solution():
    if is_complete():
        messagebox.showinfo("Congratulations!", "You completed the Sudoku!")
    else:
        messagebox.showwarning("Incomplete or Invalid", "The puzzle is not solved correctly yet.")

check_button = tk.Button(root, text="Check Solution", command=check_solution)
check_button.grid()
check_button = tk.Button(root, text="Solve Automatically", command=auto_solve)
check_button.grid()

# Draw the initial board
draw_board()

# Run the Tkinter main loop
root.mainloop()







# import tkinter as tk
# from tkinter import messagebox
#
# class SudokuGUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Sudoku Game")
#         self.entries = [[None for _ in range(9)] for _ in range(9)]
#         self.create_grid()
#
#     def create_grid(self):
#         # Create a 9x9 grid of Entry widgets with borders for 3x3 sections
#         for row in range(9):
#             for col in range(9):
#                 # Configure thicker borders for 3x3 subgrids
#                 if row in [0, 3, 6] and col == 0:
#                     border_style = {"highlightbackground": "black", "highlightthickness": 1}
#                 elif row in [0, 3, 6] or col in [0, 3, 6]:
#                     border_style = {"highlightbackground": "black", "highlightthickness": 1}
#                 else:
#                     border_style = {"highlightbackground": "grey", "highlightthickness": 1}
#
#                 entry = tk.Entry(self.root, width=2, font=("Arial", 18), justify="center", **border_style)
#                 entry.grid(row=row, column=col, padx=2, pady=2)
#                 entry.bind("<FocusOut>", self.validate_input)
#                 self.entries[row][col] = entry
#
#         # Add a button to solve the puzzle
#         solve_button = tk.Button(self.root, text="Solve", command=self.solve_sudoku)
#         solve_button.grid(row=9, column=4, pady=10)
#
#     def validate_input(self, event):
#         # Ensures entries are valid numbers between 1 and 9
#         entry = event.widget
#         value = entry.get()
#         if value and (not value.isdigit() or int(value) < 1 or int(value) > 9):
#             messagebox.showwarning("Invalid Input", "Please enter a number between 1 and 9.")
#             entry.delete(0, tk.END)
#
#     def get_grid(self):
#         # Convert entries to a grid
#         grid = []
#         for row in range(9):
#             grid_row = []
#             for col in range(9):
#                 value = self.entries[row][col].get()
#                 grid_row.append(int(value) if value else 0)
#             grid.append(grid_row)
#         return grid
#
#     def set_grid(self, grid):
#         # Populate entries with a given grid (solution or preset puzzle)
#         for row in range(9):
#             for col in range(9):
#                 if grid[row][col] != 0:
#                     self.entries[row][col].delete(0, tk.END)
#                     self.entries[row][col].insert(0, str(grid[row][col]))
#
#     def is_valid(self, grid, row, col, num):
#         # Check if a number can be placed at grid[row][col]
#         for i in range(9):
#             if grid[row][i] == num or grid[i][col] == num:
#                 return False
#         start_row, start_col = 3 * (row // 3), 3 * (col // 3)
#         for i in range(3):
#             for j in range(3):
#                 if grid[start_row + i][start_col + j] == num:
#                     return False
#         return True
#
#     def solve(self, grid):
#         # Recursive backtracking function to solve the puzzle
#         for row in range(9):
#             for col in range(9):
#                 if grid[row][col] == 0:
#                     for num in range(1, 10):
#                         if self.is_valid(grid, row, col, num):
#                             grid[row][col] = num
#                             if self.solve(grid):
#                                 return True
#                             grid[row][col] = 0
#                     return False
#         return True
#
#     def solve_sudoku(self):
#         grid = self.get_grid()
#         if self.solve(grid):
#             self.set_grid(grid)
#         else:
#             messagebox.showinfo("Unsolvable", "This puzzle cannot be solved.")
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = SudokuGUI(root)
#     root.mainloop()