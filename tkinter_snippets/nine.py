#adding toolbar and status bar to the drop down menu code
from tkinter import *

#making menu
def doNothing():
    print("Okay")

root=Tk()

menu= Menu(root)  #crete a menu , tells where we want to create a menu
root.config(menu=menu)  #tells tkinter that a is Menu , it already has knowledge of menus

submenu= Menu(menu) # this menu is going inside the main menu
#implement the drop down functionality
menu.add_cascade(label="file",menu=submenu) # button name, submenu
submenu.add_command(label="New project" , command=doNothing)
submenu.add_command(label="New", command=doNothing)
submenu.add_separator()
#create a separator for different sections
submenu.add_command(label="Exit", command=doNothing)

secondsubmenu=Menu(menu)
menu.add_cascade(label="edit",menu=secondsubmenu)
submenu.add_command(label="Redo" , command=doNothing)

#creating toolbar

toolbar=Frame(root,bg="blue")
insertbut = Button(toolbar,text="Insert image",command=doNothing)
insertbut.pack(side=LEFT,padx=2,pady=2)  # can add padding in pixels , padx in x direction, pady in y direction

printbut=Button(toolbar,text="print",command=doNothing)
printbut.pack(side=LEFT,padx=2,pady=2)
toolbar.pack(side=TOP ,fill=X) #by default tkinter always fills menu to top...so it will be below it

#creating statusbar
status=Label(root,text="preparing to do nothing",bd=1,relief=SUNKEN,anchor=W)  #bd means border around the label, relief adds an effect
status.pack(side=BOTTOM,fill=X)

root.mainloop()