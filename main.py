import tkinter as tk
from tkinter import messagebox
from functions import *

# Initialize the main window
from canv import root
root.title("GRIDMASTER")
root.geometry("550x700")
root.configure(bg="#ffffff")

# Function that gradually changes button color
def change_colors_over_time(button, start_fg, end_fg, start_bg, end_bg, duration):
    steps = 30  # Number of steps for transition to occur
    # Hex color to rgb
    def hex_to_rgb(hex_color):
        return [int(hex_color[i:i+2], 16) for i in range(1, len(hex_color), 2)]
    
    start_fg_rgb, end_fg_rgb = hex_to_rgb(start_fg), hex_to_rgb(end_fg)
    start_bg_rgb, end_bg_rgb = hex_to_rgb(start_bg), hex_to_rgb(end_bg)
    
    def step_color_change(step):
        # Calculate intermediate colors for each component
        new_fg_rgb = [
            int(start_fg_rgb[i] + (end_fg_rgb[i] - start_fg_rgb[i]) * step / steps)
            for i in range(3)
        ]
        new_bg_rgb = [
            int(start_bg_rgb[i] + (end_bg_rgb[i] - start_bg_rgb[i]) * step / steps)
            for i in range(3)
        ]
        
        # Update the button's color dynamically
        button.config(
            fg=f'#{new_fg_rgb[0]:02x}{new_fg_rgb[1]:02x}{new_fg_rgb[2]:02x}',
            bg=f'#{new_bg_rgb[0]:02x}{new_bg_rgb[1]:02x}{new_bg_rgb[2]:02x}'
        )
        
        if step < steps:
            button.after(duration // steps, step_color_change, step + 1)

    step_color_change(0)

# Title Label
title_label = tk.Label(
    root,
    text="GRIDMASTER",
    font=("Times New Roman", 20),
    bg="#ffffff",
    fg="#333333",
    padx=20,
    pady=20,
)
title_label.pack(pady=(40, 20))

# Button creation helper function
def create_button(text, command, button_state):
    button = tk.Button(
        root,
        text=text,
        font=("Times New Roman", 14),
        bg="#ffffff",
        fg="#333333",
        relief="solid",
        width=15,
        height=2,
        bd=3,
        command=command
    )
    button.pack(pady=20)

    # Hover effect
    def on_hover(e, button, button_state):
        if button_state["hovered"]:
            change_colors_over_time(button, "#ffffff", "#333333", "#000000", "#ffffff", 125)
        else:
            change_colors_over_time(button, "#333333", "#ffffff", "#ffffff", "#000000", 125)
        button_state["hovered"] = not button_state["hovered"]

    button.bind("<Enter>", lambda e: on_hover(e, button, button_state))
    return button

# Button states
normal_button_state = {"hovered": False}
kids_button_state = {"hovered": False}

# Create Normal and Kids Mode buttons
normal_button = create_button("Normal Mode", open_normal_mode, normal_button_state)
kids_button = create_button("Kid's Mode", open_kids_mode, kids_button_state)

# Run the application
root.mainloop()
