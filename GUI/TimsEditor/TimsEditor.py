from tkinter import *
import PIL
from PIL import Image, ImageTk
from tkinter.filedialog import *
from tkinter.messagebox import *
from datetime import *
import time
import os
import sys
import win32ui

#---------------------------------------
in_path = mainBody= find= infile= " "
container = Tk()
container.title('TimsEditor')
container.wm_iconbitmap('notepad.ico')
menu = Menu(container)
container.config(menu=menu)

#-------------------------------------------------------------------
lt=Label(container, font = ('times', 12, 'bold'), bg='white')
lt.pack(side=TOP)

def screenTime():
	time2 = time.strftime("Date: " '%b %d, %Y | Time: %I:%M:%S %p')
	lt.config(text=time2)
	lt.after(5, screenTime)
screenTime()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def setStatus_keyboard(event):
    list1 = mainBody.index(INSERT).split('.')
    statusbar= "Line= "+str(mainBody.count('1.0', END, 'lines'))+ ", Cursor Position = row: "+list1[0]+", col: "+list1[1]+", word Count= "+str(len(mainBody.get('1.0', 'end-1c').split()))
    showtext.set(statusbar)

def setStatus_button(event):
    pass

def status_bar():
	print('here')
	list1 = mainBody.index(INSERT).split('.')
	statusbar = "Line= "+str(mainBody.count('1.0', END, 'lines'))+ ", Cursor Position = row: "+list1[0]+", col: "+list1[1]+", word Count= "+str(len(mainBody.get('1.0', 'end-1c').split()))
	print(statusbar)
	showtext.set(statusbar)

#---------------------------------------------------------------------------------------------------------------------------------
def open_callback():
	try:
		global bodytext, mainBody, in_path
		in_path = askopenfilename(initialfile='', defaultextension='.txt', filetypes=[('All Files','*.*'),('Text files', '*.txt*')])
		if in_path ==" ":
			in_path = None
		else:
			with open(in_path,"r") as infile:
				mainBody.delete(1.0, END)
				container.title(os.path.basename(in_path) + " TimsEditor")
				mainBody.insert(1.0, infile.read())
	except:
		showinfo(title='Error', message='No file Selected')

def sOpen(event):
	try:
		global bodytext, mainBody, in_path
		in_path = askopenfilename(initialfile='', defaultextension='.txt', filetypes=[('All Files','*.*'),('Text files', '*.txt*')])
		if in_path ==" ":
			in_path = None
		else:
			with open(in_path,"r") as infile:
				mainBody.delete(1.0, END)
				container.title(os.path.basename(in_path) + " TimsEditor")
				mainBody.insert(1.0, infile.read())
	except:
		showinfo(title='Error', message='No file Selected')

#--------------------------------------------------------------------------------------------------------------------------------------------------------
def save_callback():
	global bodytext, mainBody, in_path
	if in_path == " ":
		in_path = asksaveasfilename(initialfile='Untitled.txt ', defaultextension='.txt', filetypes=[('All Files', '*.*'),('Text Documents', '*.txt*')])
		if in_path =="":
			in_path = None
		else:
			with open(in_path,"w") as infile:
				infile.write(mainBody.get(1.0, END))
				container.title(os.path.basename(in_path) + " TimsEditor")
	else:
		with open(in_path,"w") as infile:
				infile.write(mainBody.get(1.0, END))
				container.title(os.path.basename(in_path) + " TimsEditor")

def saveShort(event):
	global bodytext, mainBody, in_path
	if in_path == " ":
		in_path = asksaveasfilename(initialfile='Untitled.txt ', defaultextension='.txt', filetypes=[('All Files', '*.*'),('Text Documents', '*.txt*')])
		if in_path =="":
			in_path = None
		else:
			with open(in_path,"w") as infile:
				infile.write(mainBody.get(1.0, END))
				container.title(os.path.basename(in_path) + " TimsEditor")
	else:
		with open(in_path,"w") as infile:
				infile.write(mainBody.get(1.0, END))
				container.title(os.path.basename(in_path) + " TimsEditor")

#---------------------------------------------------------------------------------------------------------------------------------------------------
def saveas_callback():
	global bodytext, mainBody, in_path
	in_path = asksaveasfilename(initialfile='Untitled.txt ', defaultextension='.txt', filetypes=[('All Files', '*.*'),('Text Documents', '*.txt*')])
	if in_path =="":
		in_path = None
	else:
		with open(in_path,"w") as infile:
			infile.write(mainBody.get(1.0, END))
			container.title(os.path.basename(in_path) + " TimsEditor")

#--------------------------------------------------------------------------------------------------------------------------------------------------
def quitter_function():
	answer = askquestion(title='Quit?', message='Really quit?')
	if answer=='yes':
		container.destroy()

#-------------------------------------------------------------------------
def newPage():
	confirm= askyesnocancel('warning', 'Do you want to save this page?')
	if confirm == True:
		global bodytext, mainBody, in_path
		if in_path == " ":
			in_path = asksaveasfilename(initialfile='Untitled.txt ', defaultextension='.txt', filetypes=[('All Files', '*.*'),('Text Documents', '*.txt*')])
			if in_path =="":
				in_path = None
			else:
				with open(in_path,"w") as infile:
					infile.write(mainBody.get(1.0, END))
					container.title(os.path.basename(in_path) + " TimsEditor")
		else:
			with open(in_path,"w") as infile:
				infile.write(mainBody.get(1.0, END))
				container.title(os.path.basename(in_path) + " TimsEditor")
		container.title("TimsEditor")
		filename = None
		mainBody.delete(1.0, 'end')
		in_path=" "
		
	elif confirm == False:
		container.title("TimsEditor")
		filename = None
		mainBody.delete(1.0, 'end')
		in_path=" "

	else:
		pass

	
def shortcut(event):
	confirm= askyesnocancel('warning', 'Do you want to save this page?')
	if confirm == True:
		global bodytext, mainBody, in_path
		if in_path == " ":
			in_path = asksaveasfilename(initialfile='Untitled.txt ', defaultextension='.txt', filetypes=[('All Files', '*.*'),('Text Documents', '*.txt*')])
			if in_path =="":
				in_path = None
			else:
				with open(in_path,"w") as infile:
					infile.write(mainBody.get(1.0, END))
					container.title(os.path.basename(in_path) + " TimsEditor")
		else:
			with open(in_path,"w") as infile:
				infile.write(mainBody.get(1.0, END))
				container.title(os.path.basename(in_path) + " TimsEditor")
		container.title("TimsEditor")
		filename = None
		mainBody.delete(1.0, 'end')
		in_path=" "
		
	elif confirm == False:
		container.title("TimsEditor")
		filename = None
		mainBody.delete(1.0, 'end')
		in_path=" "

	else:
		pass

#-----------------------------------------
def select_all():
	mainBody.tag_add(SEL, '1.0', END)
	mainBody.mark_set(INSERT, '1.0')
	mainBody.see(INSERT)

def shortSelect(event):
	mainBody.tag_add(SEL, '1.0', END)
	mainBody.mark_set(INSERT, '1.0')
	mainBody.see(INSERT)

#------------------------------------------------------------------
def cut():
	try:
		mainBody.event_generate("<<Cut>>")
	except:
		showinfo(title='Error', message='There is nothing to Cut')

def sCut(event):
	try:
		mainBody.event_generate("<<Cut>>")
	except:
		showinfo(title='Error', message='There is nothing to Cut')

def copy():
	try:
		mainBody.event_generate("<<Copy>>")

	except:
		showinfo(title='Error', message='There is nothing to Copy')

def sCopy(event):
	try:
		mainBody.event_generate("<<Copy>>")

	except:
		showinfo(title='Error', message='There is nothing to Copy')

def paste():
	try:
		mainBody.event_generate("<<Paste>>")
	except:
		showinfo(title='Error', message='There is nothing to Paste')

def sPaste(event):
	try:
		mainBody.event_generate("<<Paste>>")
	except:
		showinfo(title='Error', message='There is nothing to Paste')

def undo():
	try:
		mainBody.edit_undo()

	except:
		showinfo(title='Error', message='There is nothing to Undo')

def sUndo(event):
	try:
		mainBody.edit_undo()

	except:
		showinfo(title='Error', message='There is nothing to Undo')

def redo():
	try:
		mainBody.edit_redo()
	except:
		showinfo(title='Error', message='There is nothing to Redo')

def sRedo(event):
	try:
		mainBody.edit_redo()
	except:
		showinfo(title='Error', message='There is nothing to Redo')

#--------------------------------------------------------------------------------------
def delete():
	try:
		mainBody.delete(SEL_FIRST, SEL_LAST)
	except:
		showinfo(title='Error', message='Nothing to delete, select content to delete')

def sDelete(event):
	try:
		mainBody.delete(SEL_FIRST, SEL_LAST)
	except:
		showinfo(title='Error', message='Nothing to delete, select content to delete')


#-----------------------------------------------------------------------------------
def bold():
	global mainBody
	try:
		if bd.get()==True:
			mainBody.tag_add('bold1', SEL_FIRST, SEL_LAST)
			mainBody.tag_config('bold1', font=('bold'))
		else:
			mainBody.tag_remove('bold1', SEL_FIRST, SEL_LAST)
	except:
		showinfo(title='Error', message='Nothing to Bold, select content to Bold')

def sBold(event):
	global mainBody
	try:
		if bd.get()==True:
			mainBody.tag_add('bold1', SEL_FIRST, SEL_LAST)
			mainBody.tag_config('bold1', font=('bold'))
		else:
			mainBody.tag_remove('bold1', SEL_FIRST, SEL_LAST)
	except:
		showinfo(title='Error', message='Nothing to Bold, select content to Bold')


def italic():
	global mainBody
	try:
		if itl.get()==True:
			mainBody.tag_add('italic1', SEL_FIRST, SEL_LAST)
			mainBody.tag_config('italic1', font=('italic'))
		else:
			mainBody.tag_remove('italic1', SEL_FIRST, SEL_LAST)
	except:
		showinfo(title='Error', message='Nothing to Italize, select content to Italize')

def sItalic(event):
	global mainBody
	try:
		if itl.get()==True:
			mainBody.tag_add('italic1', SEL_FIRST, SEL_LAST)
			mainBody.tag_config('italic1', font=('italic'))
		else:
			mainBody.tag_remove('italic1', SEL_FIRST, SEL_LAST)
	except:
		showinfo(title='Error', message='Nothing to Italize, select content to Italize')

def underline():
	try:
		if udl.get()==True:
			mainBody.tag_add('Underline1', SEL_FIRST, SEL_LAST)
			mainBody.tag_config('Underline1', underline=True)
		else:
			mainBody.tag_remove('Underline1', SEL_FIRST, SEL_LAST)
	except:
		showinfo(title='Error', message='Nothing to Underline, select content to Underline')

#---------------------------------------------------------------------------------------------
def find():
	global find
	def findIt():
		start = '1.0'
		end = 'end'
		start = mainBody.index(start)
		end = mainBody.index(end)
		count = IntVar()
		count = count
		mainBody.mark_set('matchStart', start)
		mainBody.mark_set('matchEnd', start)
		mainBody.mark_set('searchLimit', end)
		targetfind = findw.get()

		if targetfind:
			while True: 
				where = mainBody.search(targetfind, 'matchEnd', 'searchLimit', count=count)
				if where == "":
					break
				elif where:
					pastit = where + ('+%dc' % len(targetfind))
					mainBody.mark_set('matchStart', where)
					mainBody.mark_set('matchEnd', '%s+%sc' % (where, count.get()))
					mainBody.tag_add(SEL, where, pastit)
					mainBody.see(INSERT)
					mainBody.focus()
		find.destroy()
	mainBody.tag_remove(SEL, '1.0', END)

	find = Toplevel()
	find.wm_iconbitmap('notepad.ico')
	find.grid_propagate(0)
	frm = Frame(find)
	frm.pack(side=TOP, pady=6)
	frm.grid_propagate(0)
	Label(frm, text="Find what?  ").pack(side=LEFT)
	findw = Entry(frm, width=50)
	findw.focus_set()
	findw.pack(side=LEFT)
	frm3 = Frame(find)
	frm3.pack(side=TOP, pady=6)
	frm3.grid_propagate(0)
	Button(frm3, text="Find", width=10, command=findIt).pack(side=LEFT, expand= YES, fill=BOTH, padx=3)

def sFind(event):
	global find
	def findIt():
		start = '1.0'
		end = 'end'
		start = mainBody.index(start)
		end = mainBody.index(end)
		count = IntVar()
		count = count
		mainBody.mark_set('matchStart', start)
		mainBody.mark_set('matchEnd', start)
		mainBody.mark_set('searchLimit', end)
		targetfind = findw.get()

		if targetfind:
			while True: 
				where = mainBody.search(targetfind, 'matchEnd', 'searchLimit', count=count)
				if where == "":
					break
				elif where:
					pastit = where + ('+%dc' % len(targetfind))
					mainBody.mark_set('matchStart', where)
					mainBody.mark_set('matchEnd', '%s+%sc' % (where, count.get()))
					mainBody.tag_add(SEL, where, pastit)
					mainBody.see(INSERT)
					mainBody.focus()
		find.destroy()
	mainBody.tag_remove(SEL, '1.0', END)

	find = Toplevel()
	find.wm_iconbitmap('notepad.ico')
	find.grid_propagate(0)
	frm = Frame(find)
	frm.pack(side=TOP, pady=6)
	frm.grid_propagate(0)
	Label(frm, text="Find what?  ").pack(side=LEFT)
	findw = Entry(frm, width=50)
	findw.focus_set()
	findw.pack(side=LEFT)
	frm3 = Frame(find)
	frm3.pack(side=TOP, pady=6)
	frm3.grid_propagate(0)
	Button(frm3, text="Find", width=10, command=findIt).pack(side=LEFT, expand= YES, fill=BOTH, padx=3)

#--------------------------------------------------------------------------------------------------------
def replace():
	def findIt():
		start = '1.0'
		end = 'end'
		start = mainBody.index(start)
		end = mainBody.index(end)
		count = IntVar()
		count = count
		mainBody.mark_set('matchStart', start)
		mainBody.mark_set('matchEnd', start)
		mainBody.mark_set('searchLimit', end)
		targetfind = findw.get()

		if targetfind:
			while True: 
				where = mainBody.search(targetfind, 'matchEnd', 'searchLimit', count=count)
				if where == "":
					break
				elif where:
					pastit = where + ('+%dc' % len(targetfind))
					mainBody.mark_set('matchStart', where)
					mainBody.mark_set('matchEnd', '%s+%sc' % (where, count.get()))
					mainBody.tag_add(SEL, where, pastit)
					mainBody.see(INSERT)
					mainBody.focus()
	mainBody.tag_remove(SEL, '1.0', END)

	def replaceIt():
		bodytxt=mainBody.get(1.0, END)
		finded = findw.get()
		replacew = replace.get()
		mainBody.replace(1.0, 'end', mainBody.get(1.0, 'end').replace(finded, replacew))

	find = Toplevel()
	find.wm_iconbitmap('notepad.ico')
	find.grid_propagate(0)
	frm = Frame(find)
	frm.pack(side=TOP, pady=6)
	frm.grid_propagate(0)
	Label(frm, text="Find what?  ").pack(side=LEFT)
	findw = Entry(frm, width=50)
	findw.focus_set()
	findw.pack(side=LEFT)
	frm2 = Frame(find)
	frm2.pack(side=TOP, pady=6)
	frm2.grid_propagate(0)
	Label(frm2, text="Replace With? ").pack(side=LEFT, expand=YES, fill=BOTH)
	replace = Entry(frm2, width=50)
	replace.pack(side=LEFT, expand= YES, fill=BOTH, padx=3)
	frm3 = Frame(find)
	frm3.pack(side=TOP, pady=6)
	frm3.grid_propagate(0)
	Button(frm3, text="Replace", width=10, command=replaceIt).pack(side=LEFT, expand= YES, fill=BOTH, padx=3)

def sReplace(event):
	def findIt():
		start = '1.0'
		end = 'end'
		start = mainBody.index(start)
		end = mainBody.index(end)
		count = IntVar()
		count = count
		mainBody.mark_set('matchStart', start)
		mainBody.mark_set('matchEnd', start)
		mainBody.mark_set('searchLimit', end)
		targetfind = findw.get()

		if targetfind:
			while True: 
				where = mainBody.search(targetfind, 'matchEnd', 'searchLimit', count=count)
				if where == "":
					break
				elif where:
					pastit = where + ('+%dc' % len(targetfind))
					mainBody.mark_set('matchStart', where)
					mainBody.mark_set('matchEnd', '%s+%sc' % (where, count.get()))
					mainBody.tag_add(SEL, where, pastit)
					mainBody.see(INSERT)
					mainBody.focus()
	mainBody.tag_remove(SEL, '1.0', END)

	def replaceIt():
		bodytxt=mainBody.get(1.0, END)
		finded = findw.get()
		replacew = replace.get()
		mainBody.replace(1.0, 'end', mainBody.get(1.0, 'end').replace(finded, replacew))

	find = Toplevel()
	find.wm_iconbitmap('notepad.ico')
	find.grid_propagate(0)
	frm = Frame(find)
	frm.pack(side=TOP, pady=6)
	frm.grid_propagate(0)
	Label(frm, text="Find what?  ").pack(side=LEFT)
	findw = Entry(frm, width=50)
	findw.focus_set()
	findw.pack(side=LEFT)
	frm2 = Frame(find)
	frm2.pack(side=TOP, pady=6)
	frm2.grid_propagate(0)
	Label(frm2, text="Replace With? ").pack(side=LEFT, expand=YES, fill=BOTH)
	replace = Entry(frm2, width=50)
	replace.pack(side=LEFT, expand= YES, fill=BOTH, padx=3)
	frm3 = Frame(find)
	frm3.pack(side=TOP, pady=6)
	frm3.grid_propagate(0)
	Button(frm3, text="Replace", width=10, command=replaceIt).pack(side=LEFT, expand= YES, fill=BOTH, padx=3)

#---------------------------------------------------------------------------------------------------------------
def styly(style):
	mainBody.tag_add('style1', SEL_FIRST, SEL_LAST)
	mainBody.tag_config('style1', font=('stlye'))
	#mainBody.tag_remove('style1', SEL_FIRST, SEL_LAST)


def ConvertCase():
	pass
	# case = mainBody.event_generate("<<Copy>>")
	# mainBody.tag_add('case', SEL_FIRST, SEL_LAST)
	# mainBody.config('case', mainBody.upper())

def reset():
	mainBody.edit_reset

def seperator():
	mainBody.edit_separator

def modified():
	mainBody.edit_modified

def pageSettings():
	pass

#-----------------------------------------------------------------
def printing():
	global in_path, infile
	with open(in_path, 'r') as infile:
		textfile = infile.read()
	pf = win32ui.CreateDC()
	pf.CreatePrinterDC()
	pf.SetMapMode(4)
	font = win32ui.CreateFont({'name': 'Arial', 'height':16})
	pf.SelectObject(font)
	pf.StartDoc(textfile)
	pf.TextOut(40,40, textfile)
	pf.EndPage()
	pf.EndDoc()
	print(textfile)
	
#---------------------------------------------------------------------------------------------------------------
def dateTime():
	d = datetime (1,1,1).now()
	showinfo(title='Date & Time', message= d.strftime("Date: " '%b %d, %Y | Time: %I:%M %p'))

def sDT(event):
	d = datetime (1,1,1).now()
	showinfo(title='Date & Time', message= d.strftime("Date: " '%b %d, %Y | Time: %I:%M %p'))

def about():
	showinfo(title='info', message= 'TimsEditor is a writing pad for all, developed by Timsworld @ SQI OGBOMOSO')

#-------------------------------------------------------------------------------------------------------------
load = PIL.Image.open('new.png')
render = ImageTk.PhotoImage(load, master = container)
load1 = PIL.Image.open('open.png')
render1 = ImageTk.PhotoImage(load1, master = container)
load2 = PIL.Image.open('save.png')
render2 = ImageTk.PhotoImage(load2, master = container)
load3 = PIL.Image.open('print.png')
render3 = ImageTk.PhotoImage(load3, master = container)
load4 = PIL.Image.open('undo.png')
render4 = ImageTk.PhotoImage(load4, master = container)
load5 = PIL.Image.open('redo.png')
render5 = ImageTk.PhotoImage(load5, master = container)
load6 = PIL.Image.open('cut.png')
render6 = ImageTk.PhotoImage(load6, master = container)
load7 = PIL.Image.open('copy.png')
render7 = ImageTk.PhotoImage(load7, master = container)
load8 = PIL.Image.open('paste.png')
render8 = ImageTk.PhotoImage(load8, master = container)
load9 = PIL.Image.open('delete.png')
render9 = ImageTk.PhotoImage(load9, master = container)
load10 = PIL.Image.open('saveas.png')
render10 = ImageTk.PhotoImage(load10, master = container)
load11 = PIL.Image.open('exit.png')
render11 = ImageTk.PhotoImage(load11, master = container)
load12 = PIL.Image.open('pagesetup.png')
render12 = ImageTk.PhotoImage(load12, master = container)
load13 = PIL.Image.open('help.png')
render13 = ImageTk.PhotoImage(load13, master = container)
load13a = PIL.Image.open('about.png')
render13a = ImageTk.PhotoImage(load13a, master = container)
load14 = PIL.Image.open('find.png')
render14 = ImageTk.PhotoImage(load14, master = container)
load15 = PIL.Image.open('replace.png')
render15 = ImageTk.PhotoImage(load15, master = container)
load16 = PIL.Image.open('goto.png')
render16 = ImageTk.PhotoImage(load16, master = container)
load17 = PIL.Image.open('selectall.png')
render17 = ImageTk.PhotoImage(load17, master = container)
load18 = PIL.Image.open('timeanddate.png')
render18 = ImageTk.PhotoImage(load18, master = container)
load19 = PIL.Image.open('bold.png')
render19 = ImageTk.PhotoImage(load19, master = container)
load20 = PIL.Image.open('italic.png')
render20 = ImageTk.PhotoImage(load20, master = container)
load21 = PIL.Image.open('underline.png')
render21 = ImageTk.PhotoImage(load21, master = container)


#---------------------------------------------------------
bodyfrm = Frame(container)
bodyfrm.pack(side=TOP, expand=YES, fill=BOTH)
bodyfrm.grid_propagate(0)

#--------------------------------------------------------------------------------------------
mainBody= Text(bodyfrm, height=35, width=125, font= ('Times New Roman', 12), bg = 'sky blue')
mainBody.focus_set()
mainBody.pack(side=LEFT, expand=YES, fill=BOTH)
scroll = Scrollbar(bodyfrm, orient = "vertical", command = mainBody.yview)
scroll.pack(side=LEFT, anchor=E, fill=BOTH)
mainBody.configure(yscrollcommand = scroll.set)
mainBody.bind("<KeyPress>", setStatus_keyboard)
mainBody.bind("<ButtonPress-1>", setStatus_button)
mainBody.bind("<Control-Key-o>", sOpen)
mainBody.bind("<Control-Key-O>", sOpen)
mainBody.bind("<Control-Key-n>", shortcut)
mainBody.bind("<Control-Key-N>", shortcut)


mainBody.bind("<Control-Key-a>", shortSelect)
mainBody.bind("<Control-Key-A>", shortSelect)
mainBody.bind("<Control-Key-s>", saveShort)
mainBody.bind("<Control-Key-S>", saveShort)
mainBody.bind("<Control-Key-x>", sCut)
mainBody.bind("<Control-Key-X>", sCut)
mainBody.bind("<Control-Key-c>", sCopy)
mainBody.bind("<Control-Key-C>", sCopy)
# mainBody.bind("<Control-Key-v>", sPaste)
# mainBody.bind("<Control-Key-V>", sPaste)
mainBody.bind("<Control-Key-z>", sUndo)
mainBody.bind("<Control-Key-Z>", sUndo)
mainBody.bind("<Control-Key-y>", sRedo)
mainBody.bind("<Control-Key-Y>", sRedo)
mainBody.bind("<Key-Delete>", sDelete)
mainBody.bind("<Key-F5>", sDT)
mainBody.bind("<Control-Key-b>", sBold)
mainBody.bind("<Control-Key-B>", sBold)
mainBody.bind("<Control-Key-i>", sItalic)
mainBody.bind("<Control-Key-I>", sItalic)
mainBody.bind("<Control-Key-f>", sFind)
mainBody.bind("<Control-Key-F>", sFind)
mainBody.bind("<Control-Key-h>", sReplace)
mainBody.bind("<Control-Key-H>", sReplace)

#------------------------------------------------------------------------ 
showtext = StringVar()
statusbarfrm = Frame(container)
statusbarfrm.pack(side=TOP, expand=YES, fill=BOTH, anchor=W)
statusbarfrm.grid_propagate(0)
linecount = Label(statusbarfrm, text='showtext').pack(side=LEFT)

#------------------------------------------------------------------------------------------------------------------------
file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label='New', command=newPage, accelerator = 'Ctrl + N', image= render, compound='left')
file_menu.add_command(label='Open...', command=open_callback, accelerator = 'Ctrl + O', image= render1, compound='left')
file_menu.add_command(label='Save', command=save_callback, accelerator = 'Ctrl + S', image= render2, compound='left')
file_menu.add_command(label='Save As...', command=saveas_callback, image= render10, compound='left')
file_menu.add_separator()
file_menu.add_command(label='Page Set-Up', command=pageSettings, image=render12, compound='left')
file_menu.add_command(label='Print...', accelerator = 'Ctrl + P', command=printing, image= render3, compound='left')
file_menu.add_command(label='Exit', command=quitter_function, image = render11, compound='left')
menu.add_cascade(label='File', menu=file_menu)

#--------------------------------------------------------------------------------------------------------------
file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label='Undo', command=undo, accelerator = 'Ctrl + Z', image= render4, compound="left")
file_menu.add_command(label='Redo', command=redo, accelerator = 'Ctrl + Y', image= render5, compound='left')
file_menu.add_separator()
file_menu.add_command(label='Cut', command= cut, accelerator = 'Ctrl + X', image=render6, compound='left')
file_menu.add_command(label='Copy', command= copy, accelerator = 'Ctrl + C', image= render7, compound='left')
file_menu.add_command(label='Paste', command= paste, accelerator = 'Ctrl + V', image= render8, compound='left')
file_menu.add_command(label='Delete', command= delete, accelerator = 'Del', image= render9, compound='left')
file_menu.add_separator()
file_menu.add_command(label='Find', command=find, accelerator = 'Ctrl + F', image=render14, compound='left')
#file_menu.add_command(label='Find Next', accelerator = 'F3')
file_menu.add_command(label='Replace', command=replace, accelerator = 'Ctrl + H', image=render15, compound='left')
file_menu.add_command(label='Go To...', accelerator = 'Ctrl + G', image=render16, compound='left')
file_menu.add_command(label='Select All', command=select_all, accelerator = 'Ctrl + A', image=render17, compound='left')
file_menu.add_command(label='Time/Date', command = dateTime, accelerator = 'F5', image=render18, compound='left')
menu.add_cascade(label='Edit', menu=file_menu)

#---------------------------------------------------------------------------------------------------------------------------
file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label='Word Wrap',)
file_menu.add_command(label='Font..',)
bd = BooleanVar()
file_menu.add_checkbutton(label='Bold', variable=bd, command= bold, accelerator = 'Ctrl + B', image=render19, compound='left')
itl = BooleanVar()
file_menu.add_checkbutton(label='Italic', variable=itl, command= italic, accelerator = 'Ctrl + I', image=render20, compound='left')
udl = BooleanVar()
file_menu.add_checkbutton(label='Underline', variable=udl, command=underline, accelerator = 'Ctrl + U', image=render21, compound='left')
menu.add_cascade(label='Format', menu=file_menu)

#---------------------------------------------------------------
file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label='Status Bar', command = status_bar)
menu.add_cascade(label='View', menu=file_menu)

#---------------------------------------------------------------
file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label='View Help', image=render13a, compound='left')
file_menu.add_command(label='About', command=about, image=render13, compound='left')
menu.add_cascade(label='Help', menu=file_menu)

#--------------------
container.mainloop()