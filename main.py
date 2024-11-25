# Our main game interface
import turtle
import tkinter as tk
from draw import *
from block import Block
# from tkinter import *
from tkinter import ttk
from canv import canvas, window
scr = turtle.TurtleScreen(canvas)
t = turtle.RawTurtle(scr)
scr.tracer(0)
t.speed(0)

frm = ttk.Frame(window, width=1000, height=1000, padding=10)
frm.grid(sticky='nsew')
ttk.Label(frm, text="Hello World!").grid(row=1, column=0, sticky='nsew')
ttk.Button(frm, text="Quit", command=window.destroy).grid(row=1, column=1, sticky='nsew')

draw_board(WIDTH, ROW, t)
blocks, tempblocks = [], []
colors = ["red", "orange","yellow", "green","cyan", "blue", "purple","magenta", "pink"]
for x in range(ROW):
    for y in range(ROW):
        temp = Block(WIDTH/ROW)
        temp.color(colors[x])
        temp.goto(pantry[x])
        temp.old_pos = pantry[x]
        tempblocks.append(temp)
    blocks.append(tempblocks)
scr.tracer(1)
window.mainloop()
