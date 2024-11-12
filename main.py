# Starting on the 4x4 🫠
from turtle import *
import draw
from block import Block

screen = Screen()
screen.bgcolor("white")
screen.setup(500, 600)
screen.title("Kids Sudoku")
screen.colormode(255)
screen.tracer(0)
pantry = []
x, y = -155, -210
for i in range(4):
    pantry.append((x,y))
    x += 100
locs = []
x, y = -155, 220
for a in range(4):
    temp = []
    for b in range(4):
        temp.append((x, y))
        x += 100
    y -= 100
    locs.append(temp)
# locs = [[(-155, 220), (-55, 220), (45, 220), (145, 220)], [(245, 120), (345, 120), (445, 120), (545, 120)],
# [(645, 20), (745, 20), (845, 20), (945, 20)], [(1045, -80), (1145, -80), (1245, -80), (1345, -80)]]
a1, a2, a3, a4 = Block(), Block(), Block(), Block()
a1.goto(pantry[0])
a2.goto(pantry[1])
a3.goto(pantry[2])
a4.goto(pantry[3])
print(locs)

draw.draw_board(400, 4)


screen.tracer(1)
while True:
    screen.update()
screen.mainloop()