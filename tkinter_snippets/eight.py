#creating drop down menu
from tkinter import *

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

root.mainloop()