# Also 4 x 4 some stuff I'm experimenting with
# DON'T TOUCH!!!
from turtle import *
class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.y = [-40, -20, 0]
        self.shape("square")
        self.shapesize(5)
        self.penup()

        self.goto(-155, 0)
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
