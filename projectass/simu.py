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
		self.menuBar()
		self.iconbar()
		self.canvas =Canvas(self.root, bg = "blue", height=800, width=1400)
		self.canvas.pack()
		Widget.bind(self.canvas, "<ButtonPress-1>", self.mouseDown)
		Widget.bind(self.canvas, "<B1-Motion>", self.mouseMove)
		self.cord={"x":0,"y":0,"x2":0,"y2":0}
		self.lines=[]
		# self.root.resizable(0,0)
		
		self.root.mainloop()


	def mouseDown(self, event):
		# print(event)
		# self.lastx=event.x
		# self.lasty=event.y
		# print(self.lastx,self.lasty)
		self.cord['x']=event.x
		self.cord['y']=event.y
		self.line_id=self.lines.append(self.canvas.create_line(self.cord['x'],self.cord['y'],self.cord['x'],self.cord['y']))
	def mouseMove(self,event):
		# self.canvas.move(CURRENT,event.x - self.lastx, event.y - self.lasty)
		# self.lastx=event.x
		# self.lasty=event.y
		#print(self.lastx,self.lasty)	
		self.cord['x2']=event.x
		self.cord['y2']=event.y
		self.line_id=self.canvas.coords(self.lines[-1],self.cord['x'],self.cord['y'],self.cord['x2'],self.cord['y2'])
	def show_lines(self):
		pass
		# print('here')
		# def mouseDown(self,event):
		# 	print(event)
		# 	self.cord['x']=event.x
		# 	self.cord['y']=event.y
		# 	self.line_id=self.lines.append(self.canvas.create_line(self.cord['x'],self.cord['y'],self.cord['x'],self.cord['y']))
		# def mouseMove(self,event):
		# 	self.cord['x2']=event.x
		# 	self.cord['y2']=event.y
		# 	self.line_id=self.canvas.coords(self.lines[-1],self.cord['x'],self.cord['y'],self.cord['x2'],self.cord['y2'])		

	def iconbar(self):
		self.iconFrame = Frame(self.root)
		self.iconFrame.pack(side=TOP,anchor="w")
		self.newbl=Image.open('image/Bulb.png')
		self.newbulb=ImageTk.PhotoImage(self.newbl,self.root)
		Button(self.iconFrame,image=self.newbulb,padx=8,bd=5,command=self.show_bulb).grid(row=1)
		self.newlin=Image.open('image/Horizontal Line.png')
		self.newline=ImageTk.PhotoImage(self.newlin,self.root)
		Button(self.iconFrame,image=self.newline,padx=8,bd=5,command=self.show_line).grid(row=1,column=2)
		self.lin=Image.open('image/Line.png')
		self.line=ImageTk.PhotoImage(self.lin,self.root)
		Button(self.iconFrame,image=self.line,padx=8,bd=5,command=self.show_lines).grid(row=1,column=3)
		# Button(self.iconFrame,command=).grid(row=1,column=3)

	def menuBar(self):
		# loadn=Image.open('image/1.png')
		# rendern=ImageTk.PhotoImage(loadn,master=self.root)
		self.menubar=Menu(self.root)
		self.fileMenu=Menu(self.menubar,tearoff=0)
		self.newPag=Image.open('image/Bulb.png')
		self.newPagei=ImageTk.PhotoImage(self.newPag,self.root)
		self.fileMenu.add_command(image=self.newPagei,label='new page',command=self.newPage,)
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
		# self.text.bind("<Control-Key-n>",self.newPage)
		# self.text.bind("<Control-Key-N>",self.newPage)
		self.menubar.add_cascade(label='file',menu=self.fileMenu,underline=0)

		self.editmenu = Menu(self.menubar, tearoff=0)
		self.editmenu.add_command(label="Undo", command=self.donothing)

		self.editmenu.add_separator()

		self.editmenu.add_command(label="Cut", command=self.cut)
		self.editmenu.add_command(label="Copy", command=self.copy)
		self.editmenu.add_command(label="Paste", command=self.paste)
		self.editmenu.add_command(label="Delete", command=self.delete)
		self.editmenu.add_command(label="Select All", command=self.donothing)
		self.menubar.add_cascade(label="Edit", menu=self.editmenu, command=self.quitApplication)

		self.helpmenu = Menu(self.menubar, tearoff=0)
		self.helpmenu.add_command(label="Help Index", command=self.donothing)
		self.helpmenu.add_command(label="About...", command=self.showAbout)
		self.menubar.add_cascade(label="Help", menu=self.helpmenu, command=self.donothing)
	
		self.root.config(menu=self.menubar)


	def show_line(self):
		line=self.canvas.create_line(50,50,200,50,fill="red")
	def show_bulb(self):
		line=self.canvas.create_image(50,50,image=self.newbulb)
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