from tkinter import *
from PIL import Image, ImageTk
import time

root=Tk()
canvas =Canvas(root, bg = "blue", height=250, width=300)
canvas.pack()

dim=10,50,100,200
# arc=canvas.create_arc(dim,start=0,extent=150,fill='green')
arc=canvas.create_rectangle(dim,fill='green')
line=canvas.create_line(10,10,100,100,fill="red")
# loadn=Image.open('image/pic.png')
# rendern=ImageTk.PhotoImage(loadn,master=root)
# img=canvas.create_image(50,50,image=rendern)
# for x in range(1,100):
# 	canvas.move(img,5,1)
# 	root.update
	# time.sleep(5)
	# time.sleep( 5 )
root.mainloop()