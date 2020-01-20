from tkinter import *
from tkinter.messagebox import *
import  math
class Gui():
	def __init__(self):
		self.root=Tk()
		self.root.title(' ATM GUI ')
		self.root.resizable(0,0)
		self.ans= StringVar()
		self.ans1= StringVar()
		self.op= StringVar()
		self.balance = 2060.14
		# self.log_in()round(2060.14,2)
		self.buttongui()
		self.screemgui()
		# self.btn5.config(command=self.okk)
		# self.enterframe()
		
		self.root.mainloop()
	# def okk(self):
	# 	print('here')
	# 	pass
	def screemgui(self):

		self.bottomframe = Frame(self.root)
		self.bottomframe.pack( side = BOTTOM )
		
		self.btn2=Button(self.bottomframe,padx=16,bd=8,fg='black',font=('arial',13,'bold'),text="----",bg="powder blue")
		self.btn2.grid(row=1, column=1)

		self.btn4=Button(self.bottomframe,padx=16,bd=8,fg='black',font=('arial',13,'bold'),text="----",bg="powder blue")
		self.btn4.grid(row=2, column=1)

		self.btn3=Button(self.bottomframe,padx=16,bd=8,fg='black',font=('arial',13,'bold'),text="----",bg="powder blue")
		self.btn3.grid(row=3, column=1)

		self.labelframe = LabelFrame(self.bottomframe,text="",width=320, height=120)
		self.labelframe.grid(row=1,column=2,rowspan=4, padx=5, pady=0, ipadx=0, ipady=0)
		
		self.lb = Label(self.labelframe, text="Welcome to ATM python program.",font=('arial', 15,'normal'),)
		self.lb.place(x=0, y=25, anchor="w")

		self.lb1 = Label(self.labelframe, text="Please, press ok",font=('arial', 14,'normal'),)
		self.lb1.place(x=60, y=50, anchor="w")
		# Entry(self.labelframe,).place(x=10, y=10, anchor="w")
		self.lb2 = Label(self.labelframe, text="Enter Your 4 Digit Pin: ",font=('arial', 12,'normal'),)
		self.lb2.place(x=0, y=55, anchor="w")
		self.lb2.place_forget()
		self.text=Entry(self.labelframe,bd=5,textvariable=self.ans,insertwidth=2,bg="powder blue",width=8,justify='right',show='*',font=('arial',20,'bold'))
		self.text.place(x=165, y=55, anchor="w")
		self.text.focus()
		self.text.place_forget()
		self.lb3 = Label(self.labelframe, text="Enter",font=('arial', 14,'normal'),)
		self.lb3.place(x=250, y=15, anchor="w")
		self.lb3.place_forget()
		self.lb4 = Label(self.labelframe, text="Recharge ",font=('arial', 12,'normal'),)
		self.lb4.place(x=0, y=15, anchor="w")
		self.lb4.place_forget()

		self.lb5 = Label(self.labelframe, text="Change pin",font=('arial', 12,'normal'),)
		self.lb5.place(x=0, y=55, anchor="w")
		self.lb5.place_forget()

		self.lb6 = Label(self.labelframe, text="Withdraw",font=('arial', 12,'normal'),)
		self.lb6.place(x=240, y=15, anchor="w")
		self.lb6.place_forget()

		self.lb7 = Label(self.labelframe, text="Balance",font=('arial', 12,'normal'),)
		self.lb7.place(x=240, y=55, anchor="w")
		self.lb7.place_forget()
		self.lb8 = Label(self.labelframe, text="Pay in",font=('arial', 12,'normal'),)
		self.lb8.place(x=240, y=100, anchor="w")
		self.lb8.place_forget()

		self.lb9 = Label(self.labelframe, text="5000",font=('arial', 12,'normal'),)
		self.lb9.place(x=0, y=15, anchor="w")
		self.lb9.place_forget()

		self.lb10 = Label(self.labelframe, text="500",font=('arial', 12,'normal'),)
		self.lb10.place(x=0, y=100, anchor="w")
		self.lb10.place_forget()

		self.lb11 = Label(self.labelframe, text="1000",font=('arial', 12,'normal'),)
		self.lb11.place(x=0, y=55, anchor="w")
		self.lb11.place_forget()

		self.lb12 = Label(self.labelframe, text="10000",font=('arial', 12,'normal'),)
		self.lb12.place(x=240, y=15, anchor="w")
		self.lb12.place_forget()
		self.lb13 = Label(self.labelframe, text="15000",font=('arial', 12,'normal'),)
		self.lb13.place(x=240, y=55, anchor="w")
		self.lb13.place_forget()

		self.lb14 = Label(self.labelframe, text="other",font=('arial', 12,'normal'),)
		self.lb14.place(x=240, y=100, anchor="w")
		self.lb14.place_forget()

		self.lb15 = Label(self.labelframe, text="Would You you like to go back?",font=('arial', 14,'normal'),)
		self.lb15.place(x=0, y=50, anchor="w")
		self.lb15.place_forget()

		self.lb16 = Label(self.labelframe, text="Yes",font=('arial', 12,'normal'),)
		self.lb16.place(x=280, y=15, anchor="w")
		self.lb16.place_forget()

		self.lb17 = Label(self.labelframe, text="No",font=('arial', 12,'normal'),)
		self.lb17.place(x=280, y=55, anchor="w")
		self.lb17.place_forget()

		self.lb18 = Label(self.labelframe, text="Your balance is #",font=('arial', 15,'normal'),)
		self.lb18.place(x=0, y=15, anchor="w")
		self.lb18.place_forget()

		self.lb19 = Label(self.labelframe, text="",font=('arial', 14,'normal'),)
		self.lb19.place(x=165, y=15, anchor="w")
		self.lb19.place_forget()

		self.lb20 = Label(self.labelframe, text="Enter Desired amount: ",font=('arial', 12,'normal'),)
		self.lb20.place(x=0, y=55, anchor="w")
		self.lb20.place_forget()
		self.lb21 = Label(self.labelframe, text="How Much Would You like To pay In? ",font=('arial', 12,'normal'),)
		self.lb21.place(x=0, y=55, anchor="w")
		self.lb21.place_forget()

		self.lb22 = Label(self.labelframe, text="enter Your number",font=('arial', 12,'normal'),)
		self.lb22.place(x=0, y=55, anchor="w")
		self.lb22.place_forget()

		self.lb23 = Label(self.labelframe, text="enter the amount ",font=('arial', 12,'normal'),)
		self.lb23.place(x=0, y=75, anchor="w")
		self.lb23.place_forget()

		self.text1=Entry(self.labelframe,bd=5,textvariable=self.ans1,insertwidth=2,bg="powder blue",justify='right',font=('arial',10,'bold'))
		self.text1.place(x=165, y=55, anchor="w")
		self.text1.focus()
		self.text1.place_forget()

		self.text2=Entry(self.labelframe,bd=5,textvariable=self.ans,insertwidth=2,bg="powder blue",justify='right',font=('arial',10,'bold'))
		self.text2.place(x=165, y=55, anchor="w")
		self.text2.focus()
		self.text2.place_forget()

		self.lbb = Label(self.labelframe, text="",font=('arial', 15,'normal'),)
		self.lbb.place(x=0, y=15, anchor="w")
		self.lbb.place_forget()

	

		self.btn5=Button(self.bottomframe,padx=16,bd=8,fg='black',font=('arial',13,'bold'),text="----",bg="powder blue",command=self.enter)
		self.btn5.grid(row=1, column=3)

		# self.btn6=Button(self.root,padx=16,bd=8,fg='black',font=('arial',13,'bold'),text="----",bg="powder blue",command=lambda:self.numb('-'))
		# self.btn6.grid(row=1, column=4)

		self.btn7=Button(self.bottomframe,padx=16,bd=8,fg='black',font=('arial',13,'bold'),text="----",bg="powder blue")
		self.btn7.grid(row=2, column=3)

		self.btn8=Button(self.bottomframe,padx=16,bd=8,fg='black',font=('arial',13,'bold'),text="----",bg="powder blue")
		self.btn8.grid(row=3, column=3)

		
		# self.buttongui()


	def buttongui(self):
		self.botframe = Frame(self.root)
		self.botframe.pack( side = BOTTOM )

		self.num7=Button(self.botframe,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text="7",bg="powder blue",command=lambda:self.nums(7))
		self.num7.grid(row=1, column=1)

		self.num8=Button(self.botframe,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text="8",bg="powder blue",command=lambda:self.nums(8))
		self.num8.grid(row=1, column=2)

		self.num9=Button(self.botframe,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text="9",bg="powder blue",command=lambda:self.nums(9))
		self.num9.grid(row=1, column=3)

		self.clear=Button(self.botframe,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text="clear",bg="powder blue",command=lambda:self.nclear(''))
		self.clear.grid(row=1, column=4)

		self.num4=Button(self.botframe,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text="4",bg="powder blue",command=lambda:self.nums(4))
		self.num4.grid(row=2, column=1)

		self.num5=Button(self.botframe,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text="5",bg="powder blue",command=lambda:self.nums(5))
		self.num5.grid(row=2, column=2)

		self.num6=Button(self.botframe,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text="6",bg="powder blue",command=lambda:self.nums(6))
		self.num6.grid(row=2, column=3)

		self.cancal=Button(self.botframe,padx=16,bd=8,fg='black',font=('arial',18,'bold'),text="cancel",bg="powder blue", command=lambda:self.operate('*'))
		self.cancal.grid(row=2, column=4)

		self.num3=Button(self.botframe,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text="3",bg="powder blue",command=lambda:self.nums(3))
		self.num3.grid(row=3, column=1)

		self.num2=Button(self.botframe,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text="2",bg="powder blue",command=lambda:self.nums(2))
		self.num2.grid(row=3, column=2)

		self.num1=Button(self.botframe,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text="1",bg="powder blue",command=lambda:self.nums(1))
		self.num1.grid(row=3, column=3)

		self.ok=Button(self.botframe,padx=16,bd=8,fg='black',font=('arial',22,'bold'),text="ok",bg="powder blue", command=self.ok)
		self.ok.grid(row=3, column=4)

		self.zero=Button(self.botframe,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text="0",bg="powder blue", width=17,command=lambda:self.nums(0))
		self.zero.grid(row=4, column=1,columnspan=4)

		

		self.num=""
		self.ope=""
		self.c=""
		self.val1=self.val2=0
	
	def nclear(self,m):
		self.ans.set("")
		self.num=""
	def ok(self):
		# pass
		# self.labelframe.destroy()
		# self.framebtn()
		self.lb.place_forget()
		self.lb1.place_forget()
		self.lb2.place(x=0, y=55, anchor="w")
		self.lb3.place(x=250, y=15, anchor="w")
		self.text.place(x=165, y=55, anchor="w")
		self.ok.config(state='disabled')
	def verify_pin(self,pin):
		self.pins='1234'
		if self.pin == self.pins:
			return True
		else:
			return False
	
	def log_in(self):
		# pass
		self.tries = 0
		self.pin=self.text.get()
		if self.verify_pin(self.pin):
			print("Pin accepted!")
			return True
		else:
			showinfo("Warming","Insufficient balance")			
			print("Invalid pin")
				
	
	def enter(self):
	 	if self.log_in():
	 		self.ans1.set("")
	 		self.ans.set("")
	 		self.num=""
	 		self.lb2.place_forget()
	 		self.lb3.place_forget()
	 		self.text.place_forget()
	 		self.lb4.place(x=0, y=15, anchor="w")
	 		self.lb5.place(x=0, y=55, anchor="w")
	 		self.lb6.place(x=240, y=15, anchor="w")
	 		self.lb7.place(x=240, y=55, anchor="w")
	 		self.lb8.place(x=240, y=100, anchor="w")
	 		self.btn2.config(command=self.recharge)
	 		self.btn3.config(command=self.changepins)
	 		# self.btn4.config(command=self.withdraw)
	 		self.btn5.config(command=self.withdraws)
	 		self.btn8.config(command=self.Payin)
	 		self.btn7.config(command=self.balances)
	 
	def withdraws(self):
		pass
		# print('here')
		self.lb4.place_forget()
		self.lb5.place_forget()
		self.lb6.place_forget()
		self.lb7.place_forget()
		self.lb8.place_forget()
		self.lb9.place(x=0, y=15, anchor="w")
		self.lb10.place(x=0, y=100, anchor="w")
		self.lb11.place(x=0, y=55, anchor="w")
		self.lb12.place(x=240, y=15, anchor="w")
		self.lb13.place(x=240, y=55, anchor="w")
		self.lb14.place(x=240, y=100, anchor="w")
		self.btn2.config(command=lambda:self.numb(5000))
		self.btn4.config(command=lambda:self.numb(1000))
		self.btn3.config(command=lambda:self.numb(500))
		self.btn5.config(command=lambda:self.numb(10000))
		self.btn8.config(command=self.others)
		self.btn7.config(command=lambda:self.numb(15000))
	def others(self):
		self.lb9.place_forget()
		self.lb10.place_forget()
		self.lb11.place_forget()
		self.lb12.place_forget()
		self.lb13.place_forget()
		self.lb14.place_forget()
		self.lb20.place(x=0, y=55, anchor="w")
		self.text1.place(x=165, y=55, anchor="w")
		self.lb3.place(x=250, y=15, anchor="w")
		self.btn5.config(command=self.enter2)
		
	def enter2(self):
		self.withdraw=float(self.text1.get())
		self.balance=round(self.balance - self.withdraw,2)
		self.result=round(self.withdraw,2)
		print(self.withdraw)
		print(self.balance)
		self.lb20.place_forget()
		self.text1.place_forget()
		self.lb3.place_forget()
		self.lb15.place(x=0, y=50, anchor="w")
		self.lb16.place(x=280, y=15, anchor="w")
		self.lb17.place(x=280, y=55, anchor="w")
		self.lbb.place(x=0, y=15, anchor="w")
		self.lbb.config(text=self.result)
		self.btn5.config(command=self.back)
		self.btn7.config(command=self.no)
		pass
	def balances(self):
		print('here')
		print(self.balance)
		self.lb4.place_forget()
		self.lb5.place_forget()
		self.lb6.place_forget()
		self.lb7.place_forget()
		self.lb8.place_forget()
		self.lb18.place(x=0, y=15, anchor="w")
		self.lb19.place(x=165, y=15, anchor="w")
		self.lb19.config(text=round(self.balance,2))
		self.lb15.place(x=0, y=50, anchor="w")
		self.lb16.place(x=280, y=15, anchor="w")
		self.lb17.place(x=280, y=55, anchor="w")
		self.btn5.config(command=self.back)
		# self.btn8.config(command=lambda:self.numb(20000))
		self.btn7.config(command=self.no)

		# pass
	def Payin(self):
		self.lb4.place_forget()
		self.lb5.place_forget()
		self.lb6.place_forget()
		self.lb7.place_forget()
		self.lb8.place_forget()
		self.lb21.place(x=0, y=45, anchor="w")
		self.text1.place(x=165, y=75, anchor="w")
		self.lb3.place(x=250, y=15, anchor="w")
		self.btn5.config(command=self.enter3)
		
		# print('here')
		pass
	def enter3(self):
		self.payin=float(self.text1.get())
		self.balance=round(self.balance + self.payin,2)
		self.result=round(self.balance,2)
		self.lb21.place_forget()
		self.text1.place_forget()
		self.lb3.place_forget()
		self.lb15.place(x=0, y=50, anchor="w")
		self.lb16.place(x=280, y=15, anchor="w")
		self.lb17.place(x=280, y=55, anchor="w")
		self.lbb.place(x=0, y=15, anchor="w")
		self.lbb.config(text=self.result)
		self.btn5.config(command=self.back)
		self.btn7.config(command=self.no)	
	def recharge(self):
		self.lb4.place_forget()
		self.lb5.place_forget()
		self.lb6.place_forget()
		self.lb7.place_forget()
		self.lb8.place_forget()
		self.lb22.place(x=0, y=45, anchor="w")
		self.lb23.place(x=0, y=75, anchor="w")
		self.text1.place(x=165, y=45, anchor="w")
		self.text2.place(x=165, y=75, anchor="w")
		self.lb3.place(x=250, y=15, anchor="w")
		self.btn5.config(command=self.enter4)
		pass
	def enter4(self):
		self.number=float(self.text1.get())
		self.amount=float(self.text2.get())
		self.balance=round(self.balance - self.amount,2)
		self.result=round(self.balance,2)
		self.lb22.place_forget()
		self.lb23.place_forget()
		self.text1.place_forget()
		self.text2.place_forget()
		self.lb3.place_forget()
		self.lb15.place(x=0, y=50, anchor="w")
		self.lb16.place(x=280, y=15, anchor="w")
		self.lb17.place(x=280, y=55, anchor="w")
		self.lbb.place(x=0, y=15, anchor="w")
		self.lbb.config(text=self.result)
		self.btn5.config(command=self.back)
		self.btn7.config(command=self.no)		
	def changepins(self):
		print('here')
		pass
	def numb(self,numbers):
		self.withdraw=numbers
		print(self.withdraw)
		print(self.balance)
		
		if self.balance <=self.withdraw:
			showinfo("Warming","Insufficient balance")
			print('Insufficient balance')
		else:
			self.balance=self.balance - self.withdraw
			self.result=round(self.withdraw,2)
			self.lb9.place_forget()
			self.lb10.place_forget()
			self.lb11.place_forget()
			self.lb12.place_forget()
			self.lb13.place_forget()
			self.lb14.place_forget()
			self.lb15.place(x=0, y=50, anchor="w")
			self.lb16.place(x=280, y=15, anchor="w")
			self.lb17.place(x=280, y=55, anchor="w")
			self.lbb.place(x=0, y=15, anchor="w")
			self.lbb.config(text=self.result)
			self.btn5.config(command=self.back)
			self.btn7.config(command=self.no)

	def back(self):
		self.lb15.place_forget()
		self.lb16.place_forget()
		self.lb17.place_forget()
		self.lbb.place_forget()
		self.lb19.place_forget()
		self.lb18.place_forget()
		self.lb4.place(x=0, y=15, anchor="w")
		self.lb5.place(x=0, y=55, anchor="w")
		self.lb6.place(x=240, y=15, anchor="w")
		self.lb7.place(x=240, y=55, anchor="w")
		self.lb8.place(x=240, y=100, anchor="w")
		self.btn2.config(command=self.recharge)
		self.btn3.config(command=self.changepins)
		# self.btn4.config(command=self.withdraw)
		self.btn5.config(command=self.withdraws)
		self.btn8.config(command=self.Payin)
		self.btn7.config(command=self.balances)
		self.ans1.set("")
		self.ans.set("")
		self.num=""
	def no(self):
		# pass
		showinfo("Thanks","Thank You for Banking with us")
		# print('Thank You for Banking with us')
		self.bottomframe.destroy()
		self.screemgui()
		self.ok.config(state='normal')
		self.ans1.set("")
		self.ans.set("")
		self.num=""
		
	def nums(self,number):
		self.num+=str(number)
		# print(self.num)
		self.ans.set(self.num)
		self.ans1.set(self.num)
Gui()



























# # from tkinter import *
# # root = Tk()

# # labelframe = LabelFrame(root, text="This is a LabelFrame")
# # labelframe.grid(row=1,column=2,columnspan=2)
 
# # left = Label(labelframe, text="Inside the LabelFrame")
# # left.grid()
 
# # root.mainloop()
# from tkinter import *

# form = Tk()
# form.geometry('250x150') 
# errorArea = LabelFrame(form, text=" Errors ", width=250, height=80)
# errorArea.grid(row=2, column=0, columnspan=2, sticky="E", \
#              padx=5, pady=0, ipadx=0, ipady=0)

# errorMessage = Label(errorArea, text="coordinates",font=('arial',72,'bold') )

# # 1) 'x' and 'y' are the x and y coordinates inside 'errorArea'
# # 2) 'place' uses 'anchor' instead of 'sticky'
# # 3) There is no need for 'padx' and 'pady' with 'place'
# # since you can specify the exact coordinates
# errorMessage.place(x=10, y=10, anchor="w")
# form.mainloop()