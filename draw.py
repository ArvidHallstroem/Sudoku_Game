# function to draw the Sudoku can draw any rows.
from turtle import Turtle

ROW = 9
WIDTH = 400
cellsize = WIDTH/ROW
X_CONST = -5 - WIDTH / 2
if ROW % 2 == 0:
    Y_CONST = 270
    y_pantry = -160
else:
    Y_CONST = 270 - cellsize
    y_pantry = -180

pantry = []
x, y = (X_CONST + cellsize / 2, y_pantry - cellsize / 2)
for i in range(ROW):
    pantry.append((x, y))
    x += cellsize

locs = []
y = Y_CONST + cellsize / 2
for a in range(ROW):
    temp = []
    x = X_CONST + cellsize / 2
    for b in range(ROW):
        temp.append((x, y))
        x += cellsize
    y -= cellsize
    locs.append(temp)

cell_occupied = []
for y in range(ROW):
    temp_cell = []
    for x in range(ROW):
        temp_cell.append(0)
    cell_occupied.append(temp_cell)

def draw_board(width, rows, line):
    line.penup()
    line.hideturtle()
    draw_cells(width, rows, line)
    draw_pantry(width, rows, line)
def draw_cells(width, rows, line):
    # if rows == 4 or rows == 9:
        # line.color(180, 180, 180)
    cell = width / rows
    if rows % 2 == 0:
        line.goto(X_CONST, Y_CONST)
    else:
        line.goto(X_CONST, 270 - cell)
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
        draw_cells(width, 2, line)
    elif rows == 9:
        line.width(3)
        draw_cells(width, 3, line)
    line.penup()


def draw_pantry(width, rows, line):
    line.width(1)
    line.goto(X_CONST, y_pantry)
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
    line.goto(X_CONST, y_pantry)
    line.pendown()
    line.width(3)
    for i in range(2):
        line.fd(width)
        line.right(90)
        line.forward(cell)
        line.right(90)
