from turtle import *

screen = Screen()
screen.bgcolor("white")
screen.setup(600, 500)
screen.title("Kids Sudoku")
screen.tracer(0)

line = Turtle()
line.penup()
line.hideturtle()
line.goto(-300, -50)
line.pendown()

screen.mainloop()