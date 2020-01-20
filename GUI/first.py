from tkinter import *
class Gui():
	def __init__(self):
		self.root=Tk()
		self.root.title('GUI example')
		self.lb= StringVar()
		self.lb.set('first example')
		Label(self.root, textvariable=self.lb).pack(side=LEFT)
		self.but=Button(self.root,text='show text', command=self.show)
		self.but.pack(side=LEFT)
		self.entry=Entry(self.root)
		self.entry.pack(side='left')
		self.state = True
		self.root.mainloop()
	def show(self):
	# global state
		if self.state:
			self.lb.set('new text to display')
			self.state=False
		else:
			self.lb.set('second new text to display')
			self.state=True
# fm =Frame(root, height=400, width=300, bg='green')
# fm.pack()
# lb= StringVar()
# lb.set('first example')
# Label(root, textvariable=lb).pack(side=LEFT)

# # Label(fm,text='first example').pack(side=LEFT)
# but=Button(root,text='show text', command=show)
# but.pack(side=LEFT)

# cont= Frame(fm,height=500, width=400,bg='blue')
# cont.pack()

app=Gui()


#npm i nodemom
# ternary operator