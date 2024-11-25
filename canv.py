import tkinter as tk
window = tk.Tk()
window.title("Sudoku Game")
canvas = tk.Canvas(window, width=800, height=800)
canvas.grid(sticky='nsew')