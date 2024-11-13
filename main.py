# Starting on the 4x4 🫠
from turtle import *
from draw import *
from block import Block

screen = Screen()
screen.bgcolor("white")
screen.setup(500, 600)
screen.title("Sudoku Game")
screen.colormode(255)
screen.tracer(0)
# locs = [[(-155, 220), (-55, 220), (45, 220), (145, 220)], [(-155, 120), (-55, 120), (45, 120), (145, 120)],
# [(-155, 20), (-55, 20), (45, 20), (145, 20)], [(-155, -80), (-55, -80), (45, -80), (145, -80)]]

# pantry = [(-155, -210), (-55, -210), (45, -210), (145, -210)]

blocks, tempblocks = [], []
colors = ["red", "orange","yellow", "green","cyan", "blue", "purple","magenta", "pink"]
for x in range(ROW):
    for y in range(ROW):
        temp = (Block(WIDTH/ROW))
        temp.color(colors[x])
        temp.goto(pantry[x])
        tempblocks.append(temp)
    blocks.append(tempblocks)

draw_board(WIDTH, ROW)


screen.tracer(1)
while True:
    screen.update()
screen.mainloop()