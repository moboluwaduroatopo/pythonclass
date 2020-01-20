from tkinter import *
root=Tk()
root.title('Text example')
fm=Frame(root)
fm.pack(side=TOP, expand=YES, fill=BOTH)
fm.grid_propagate(0)
# displayText='this is a textexample python program'
congroup=BooleanVar()
val1=congroup.get()

Radiobutton(fm, variable=congroup, text='A', value='a').pack()
Radiobutton(fm, variable=congroup, text='B', value='b').pack()
Radiobutton(fm, variable=congroup, text='C', value='c').pack()
Radiobutton(fm, variable=congroup, text='D', value='d').pack()
root.mainloop()