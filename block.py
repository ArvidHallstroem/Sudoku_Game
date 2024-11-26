# Also 4 x 4 some stuff I'm experimenting with
# DON'T TOUCH!!!
from turtle import *
from storage import *
class Block(RawTurtle):
    cell_occupied = []
    def __init__(self, row, width, shape, canvas):
        super().__init__(canvas)
        global cell_occupied
        pantry,self.locs,cell_occupied,self.cellsize = compute(row,width)
        self.old_pos = None
        self.shape(shape)
        self.row = row
        cell = width/row
        size = cell/20
        self.shapesize(size)
        self.penup()
        self.moving_direction = 0
        self.ondrag(self.drag)


    def drag(self, x, y):
        # stop backtracking
        self.ondrag(None)
        self.speed(4)
        self.goto(x, y)
        self.ondrag(self.drag)
        self.onrelease(self.move_block)

    def move_block(self, x, y):
        moved = False
        in_pantry = True
        for i in range(self.row):
            for j in range(self.row):
                if cell_occupied[i][j] == self:
                    self.old_pos = self.locs[i][j]
                    cell = [i, j]
                    in_pantry = False
                if (-205 + j * self.cellsize <= self.xcor() <= -205 + (j + 1) * self.cellsize and
                        270 - i * self.cellsize >= self.ycor() >= 270 - (i + 1) * self.cellsize):
                    if cell_occupied[i][j] == 0:
                        self.goto(self.locs[i][j])
                        cell_occupied[i][j] = self
                        moved = True
        if moved:
            if not in_pantry:
                cell_occupied[cell[0]][cell[1]] = 0
            return True
        self.goto(self.old_pos)


