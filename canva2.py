from tkinter import*
import time
root=Tk("800x800")
root.geometry()
# var =IntVar()
canvas =Canvas(root, bg = "blue", height=800, width=800)
canvas.pack()
dim=5,5,60,60
ova=canvas.create_oval(dim, fill='pink')
a=10
b=20
while True: 
	# oval is an object to move and d position is a and b
	canvas.move(ova,a,b)
	# to change canvas position
	p=canvas.coords(ova)
	# p[x1,y1,x2,y2]
	if p[3]>=800 or p[1] <=0:
		b = -b
	if p[2]>=800 or p[0] <=0:
		a = -a

	root.update()
	time.sleep(0.025)
	root.title('Bouncing ball')
root.mainloop()	

