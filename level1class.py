
# window.geometry("200x250") 

# top_frame = t.Frame(window).pack(side="top")
# top_frame = t.Frame(window)
# top_frame.pack(side="top")
def num(n):
	s=func.number(n)
	length=len(screen.get())
	screen.insert(length)
	#print("Hello")
import tkinter as t
window =t.Tk()
window.title("SQI Python Calculator")
screen=t.Entry(window, text="0")
screen.grid(row=0, columnspan=4,pady=3)
bnt1=t.Button(window,text="1",width=5,height=3, command=lambda:num('1'))
bnt1.grid(row=1,column=0)
btn2=t.Button(window,text="2",width=5,height=3)
btn2.grid(row=1,column=1)
bnt3=t.Button(window,text="3",width=5,height=3)
bnt3.grid(row=1,column=2)
plus=t.Button(window,text="+",width=5,height=3)
plus.grid(row=1,column=3)

bnt4=t.Button(window,text="4",width=5,height=3)
bnt4.grid(row=2,column=0)
bnt5=t.Button(window,text="5",width=5,height=3)
bnt5.grid(row=2,column=1)
bnt6=t.Button(window,text="6",width=5,height=3)
bnt6.grid(row=2,column=2)
minus=t.Button(window,text="-",width=5,height=3)
minus.grid(row=2,column=3)

bnt7=t.Button(window,text="7",width=5,height=3)
bnt7.grid(row=3,column=0)
bnt8=t.Button(window,text="8",width=5,height=3)
bnt8.grid(row=3,column=1)
bnt9=t.Button(window,text="9",width=5,height=3)
bnt9.grid(row=3,column=2)
multi=t.Button(window,text="*",width=5,height=3)
multi.grid(row=3,column=3)

dot=t.Button(window,text=".",width=5,height=3)
dot.grid(row=4,column=0)
zero=t.Button(window,text="0",width=5,height=3)
zero.grid(row=4,column=1)
equal=t.Button(window,text="=",width=5,height=3)
equal.grid(row=4,column=2)
divide=t.Button(window,text="/",width=5,height=3)
divide.grid(row=4,column=3)

# screen.pack()
# btn1.pack()
# btn2.pack()
# btn1 =t.Button(top_frame,text="Submit",bg="yellow",fg="red")
# btn1.pack()
window.mainloop()
