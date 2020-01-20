from tkinter import *

from PIL import Image, ImageTk
# import PIL
class TextExample():
	def __init__(self):
		self.root=Tk()
		self.root.title('Text example')
		self.displayText='this is a textexample python program'
		self.var=BooleanVar()
		self.bold=BooleanVar()
		# self.cb=Checkbutton(self.root,text="Show title",variable=self.var,command=self.onClick)
		# self.cb.select()
		# self.cb.grid(row=2,column=2)
		self.yscrollbar=Scrollbar(self.root,orient='vertical')
		self.xscrollbar=Scrollbar(self.root,orient='horizontal')
		self.text=Text(self.root,height=20,width=80,bg='sky blue',xscrollcommand=self.xscrollbar.set,yscrollcommand=self.yscrollbar.set)
		self.text.grid(row=0, column=0)
		self.xscrollbar.grid(row=1, column=0,sticky='ew')
		self.xscrollbar.config(command=self.text.yview)
		self.yscrollbar.grid(row=0, column=1,sticky='ns')
		self.yscrollbar.config(command=self.text.yview)
		self.text.insert('1.0',self.displayText,'end')
		self.menuBar()
		# self.root.resizable(0,0)
		self.listfm=Frame(self.root)
		self.listfm.grid(row=3, column=0,sticky='ew')
		self.lbox=Listbox(self.listfm,selectmode='extended')
		# selectmode='multiple'
		self.lbox.insert(1,'red')
		self.lbox.insert(2,'yellow')
		self.lbox.insert(3,'green')
		self.lbox.insert(4,'blue')
		self.lbox.insert(5,'black')
		self.lbox.grid(row=4, column=0,)
		self.lbox.bind("<<ListboxSelect>>",lambda event:self.onClick())
		self.root.mainloop()
	def onClick(self):
		select=self.lbox.curselection()
		print(select)
		# if(select==1):
		# 	print
	def menuBar(self):
		# loadn=Image.open('image/1.png')
		# rendern=ImageTk.PhotoImage(loadn,master=self.root)
		self.menubar=Menu(self.root)
		self.fileMenu=Menu(self.menubar,tearoff=0)
		self.fileMenu.add_command(label='new page',command=self.newPage, accelerator="ctrl+N")
		self.fileMenu.add_command(label='open',command=self.openfile)
		self.fileMenu.add_command(label="Save", command=self.saveFile)
		self.fileMenu.add_command(label="Save as...", command=self.saveasFile)
		self.fileMenu.add_command(label="Close", command=self.donothing)

		self.fileMenu.add_checkbutton(label='Bold',variable=self.bold,command=self.onClick)

		self.option=Menu(self.fileMenu,tearoff=0)
		self.option.add_command(label='option',command=self.openfile)
		self.option.add_command(label='option1',command=self.openfile)
		self.option.add_command(label='option2',command=self.openfile)
		self.fileMenu.add_cascade(label='option',menu=self.option,underline=0)
		self.text.bind("<Control-Key-n>",self.newPage)
		self.text.bind("<Control-Key-N>",self.newPage)
		self.menubar.add_cascade(label='file',menu=self.fileMenu,underline=0)

		
		self.root.config(menu=self.menubar)

	def showAbout(self):
		pass
	def cut(self):
		pass
	def copy(self):
		pass
	def paste(self):
		pass
	def delete(self):
		pass	
	def quitApplication(self):
		pass				
	def donothing(self):
		pass
	def saveasFile(self):
		pass
	def saveFile(self):
		pass
		# add_checkButton()
	def newPage(self):
		pass
	def openfile(self):
		pass	
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