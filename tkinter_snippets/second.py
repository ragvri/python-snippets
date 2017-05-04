#creating buttons

from tkinter import *

root=Tk()

#frame-> invisible rectangle that we can put things in

topframe=Frame(root)
topframe.pack()                 # no need to specifty side=Top here as bottom already occupied
bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)   #tells us that we want to put the frame on bottom

button1 = Button(topframe, text="Button1", fg="red")#   where you want to put it , text on button
button2 = Button(topframe, text="Button2", fg="blue")
button3 = Button(topframe, text="Button3", fg="green")
button4 = Button(bottomframe, text="Button4", fg="purple")
#just created th button
#now pack them

# when we pack, by default , they get packed on top of each other .. so we need to specify side=LEFT
button1.pack(side=LEFT) # pack it as far left as possible
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()