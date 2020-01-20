#from tkinter import *

#Import os library
import os
#import everything from tkinter
from tkinter import *
#To get the space above the message
from tkinter.messagebox import *
#To get the dialog box to open when required
from tkinter.filedialog import *
import tkinter.ttk as ttk

# from tkinter import *

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
def selectAll():
   try:
      TextArea.tag_add(SEL,'1.0',END)
      TextArea.mark_set(INSERT,'1.0')
      TextArea.see(INSERT)
      return 'break'
   except:
      showinfo("message","Nothing to Select")
def newFile():
   root.title("Untitled Notepad")
   file=None
   asked=askyesnocancel("warning","Do you want to save this page?")
   if asked==True:
      if file==None:
         files = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
   # file = None
         TextArea.delete(1.0,END)
      elif asked==False:
         TextArea.delete(1.0,END)
def openFile():
      file = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
      if file == "":
         # no file to open
         file = None
      else:
         # Try to open the file
         # set the window title
         root.title(os.path.basename(file) + " - Notepad")
         TextArea.delete(1.0,END)
         file = open(file,"r")
         TextArea.insert(1.0,file.read())
         file.close()
def saveFile():
	files=None
	if files == None:
         # Save as new file
		files = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
		if files == "":
				files = None
		else:
         # Try to save the file
				file = open(files,"w")
				file.write(TextArea.get(1.0,END))
				file.close()
         # Change the window title
				root.title(os.path.basename(files) + " - Notepad")
	else:
				file = open(files,"w")
				file.write(TextArea.get(1.0,END))
				file.close()
def cut():
		TextArea.event_generate("<<Cut>>")
def copy():
		TextArea.event_generate("<<Copy>>")
def paste():
		TextArea.event_generate("<<Paste>>")
def delete():
	TextArea.event_generate("<<remove>>")

def quitApplication():
		root.destroy()
      # exit()
def showAbout():
		showinfo("About Notepad","Simple text editor like notepad using Python")
# def showCommand():
# 		showinfo("Notepad", "Just Another TextPad \n Copyright \n with BSD license you can use it'")
def saveasFile():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
 # def ConvertCase(): 
 # case=TextArea.event_generate("<<Copy>>")
 # case upper()
def find():
   def findit():
      start="1.0"
      end="end"
      start=TextArea.index(start)
      end=TextArea.index(end)
      count=IntVar()
      count=count
      TextArea.mark_set("matchStart",start)
      TextArea.mark_set("matchEnd",start)
      TextArea.mark_set("searchLimit",end)
      targetfind=findw.get()
      if targetfind:
         while True:
            where=TextArea.search(targetfind, "matchEnd","searchLimit", count=count)
            if where=="":
               break
            elif where:
               pastit=where + ('+%dc' % len(targetfind))
               TextArea.mark_set("matchStart",where)
               TextArea.mark_set("matchEnd","%s+%sc" % (where, count.get())) 
               TextArea.tag_add(SEL, where, pastit)
               TextArea.see(INSERT)
               TextArea.focus()
   TextArea.tag_remove(SEL, '1.0', END)


   def replaceit():
      bodytxt=TextArea.get(1.0,END)
      finded=findw.get()
      replacew=replace.get()
      TextArea.replace(1.0, 'end', TextArea.get(1.0, 'end').replace(finded,replacew))  
   find =Toplevel()
   find.grid_propagate(0)
   frm=Frame(find)
   frm.pack(side=TOP, pady=6)
   frm.grid_propagate(0)
   Label(frm, text="Find what? ").pack(side=LEFT,expand=YES, fill=BOTH)
   findw=Entry(frm, width=50)
   findw.focus_set()
   findw.pack(side=LEFT, expand=YES, fill=BOTH, padx=3)
   frm2=Frame(find)
   frm2.pack(side=TOP, pady=6)
   frm2.grid_propagate(0)
   Label(frm2, text="Replace with").pack(side=LEFT,expand=YES,fill=BOTH)
   replace=Entry(frm2,width=50)
   replace.pack(side=LEFT,expand=YES,fill=BOTH,padx=3)
   frm3=Frame(find)
   frm3.pack(side=TOP, padx=6)
   frm3.grid_propagate(0)
   findbtn= Button(frm3, text="Find", width=10 ,command=findit)
   findbtn.pack(side=LEFT,expand=YES,fill=BOTH, padx=3)
   replacebtn= Button(frm3, text="Replace",width=10, command=replaceit)
   replacebtn.pack(side=LEFT,expand=YES, fill=BOTH, padx=3)
def GoTo():
   global TextArea
   def findline():
      goline=gotow.get()
      TextArea.mark_set(INSERT,goline +'.0')
      TextArea.see(INSERT)
      TextArea.focus()
   go=Toplevel()
   go.grid_propagate(0)
   go.title('Go To')
   Label(go,text='Enter Line Number?').pack(side=TOP,expand=YES,fill=BOTH)
   gotow=Entry(go,width=30,text='goto')
   gotow.pack(side=TOP,padx=5,pady=3)
   Button(go,text='Go To',width=10,command=findline).pack(side=TOP,expand=YES, fill=BOTH, padx=3)

def printp(*e):
   pass
   # autostep = 0
   # TextArea.print_to_file()
def showStatus():
   if var.get()== True:
      print('here')
      StatusFrame.destroy() 
   else:
      print('no') 
      StatusFrame()     
def showfont():
   pass
   def style_select(event):
      pass
   def size_select():
      pass   
   def under_line():
      pass     

# https://www.tutorialbrain.com/css_tutorial/css_font_family_list/
   stylelist=['AcadEref','Agency FB','AIGDT','Algerian','AmdSymbols','AMGDT','Arial','Arial Rounded MT Bold','Arial narrow','Arial Black','Helvetica','Verdana', 
'Calibri','Century Gothic','Candara','Noto','Lucida Sans','']
   numlist=[8,9,10,11,12,13,14,15,16,17,18,19,20]
   fontlist=['Regular','OBLIQUE','Bold','BOLD OBLIQUE']

   font=Toplevel()
   font.title("Font")
   Label(font,text="Font:").grid(row=0,column=0,padx=10,pady=10)
   stylecomb=ttk.Combobox(font, value=stylelist)
   stylecomb.set('AcadEref')
   stylecomb.grid(row=1,column=0,columnspan=3,padx=10)
   stylecomb.bind("<<ComboboxSelected>>", style_select)

   Label(font,text="Font style:").grid(row=0,column=3)
   fontcomb=ttk.Combobox(font, value=fontlist)
   fontcomb.set('Regular')
   fontcomb.grid(row=1,column=3,columnspan=3,padx=10)
   fontcomb.bind("<<ComboboxSelected>>", size_select)

   Label(font,text="Size:").grid(row=0,column=6)
   sizecomb=ttk.Combobox(font, value=numlist)
   sizecomb.set('8')
   sizecomb.grid(row=1,column=6,columnspan=3,padx=10)
   sizecomb.bind("<<ComboboxSelected>>", size_select)

   underline =Checkbutton(font,text='Underline',command=under_line)
   underline.grid(row=2,column=0,padx=10,pady=20)

   Label(font,text="Preview Text").grid(row=2,column=3,padx=10,pady=20)
   btnok= Button(font, text="Ok",width=10, )
   btnok.grid(row=3,column=4, padx=10,pady=40)
   Label(font,text="Preview Text").grid(row=2,column=3,padx=10,pady=20)
   btncancel= Button(font, text="Cancel",width=10, )
   btncancel.grid(row=3,column=6, padx=10,pady=40)
root = Tk()
thisWidth = 500
thisHeight = 600
yscrollbar=Scrollbar(root,orient='vertical')
TextArea = Text(root,yscrollcommand=yscrollbar.set)


  # the window text
root.title("Untitled-Notepad")
 # Add controls (widget)
TextArea.grid(sticky = N + E + S + W)
 # To add scrollbar
yscrollbar.grid(row=0, column=1,sticky='ns')
yscrollbar.config(command=TextArea.yview)
# thisScrollBar = Scrollbar(TextArea)
file = None
 # Center the window
screenWidth = root.winfo_screenwidth()
screenHeight =root.winfo_screenheight()
 # For left-alling
left = (screenWidth / 2) - (thisWidth / 2)
      # For right-allign
top = (screenHeight / 2) - (thisHeight /2)
      # For top and bottom
root.geometry('%dx%d+%d+%d' % (thisWidth, thisHeight, left, top))
 # Scrollbar will adjust automatically according to the content
# thisScrollBar.config(command=TextArea.yview)
# TextArea.config(yscrollcommand=thisScrollBar.set)
      # To make the textarea auto resizable
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New File", command=newFile)
filemenu.add_command(label="Open file", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save as...", command=saveasFile)
filemenu.add_command(label="Print", command=printp, accelerator="Ctrl-p")
filemenu.add_command(label="Close", command=donothing)
# accelerator="Ctrl-p"
filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
# line=Image.open('2.png')
# line=ImageTK.PhotoImage(line)
editmenu.add_command(label="Undo", command=donothing )
editmenu.add_command(label="GoTo", command=GoTo)
editmenu.add_separator()

editmenu.add_command(label="Cut", command=cut)
editmenu.add_command(label="Copy", command=copy)
editmenu.add_command(label="Paste", command=paste)
editmenu.add_command(label="Delete", command=delete)
editmenu.add_command(label="Find", command=find)
editmenu.add_command(label="Select All", command=selectAll)

menubar.add_cascade(label="Edit", menu=editmenu, command=quitApplication)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=showAbout)
menubar.add_cascade(label="Help", menu=helpmenu, command=donothing)

formatmenu = Menu(menubar, tearoff=0)
formatmenu.add_command(label="Font",command=showfont)
# helpmenu.add_command(label="About...", command=showAbout)
menubar.add_cascade(label="format", menu=formatmenu)

var=BooleanVar()
viewmenu = Menu(menubar, tearoff=0)
viewmenu.add_checkbutton(label="Statu Bar",variable=var, command=showStatus)
# helpmenu.add_command(label="About...", command=showAbout)
menubar.add_cascade(label="view", menu=viewmenu)
# TextArea.bind("<Control-Key-n>",newFile)
# TextArea.bind("<Control-Key-N>",newFile)
# TextArea.bind("<Control-Key-o>",openFile)
# TextArea.bind("<Control-Key-O>",openFile)
# TextArea.bind("<Control-Key-s>",saveFile)
# TextArea.bind("<Control-Key-S>",saveFile)
# TextArea.bind("<Control-Key-n>",newFile)
root.bind("<Control-p>",printp)

root.config(menu=menubar)

def showsStatus():
   StatusFrame = Frame(root)
   StatusFrame.grid(row=5)
   textlabl = Label(StatusFrame, text="statubar", font=('arial', 5), bd=18)
   textlabl.grid(row=5)

showsStatus()

root.mainloop()

      # showtext=Stringbar()
      # statubar
# # https://www.sourcecodester.com/tutorials/python/12488/python-login-and-registration-form.html