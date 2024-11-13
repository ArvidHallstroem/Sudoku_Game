# function to draw the Sudoku can draw any rows.
from turtle import *

ROW = 4
WIDTH = 400
cellsize = WIDTH/ROW
line = Turtle()
line.penup()
line.hideturtle()
pantry, locs = [], []
X, y = -205+cellsize/2, -160-cellsize/2
for i in range(ROW):
    pantry.append((X, y))
    X += cellsize
y = 220
for a in range(ROW):
    temp = []
    x = X
    for b in range(ROW):
        temp.append((x, y))
        x += cellsize
    y -= cellsize
    locs.append(temp)
def draw_board(width, rows):
    draw_cells(width, rows)
    draw_pantry(width, rows)
def draw_cells(width, rows):
    # if rows == 4 or rows == 9:
        # line.color(180, 180, 180)
    cell = width / rows
    if rows % 2 == 0:
        line.goto(-205, 270)
    else:
        line.goto(-205, 270 - cell)
    line.pendown()
    for i in range(int(rows / 2)):
        line.forward(width)
        line.right(90)
        line.forward(cell)
        line.right(90)
        line.forward(width)
        line.left(90)
        line.forward(cell)
        line.left(90)
    line.forward(width)
    line.left(90)
    for i in range(int(rows / 2)):
        line.forward(width)
        line.left(90)
        line.forward(cell)
        line.left(90)
        line.forward(width)
        line.right(90)
        line.forward(cell)
        line.right(90)
    line.forward(width)
    if rows % 2 != 0:
        line.right(90)
        line.forward(width - cell)
        line.setheading(180)
        line.forward(width)
        line.left(90)
        line.forward(width)
    line.setheading(0)
    if rows == 4:
        line.width(3)
        draw_cells(width, 2)
    elif rows == 9:
        line.width(3)
        draw_cells(width, 3)
    line.penup()


def draw_pantry(width, rows):
    line.width(1)
    line.goto(-205, -160)
    line.pendown()
    cell = width/rows
    for i in range(int(rows/2)):
        line.fd(cell)
        line.right(90)
        line.fd(cell)
        for x in range(2):
            line.left(90)
            line.fd(cell)
        line.right(90)
    line.color("black")
    line.penup()
    line.goto(-205, -160)
    line.pendown()
    line.width(3)
    for i in range(2):
        line.fd(width)
        line.right(90)
        line.forward(cell)
        line.right(90)
