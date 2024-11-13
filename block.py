# Also 4 x 4 some stuff I'm experimenting with
# DON'T TOUCH!!!
from turtle import *
class Block(Turtle):
    def __init__(self,cell):
        super().__init__()
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
    def move_block(self):

        pass
