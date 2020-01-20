from tkinter import*
import time
root=Tk("800x800")
root.geometry()
# var =IntVar()
canvas =Canvas(root, bg = "blue", height=800, width=800)
canvas.pack()
dim=5,5,60,60
ova=canvas.create_oval(dim, fill='pink')
a=5
b=5
for x in range(0,100):
	canvas.move(ova,a,b)
	root.update()
	time.sleep(.001)
root.mainloop()	

