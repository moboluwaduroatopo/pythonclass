from tkinter import*
class Test(Frame):
	def mouseDown(self, event):
		self.lastx=event.x
		self.lasty=event.y
	def mouseMove(self, event):
		self.draw.move(CURRENT, event.x - self.lastx, event.y - self.lasty)
		self.lastx=event.x
		self.lasty=event.y
		# pass
	def mouseEnter():
		self.draw.itemconfig(CURRENT, fill='blue')

	def createWidgets(self):
		self.QUIT=Button(self, text='Quit',foreground='red',command=self.quit)
		self.QUIT.pack(side='left',fill=BOTH)
		# 5inhces
		self.draw=Canvas(self,width='5i',height='5i')
		self.draw.pack(side=LEFT)
		fred=self.draw.create_oval(0,0,20,20, fill='green', tags='selected')
		self.draw.bind(fred,"Enter",self.mouseEnter)		
		Widget.bind(self.draw,"<1>",self.mouseDown)	
		Widget.bind(self.draw,"<B1-Motion>",self.mouseMove)	
	def __init__(self, master=None):
		Frame.__init__(self,master)
		Pack.config(self)
		self.createWidgets()	
test=Test()
test.mainloop()		