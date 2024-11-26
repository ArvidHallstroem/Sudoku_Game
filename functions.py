import tkinter as tk
from turtle import RawTurtle, TurtleScreen
from draw import Draw
from storage import compute
from block import Block
from canv import root

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
    normal_window.geometry("550x700")
    normal_window.configure(bg="#add8e6")
    label = tk.Label(normal_window,text="Welcome to Normal Mode!",font=("Arial",16),bg="#add8e6",fg="#333")
    label.pack(pady=20)
    canvas = tk.Canvas(normal_window,width=500,height=550)
    canvas.pack()
    game(canvas,9,400)
    # Close button for the new window
    close_button = tk.Button(
        normal_window,
        text="Close",
        font=("Arial",12),
        command=normal_window.destroy
    )
    close_button.pack(pady=20)


# Function to open a new window for Kid's Mode
def open_kids_mode():
    import storage
    storage.ROW = 4
    root.destroy()
    kids_window = tk.Tk()
    kids_window.title("Kid's Mode")
    kids_window.geometry("550x700")
    kids_window.configure(bg="#ffcccb")

    label = tk.Label(kids_window, text="Welcome to Kid's Mode!",font=("Arial",16),bg="#ffcccb",fg="#333")
    label.pack(pady=20)
    canvas = tk.Canvas(kids_window, width=402, height=512, borderwidth=0, highlightthickness=0)
    canvas.pack()
    game(canvas, 4, 400)
    # Close button for the new window
    close_button = tk.Button(
        kids_window,
        text="Close",
        font=("Arial",12),
        command=kids_window.destroy
    )
    close_button.pack(pady=20)
def check_logic():
    for row in blocks:
        for a in row:
            for b in row:
                pass