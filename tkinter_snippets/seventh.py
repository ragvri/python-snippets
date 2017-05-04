#using classes
from tkinter import *


class ragvri_method:

    def __init__(self, master):     #master parameter for gui, it refers to main window (root)
        frame=Frame(master)
        frame.pack()

        self.printButton=Button(frame, text="abcd" ,  command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton=Button(frame,text="quit",command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Wow")

root=Tk()
b=ragvri_method(root)


root.mainloop()