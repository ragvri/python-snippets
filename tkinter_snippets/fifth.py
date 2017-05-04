#how to bind functions to a widget

from tkinter import *

root=Tk()

def printName():
    print("hello my namme is raghav")

button1=Button(root, text="print name" , command= printName())  # command tells what function to call when it is pressed
button1.pack()


#another way to do the same thing
def printName(event):  # will execute only after an event occurs
    print("Hello")
button1=Button(root, text="print name" , command= printName())
button1.bind("<Button-1>", printName())  #<Button-1> is event for left clicking on mouse
button1.pack()




root.mainloop()