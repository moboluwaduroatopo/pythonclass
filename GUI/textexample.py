from tkinter import *
class TextExample():
	def __init__(self):
		self.root=Tk()
		self.root.title('Text example')
		self.displayText='this is a textexample python program'
		self.var=BooleanVar()
		self.cb=Checkbutton(self.root,text="Show title",variable=self.var,command=self.onClick)
		# self.cb.select()
		self.cb.grid(row=2,column=2)
		self.yscrollbar=Scrollbar(self.root,orient='vertical')
		self.xscrollbar=Scrollbar(self.root,orient='horizontal')
		self.text=Text(self.root,height=20,width=80,bg='sky blue',xscrollcommand=self.xscrollbar.set,yscrollcommand=self.yscrollbar.set)
		self.text.grid(row=0, column=0)
		self.xscrollbar.grid(row=1, column=0,sticky='ew')
		self.xscrollbar.config(command=self.text.yview)
		self.yscrollbar.grid(row=0, column=1,sticky='ns')
		self.yscrollbar.config(command=self.text.yview)
		self.text.insert('1.0',self.displayText,'end')
		
		# self.root.resizable(0,0)
		
		self.root.mainloop()
	
	
	def onClick(self):
		# pass
		if self.var.get()==True:
			# mytext=self.text.get(1.0,END)
			self.text.tag_add('bold1',1.0,END)
			self.text.tag_config('bold1',font=('bold'))
			# root.title("Checkbutton")
		else:
			self.text.tag_remove('bold1',1.0,END)
			# root.title('')

		

TextExample()


#npm i nodemom
# ternary opera