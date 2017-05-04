#using grid layout and making a login page

from tkinter import *

root=Tk()

one=Label(root,text="Name")
two=Label(root,text="password")

entry1=Entry(root)   # to make an input field
entry2=Entry(root)

#organising
one.grid(row=0 , sticky=E)  #by default column =0
two.grid(row=1,sticky=E)
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

#by default everything is center aligned..so use sticky=N,E,S,W (North, east , south, west) in grid

#checkbox creating
c=Checkbutton(root, text="Keep me logged in")
#we want the checkbox to take 2 columns
c.grid(columnspan=2)


root.mainloop()