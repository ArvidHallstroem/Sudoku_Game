# function to draw the Sudoku can draw any rows.
from turtle import *

def draw_board(width, rows):
    draw_cells(width, rows)
    draw_pantry(width, rows)
def draw_cells(width, rows):
    line = Turtle()
    line.penup()
    line.hideturtle()
    if rows == 4 or rows == 9:
        line.color(180, 180, 180)
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
    line.color("black")
    if rows == 4:
        draw_cells(width, 2)
    elif rows == 9:
        draw_cells(width, 3)


def draw_pantry(width, rows):
    line1 = Turtle()
    line1.penup()
    line1.color(180, 180, 180)
    line1.hideturtle()
    line1.goto(-205, -160)
    line1.pendown()
    cell = width/rows
    for i in range(int(rows/2)):
        line1.fd(cell)
        line1.right(90)
        line1.fd(cell)
        for x in range(2):
            line1.left(90)
            line1.fd(cell)
        line1.right(90)
    line1.color("black")
    line1.penup()
    line1.goto(-205, -160)
    line1.pendown()
    for i in range(2):
        line1.fd(width)
        line1.right(90)
        line1.forward(cell)
        line1.right(90)
