#making the first window
from tkinter import  *

root= Tk()  #creating an object named root from Tk() class. It is the main window
#text in tkinter is called label

label=Label(root, text=" I am raghav") # first arg tells where to put and second tells what to put
#tells exact location where to put label
label.pack() # tells to put the text in first blank space it finds

root.mainloop() # keeps the windows on screen in infinite loop

