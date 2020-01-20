from tkinter import *
from PIL import Image, ImageTk
import time

root=Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New File", )
filemenu.add_command(label="Open file",)
filemenu.add_command(label="Save", )
filemenu.add_command(label="Save as...", )
filemenu.add_command(label="Print", )
filemenu.add_command(label="Close",)
# accelerator="Ctrl-p"
filemenu.add_separator()

filemenu.add_command(label="Exit", )
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
# line=Image.open('2.png')
# line=ImageTK.PhotoImage(line)
editmenu.add_command(label="Undo" )
editmenu.add_command(label="GoTo")
editmenu.add_separator()

editmenu.add_command(label="Cut", )
editmenu.add_command(label="Copy", )
editmenu.add_command(label="Paste", )
editmenu.add_command(label="Delete", )
editmenu.add_command(label="Find", )
editmenu.add_command(label="Select All", )

menubar.add_cascade(label="Edit", menu=editmenu, )
root.config(menu=menubar)

Button(root,padx=16,bd=8,fg='black',font=('arial',13,'bold'),text="1",bg="powder blue",command=lambda:self.operateSqroot('√')).pack(side=TOP,anchor="w")
Button(root,padx=16,bd=8,fg='black',font=('arial',13,'bold'),text="1",bg="powder blue",command=lambda:self.operateSqroot('√')).pack(side=TOP,)
Button(root,padx=16,bd=8,fg='black',font=('arial',13,'bold'),text="1",bg="powder blue",command=lambda:self.operateSqroot('√')).pack(side=TOP,)
Button(root,padx=16,bd=8,fg='black',font=('arial',13,'bold'),text="1",bg="powder blue",command=lambda:self.operateSqroot('√')).pack(side=TOP,)
# newbl=Image.open(image.png)
# newbulb=ImageTK.PhotoImage(newbl,root)
# Button(root,image=newbulb,command=lambda:self.operateSqroot('√'))
canvas =Canvas(root, bg = "blue", height=800, width=1400)
canvas.pack()


root.mainloop()