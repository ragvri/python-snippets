
#fill width and fill lenght in pack
from tkinter import *


root=Tk()

one=Label(root,text="One", bg="white" , fg="black")  #fg: foreground color ie text color .. bg=background color
one.pack()
two=Label(root,text="Two", bg="red" , fg="yellow")
two.pack(fill=X)  # fill as wide as parent, if not specified then size depends on the text
three=Label(root,text="Three", bg="white" , fg="black")
three.pack(side=LEFT, fill=Y) #as long as parent


root.mainloop()