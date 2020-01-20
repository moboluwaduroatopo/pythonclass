from tkinter import Tk,Frame,Checkbutton,BooleanVar,BOTH
root=Tk()
def onClick():
	if var.get()==True:
		root.title("Checkbutton")
	else:
		root.title('')
var=BooleanVar()
cb=Checkbutton(root,text="Show title",variable=var,command=onClick)
cb.select()
cb.place(x=50,y=50)



root.mainloop()		
	