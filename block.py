# Also 4 x 4 some stuff I'm experimenting with
# DON'T TOUCH!!!
from turtle import *
from draw import *
from canv import canvas
class Block(RawTurtle):
    def __init__(self, cell):
        super().__init__(canvas)
        self.old_pos = None
        self.shape("square")
        size = cell/20
        self.shapesize(size)
        self.penup()
        self.moving_direction = 0
        self.ondrag(self.drag)


    def drag(self, x, y):
        # stop backtracking
        self.ondrag(None)
        self.speed(5)
        self.goto(x, y)
        self.ondrag(self.drag)
        self.onrelease(self.move_block)
    def move_block(self, x, y):
        moved = False
        in_pantry = True
        for i in range(ROW):
            for j in range(ROW):
                if cell_occupied[i][j] == self:
                    self.old_pos = locs[i][j]
                    cell = [i, j]
                    in_pantry = False
                if (-205 + j * cellsize <= self.xcor() <= -205 + (j + 1) * cellsize and
                        270 - i * cellsize >= self.ycor() >= 270 - (i + 1) * cellsize):
                    if cell_occupied[i][j] == 0:
                        self.goto(locs[i][j])
                        cell_occupied[i][j] = self
                        moved = True
        if moved:
            if not in_pantry:
                cell_occupied[cell[0]][cell[1]] = 0
        else:
            self.goto(self.old_pos)


