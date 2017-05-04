#simple example
from tkinter import *

root=Tk()

def leftclick(event):
    print("left clicked")

def middleclick(event):
    print("middle clicked")

def rightclick(event):
    print("right clicked")

frame=Frame(root,width=300 , height=250)  # can specify width and height
frame.bind("<Button-1>", leftclick)
frame.bind("<Button-2>", middleclick)
frame.bind("<Button-3>", rightclick)

frame.pack()

root.mainloop()