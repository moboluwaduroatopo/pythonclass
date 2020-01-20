from tkinter import *
class Gui():
	def __init__(self):
		self.root=Tk()
		self.root.title('GUI example')
		self.ans= StringVar()
		self.op= StringVar()
		# self.lb.set('first example')
		self.ent=Entry(self.root)
		self.ent.grid(row=0, column=0)

		self.lab=Label(self.root, textvariable=self.op)
		self.lab.grid(row=0, column=1)

		self.entry=Entry(self.root)
		self.entry.grid(row=0, column=2)

		self.lab1=Label(self.root, text='=')
		self.lab1.grid(row=0, column=3)

		self.ans1=Entry(self.root, textvariable=self.ans)
		self.ans1.grid(row=0, column=4)

		self.plus=Button(self.root,text='+',width=5, command=lambda:self.operate('+'))
		self.plus.grid(row=1, column=0)

		self.min=Button(self.root,text='-',width=5, command=lambda:self.operate('-'))
		self.min.grid(row=1, column=1)

		self.muti=Button(self.root,text='*',width=5, command=lambda:self.operate('*'))
		self.muti.grid(row=1, column=2)

		self.divi=Button(self.root,text='/',width=5, command=lambda:self.operate('/'))
		self.divi.grid(row=1, column=3)

		self.equ=Button(self.root,text='calculate',width=10, command=self.calculate)
		self.equ.grid(row=1, column=4)
		
		self.state = True
		self.ope=""
		self.val1=self.val2=0
		self.root.mainloop()
	def calculate(self):
		if self.ope == '+':
			self.ans.set(self.val1 + self.val2)
		elif(self.ope == '-'):
			self.ans.set(self.val1 - self.val2)
		elif(self.ope =='*'):
			self.ans.set(self.val1 * self.val2)
		elif(self.ope== '/'):
			self.ans.set(self.val1 / self.val2)

		
		# self.ans.set(val1 + val2)
	def operate(self,x):
		self.op.set(x)
		self.ope=x
		self.val1=float(self.ent.get())
		self.val2=float(self.entry.get())
		# self.op.set(x)
		# self.ope=x
		# self.val1=float(self.ent.get())
		# self.val2=float(self.entry.get())


Gui()


#npm i nodemom
# ternary operator