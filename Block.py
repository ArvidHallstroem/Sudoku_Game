from turtle import *
class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.y = [-40, -20, 0]
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=1)
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
