import tkinter as tk
from turtle import RawTurtle, TurtleScreen
from draw import Draw
from storage import compute
from block import Block
from canv import root

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

# Function to create buttons with hover effect
def create_hover_button(window, text, command, width=15, height=2, font=("Times New Roman", 14)):
    button = tk.Button(
        window,
        text=text,
        font=font,
        bg="#ffffff",
        fg="#333333",
        relief="solid",
        width=width,
        height=height,
        bd=3,
        command=command
    )

    button_state = {"hovered": False}

    def on_button_hover(e):
        if button_state["hovered"]:
            change_colors_over_time(button, "#ffffff", "#333333", "#000000", "#ffffff", 125)
        else:
            change_colors_over_time(button, "#333333", "#ffffff", "#ffffff", "#000000", 125)
        button_state["hovered"] = not button_state["hovered"]

    button.bind("<Enter>", on_button_hover)

    return button

cell_occupied = Block.cell_occupied
blocks,tempblocks = [],[]
def game(canvas, row, width):
    scr = TurtleScreen(canvas)
    t = RawTurtle(scr)
    drawer = Draw(row,width)
    scr.tracer(0)
    t.speed(0)
    drawer.draw_board(width,row,t)
    global blocks
    sets = ['christmas_images','halloween_images']
    colors = ["red","orange","yellow","green","cyan","blue","purple","magenta","pink"]
    pantry,locs,cell_occupied,cellsize = compute(row,width)
    for x in range(row):
        tempblocks = []
        for y in range(row):
            if row == 4:
                scr.addshape(f'gifs/christmas_images/{x+1}.gif')
                shape = f'gifs/christmas_images/{x+1}.gif'
            else:
                shape = 'square'
            temp = Block(row,width,shape, canvas)
            temp.color(colors[x])
            temp.goto(pantry[x])
            temp.old_pos = pantry[x]
            tempblocks.append(temp)
        blocks.append(tempblocks)
    scr.tracer(1)
    print(blocks)
# Function to open a new window for Normal Mode
def open_normal_mode():
    import storage
    storage.ROW = 4 
    root.destroy()

    normal_window = tk.Tk()
    normal_window.title("Normal Mode")
    normal_window.configure(bg="#ffffff")

    # Title label
    label = tk.Label(
        normal_window, 
        text="NORMAL MODE", 
        font=("Times New Roman", 20), 
        bg="#ffffff", 
        fg="#333"
    )
    label.pack(pady=(20, 10))

    # Create a frame to hold the canvas and make it scrollable
    scrollable_frame = tk.Frame(normal_window)
    scrollable_frame.pack(fill="both", expand=True)

    # Create a canvas to draw the game board
    canvas = tk.Canvas(scrollable_frame, width=500, height=550)
    canvas.pack(padx=10, pady=(10, 20))

    # Call the game function to draw the board
    game(canvas, 9, 400)

    # Create the close button at the bottom
    close_button = create_hover_button(
        normal_window, 
        "Close", 
        normal_window.destroy
    )
    close_button.pack(pady=20)

    # Ensures that window fits all the content
    normal_window.update_idletasks()
    total_height = normal_window.winfo_reqheight()
    normal_window.geometry(f"550x{total_height}")


# Function to open a new window for Kid's Mode
def open_kids_mode():
    import storage
    storage.ROW = 4
    root.destroy()
    kids_window = tk.Tk()
    kids_window.title("KIDS MODE")
    kids_window.geometry("550x700")
    kids_window.configure(bg="#ffcccb")

    label = tk.Label(kids_window, text="KIDS MODE", font=("Times New Roman", 20), bg="#ffcccb", fg="#333")
    label.pack(pady=40)

    canvas = tk.Canvas(kids_window, width=550, height=550, borderwidth=0, highlightthickness=0)
    canvas.pack(pady=20)
    game(canvas, 4, 400)

    # Close button for the new window
    close_button = tk.Button(
        kids_window,
        text="Close",
        font=("Times New Roman", 14),
        bg="#ffffff",
        fg="#333333",
        relief="solid",
        width=15,
        height=2,
        bd=3,
        command=kids_window.destroy
    )
    close_button.pack(pady=20)
    kids_window.mainloop()
