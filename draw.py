# function to draw the Sudoku can draw any rows.
class Draw():
    def __init__(self, row, width):
        cellsize = width/row
        self.X_CONST = -width / 2
        if row % 2 == 0:
            self.Y_CONST = 255
            self.y_pantry = -155
        else:
            self.Y_CONST = 250 - cellsize
            self.y_pantry = -180
    def draw_board(self, width, rows, line):
        line.penup()
        line.hideturtle()
        self.draw_cells(width, rows, line)
        self.draw_pantry(width, rows, line)
    def draw_cells(self, width, rows, line):
        # if rows == 4 or rows == 9:
            # line.color(180, 180, 180)
        cell = width / rows
        if rows % 2 == 0:
            line.goto(self.X_CONST, self.Y_CONST)
        else:
            line.goto(self.X_CONST, 270 - cell)
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
            self.draw_cells(width=width, rows=2, line=line)
        elif rows == 9:
            line.width(3)
            self.draw_cells(width=width, rows=3, line=line)
        line.penup()


    def draw_pantry(self, width, rows, line):
        line.width(1)
        line.goto(self.X_CONST, self.y_pantry)
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
        line.goto(self.X_CONST, self.y_pantry)
        line.pendown()
        line.width(3)
        for i in range(2):
            line.fd(width)
            line.right(90)
            line.forward(cell)
            line.right(90)
