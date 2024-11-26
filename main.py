import tkinter as tk
from tkinter import messagebox
from functions import *

# Initialize the main window
from canv import root

# Title Label
title_label = tk.Label(
    root,
    text="Welcome to Sudoku!",
    font=("Arial",20,"bold"),
    bg="#f0f8ff",
    fg="#333"
)
title_label.pack(pady=20)

# Normal Mode Button
normal_button = tk.Button(
    root,
    text="Normal Mode",
    font=("Arial",14,"bold"),
    bg="#add8e6",
    fg="#333",
    activebackground="#87ceeb",
    activeforeground="#fff",
    width=15,
    height=2,
    command=open_normal_mode
)
normal_button.pack(pady=10)

# Kid's Mode Button
kids_button = tk.Button(
    root,
    text="Kid's Mode",
    font=("Arial",14,"bold"),
    bg="#ffcccb",
    fg="#333",
    width=15,
    height=2,
    command=open_kids_mode
)
kids_button.pack(pady=10)

# Run the application
root.mainloop()