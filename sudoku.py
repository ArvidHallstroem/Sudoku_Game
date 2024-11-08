import tkinter as tk
from tkinter import messagebox

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Game")
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()

    def create_grid(self):
        # Create a 9x9 grid of Entry widgets with borders for 3x3 sections
        for row in range(9):
            for col in range(9):
                # Configure thicker borders for 3x3 subgrids
                if row in [0, 3, 6] and col == 0:
                    border_style = {"highlightbackground": "black", "highlightthickness": 1}
                elif row in [0, 3, 6] or col in [0, 3, 6]:
                    border_style = {"highlightbackground": "black", "highlightthickness": 1}
                else:
                    border_style = {"highlightbackground": "grey", "highlightthickness": 1}

                entry = tk.Entry(self.root, width=2, font=("Arial", 18), justify="center", **border_style)
                entry.grid(row=row, column=col, padx=2, pady=2)
                entry.bind("<FocusOut>", self.validate_input)
                self.entries[row][col] = entry

        # Add a button to solve the puzzle
        solve_button = tk.Button(self.root, text="Solve", command=self.solve_sudoku)
        solve_button.grid(row=9, column=4, pady=10)

    def validate_input(self, event):
        # Ensures entries are valid numbers between 1 and 9
        entry = event.widget
        value = entry.get()
        if value and (not value.isdigit() or int(value) < 1 or int(value) > 9):
            messagebox.showwarning("Invalid Input", "Please enter a number between 1 and 9.")
            entry.delete(0, tk.END)

    def get_grid(self):
        # Convert entries to a grid
        grid = []
        for row in range(9):
            grid_row = []
            for col in range(9):
                value = self.entries[row][col].get()
                grid_row.append(int(value) if value else 0)
            grid.append(grid_row)
        return grid

    def set_grid(self, grid):
        # Populate entries with a given grid (solution or preset puzzle)
        for row in range(9):
            for col in range(9):
                if grid[row][col] != 0:
                    self.entries[row][col].delete(0, tk.END)
                    self.entries[row][col].insert(0, str(grid[row][col]))

    def is_valid(self, grid, row, col, num):
        # Check if a number can be placed at grid[row][col]
        for i in range(9):
            if grid[row][i] == num or grid[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if grid[start_row + i][start_col + j] == num:
                    return False
        return True

    def solve(self, grid):
        # Recursive backtracking function to solve the puzzle
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(grid, row, col, num):
                            grid[row][col] = num
                            if self.solve(grid):
                                return True
                            grid[row][col] = 0
                    return False
        return True

    def solve_sudoku(self):
        grid = self.get_grid()
        if self.solve(grid):
            self.set_grid(grid)
        else:
            messagebox.showinfo("Unsolvable", "This puzzle cannot be solved.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()
