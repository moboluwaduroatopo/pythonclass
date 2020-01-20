from tkinter import *
from tkinter.messagebox import *
import mysql.connector
import  math
class Gui():
	def __init__(self):
		self.root=Tk()
		self.root.title(' ATM GUI ')
		self.root.resizable(0,0)
		self.ans= StringVar()
		self.ans1= StringVar()
		self.op= StringVar()
		self.ADDRESS = StringVar()
		self.USERNAME = StringVar()
		self.PASSWORD = StringVar()
		self.NAME = StringVar()
		self.PHONE = StringVar()
		self.PIN = StringVar()
		self.AMOUNT = StringVar()
		# self.balance = 2060.14
		# self.log_in()round(2060.14,2)
		# self.buttongui()
		# self.screemgui()
		self.LoginForm()
		
		self.root.mainloop()
	def Database(self):
		self.mycon=mysql.connector.connect(host="localhost",user='root',passwd='',database='pythonatm_db')
		self.mycursor=self.mycon.cursor()
		self.mycursor.execute("CREATE TABLE IF NOT EXISTS `customers` (customer_id INTEGER(4) PRIMARY KEY AUTO_INCREMENT NOT NULL, username VARCHAR(200), password VARCHAR(200), name VARCHAR(200), address VARCHAR(200), phone VARCHAR(200) )")
		self.mycursor.execute("CREATE TABLE IF NOT EXISTS `account_info` (account_id INTEGER(8) PRIMARY KEY AUTO_INCREMENT NOT NULL,customer_id INTEGER(4), pin VARCHAR(4), amount VARCHAR(200))")


	def LoginForm(self):	
		self.LoginFrame = Frame(self.root)
		self.LoginFrame.pack(side=TOP, pady=80)
		self.lbl_username = Label(self.LoginFrame, text="Username:", font=('arial', 25), bd=18)
		self.lbl_username.grid(row=1)
		self.lbl_password = Label(self.LoginFrame, text="Password:", font=('arial', 25), bd=18)
		self.lbl_password.grid(row=2)
		self.lbl_result1 = Label(self.LoginFrame, text="", font=('arial', 18))
		self.lbl_result1.grid(row=3, columnspan=2)
		self.username = Entry(self.LoginFrame, font=('arial', 20), textvariable=self.USERNAME, width=15)
		self.username.grid(row=1, column=1)
		self.password = Entry(self.LoginFrame, font=('arial', 20), textvariable=self.PASSWORD, width=15, show="*")
		self.password.grid(row=2, column=1)
		self.btn_login = Button(self.LoginFrame, text="Login", font=('arial', 18), width=35, command=self.Login)
		self.btn_login.grid(row=4, columnspan=2, pady=20)
		self.lbl_register = Label(self.LoginFrame, text="Registers", fg="Blue", font=('arial', 12))
		self.lbl_register.grid(row=0, sticky=W)
		self.lbl_register.bind('<Button-1>', self.ToggleToRegister)
	def Next(self):
		if self.USERNAME.get == "" or self.PASSWORD.get() == "" or self.NAME.get() == "" or self.PHONE.get() == "" or self.ADDRESS.get() == "":
			self.lbl_result2.config(text="Please complete the required field!", fg="orange")
		else:
			self.RegisterFrame.destroy()
			self.AccountForm()
	def AccountForm(self):	
		self.AccountFrame = Frame(self.root)
		self.AccountFrame.pack(side=TOP, pady=80)
		self.lbl_pin = Label(self.AccountFrame, text="Pin:", font=('arial', 25), bd=18)
		self.lbl_pin.grid(row=1)
		self.lbl_amount = Label(self.AccountFrame, text="Amount:", font=('arial', 25), bd=18)
		self.lbl_amount.grid(row=2)
		self.lbl_result1 = Label(self.AccountFrame, text="", font=('arial', 18))
		self.lbl_result1.grid(row=3, columnspan=2)
		self.pin = Entry(self.AccountFrame, font=('arial', 20), textvariable=self.PIN, width=15,show="*")
		self.pin.grid(row=1, column=1)
		self.amount = Entry(self.AccountFrame, font=('arial', 20), textvariable=self.AMOUNT, width=15,)
		self.amount.grid(row=2, column=1)
		self.btn_login = Button(self.AccountFrame, text="Save", font=('arial', 18), width=35, command=self.Accountsave)
		self.btn_login.grid(row=4, columnspan=2, pady=20)
		self.lbl_register = Label(self.AccountFrame, text="Set Account info", fg="Blue", font=('arial', 12))
		self.lbl_register.grid(row=0, sticky=W)	
	def RegisterForm(self):
		self.RegisterFrame = Frame(self.root)
		self.RegisterFrame.pack(side=TOP, pady=40)
		self.lbl_username = Label(self.RegisterFrame, text="Username:", font=('arial', 18), bd=18)
		self.lbl_username.grid(row=1)
		self.lbl_password = Label(self.RegisterFrame, text="Password:", font=('arial', 18), bd=18)
		self.lbl_password.grid(row=2)
		self.address = Label(self.RegisterFrame, text="Address:", font=('arial', 18), bd=18)
		self.address.grid(row=3)
		self.name = Label(self.RegisterFrame, text="Name:", font=('arial', 18), bd=18)
		self.name.grid(row=4)
		self.phone = Label(self.RegisterFrame, text="Phone:", font=('arial', 18), bd=18)
		self.phone.grid(row=5)
		self.lbl_result2 = Label(self.RegisterFrame, text="", font=('arial', 18))
		self.lbl_result2.grid(row=6, columnspan=2)
		self.username = Entry(self.RegisterFrame, font=('arial', 20), textvariable=self.USERNAME, width=15)
		self.username.grid(row=1, column=1)
		self.password = Entry(self.RegisterFrame, font=('arial', 20), textvariable=self.PASSWORD, width=15, show="*")
		self.password.grid(row=2, column=1)
		self.address = Entry(self.RegisterFrame, font=('arial', 20), textvariable=self.ADDRESS, width=15)
		self.address.grid(row=3, column=1)
		self.name = Entry(self.RegisterFrame, font=('arial', 20), textvariable=self.NAME, width=15)
		self.name.grid(row=4, column=1)
		self.phone = Entry(self.RegisterFrame, font=('arial', 20), textvariable=self.PHONE, width=15)
		self.phone.grid(row=5, column=1)
		self.btn_login = Button(self.RegisterFrame, text="Next", font=('arial', 18), width=35, command=self.Next)
		self.btn_login.grid(row=7, columnspan=2, pady=20)
		self.lbl_login = Label(self.RegisterFrame, text="Login", fg="Blue", font=('arial', 12))
		self.lbl_login.grid(row=0, sticky=W)
		self.lbl_login.bind('<Button-1>', self.ToggleToLogin)
	def Login(self):
		# pass
		self.Database()
		if self.USERNAME.get == "" or self.PASSWORD.get() == "":
			self.lbl_result2.config(text="Please complete the required field!", fg="orange")	
		else:
			self.user1=self.USERNAME.get()
			self.passwd=str(self.PASSWORD.get())
			self.sqlf="SELECT * FROM customers where username=%s and password=%s"
			self.val=(self.user1,self.passwd)
			self.mycursor.execute(self.sqlf,self.val)
			self.result=self.mycursor.fetchall()
			self.res=self.result[0]
			print(self.res[0])
			print(self.val)
			if self.mycursor.rowcount:
				self.LoginFrame.destroy()
				# self.AccountForm()
				self.buttongui()
				self.screemgui()
				# self.lbl_result1.config(text="You Successfully Login", fg="red")
			else:
				self.lbl_result1.config(text="Invalid Username or password", fg="red")
			print(self.result)	
		
		# if self.USERNAME.get == "" or self.PASSWORD.get() == "":
		# 	self.lbl_result2.config(text="Please complete the required field!", fg="orange")
	def Accountsave(self):
		self.Database()
		if self.PIN.get == "" or self.AMOUNT.get() == "":
			self.lbl_result1.config(text="Please complete the required field!", fg="orange")
		else:
			self.user1=self.USERNAME.get()
			self.sqlf="SELECT * FROM customers where username=%s"
			self.val=(self.user1,)
			self.mycursor.execute(self.sqlf,self.val)
			self.result=self.mycursor.fetchall()
			print(self.mycursor.rowcount)
			if self.mycursor.rowcount > 0:
				self.lbl_result1.config(text="Username is already taken", fg="red")
			else:
				self.user=str(self.USERNAME.get())
				self.passwd=str(self.PASSWORD.get())
				self.name=str(self.NAME.get())
				self.phone=str(self.PHONE.get())
				self.address=str(self.ADDRESS.get())
				self.sql="INSERT INTO customers (username,password,name,address,phone) VALUES(%s,%s,%s,%s,%s)"
				self.val=[(self.user,self.passwd,self.name,self.address,self.phone)]
				print(self.val)
				self.mycursor.executemany(self.sql,self.val)
				self.mycon.commit()
				self.sqlf="SELECT * FROM customers where username=%s"
				self.val=(self.user,)
				self.mycursor.execute(self.sqlf,self.val)
				self.result=self.mycursor.fetchall()
				self.res=self.result[0]
				print(self.res[0])
				self.pin=str(self.PIN.get())
				self.amount=str(self.AMOUNT.get())
				self.customer_id=self.res[0]
				self.sql="INSERT INTO account_info (customer_id,pin,amount) VALUES(%s,%s,%s)"
				self.val=[(self.customer_id,self.pin,self.amount)]
				self.mycursor.executemany(self.sql,self.val)
				self.mycon.commit()
				self.PIN.set("")
				self.AMOUNT.set("")
				# print(self.result)
				self.USERNAME.set("")
				self.PASSWORD.set("")
				self.NAME.set("")
				self.PHONE.set("")
				self.ADDRESS.set("")
				self.AccountFrame.destroy()
				self.LoginForm()
				# self.lbl_result1.config(text="Successfully Created!", fg="black")
			# self.buttongui()
			# self.screemgui()
	# def Register(self):
	# 	self.Database()
	# 	if self.USERNAME.get == "" or self.PASSWORD.get() == "" or self.NAME.get() == "" or self.PHONE.get() == "" or self.ADDRESS.get() == "":
	# 		self.lbl_result2.config(text="Please complete the required field!", fg="orange")	
	# 	else:
	# 		self.user1=self.USERNAME.get()
	# 		self.sqlf="SELECT * FROM customers where username=%s"
	# 		self.val=(self.user1,)
	# 		self.mycursor.execute(self.sqlf,self.val)
	# 		self.result=self.mycursor.fetchall()
	# 		print(self.mycursor.rowcount)
	# 		if self.mycursor.rowcount > 0:
	# 			self.lbl_result2.config(text="Username is already taken", fg="red")
	# 		else:
	# 			self.user=str(self.USERNAME.get())
	# 			self.passwd=str(self.PASSWORD.get())
	# 			self.name=str(self.NAME.get())
	# 			self.phone=str(self.PHONE.get())
	# 			self.address=str(self.ADDRESS.get())
	# 			self.sql="INSERT INTO customers (username,password,name,address,phone) VALUES(%s,%s,%s,%s,%s)"
	# 			self.val=[(self.user,self.passwd,self.name,self.address,self.phone)]
	# 			print(self.val)
	# 			self.mycursor.executemany(self.sql,self.val)
	# 			self.mycon.commit()
	# 			# self.user1=self.USERNAME.get()
				
	# 			self.USERNAME.set("")
	# 			self.PASSWORD.set("")
	# 			self.NAME.set("")
	# 			self.PHONE.set("")
	# 			self.ADDRESS.set("")
	# 			self.lbl_result2.config(text="Successfully Created!", fg="black")
	def ToggleToRegister(self,event=None):
		self.LoginFrame.destroy()
		self.RegisterForm()
	def ToggleToLogin(self,event=None):
		self.RegisterFrame.destroy()
		self.LoginForm()

	def screemgui(self):
		
		# print(self.account[0][3])
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

	

		self.btn5=Button(self.bottomframe,padx=16,bd=8,fg='black',font=('arial',13,'bold'),state='disabled',text="----",bg="powder blue",command=self.enter)
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

		self.balan=self.res[0]
		self.sqlf="SELECT * FROM account_info where customer_id=%s"
		self.val=(self.balan,)
		self.mycursor.execute(self.sqlf,self.val)
		self.account=self.mycursor.fetchall()
		self.balance=float(self.account[0][3])
		print(self.balance)

		self.num=""
		
	def nclear(self,m):
		self.ans.set("")
		self.num=""
	def ok(self):
		# pass
		# self.labelframe.destroy()
		# self.framebtn()
		self.btn5.config(state='normal')
		self.lb.place_forget()
		self.lb1.place_forget()
		self.lb2.place(x=0, y=55, anchor="w")
		self.lb3.place(x=250, y=15, anchor="w")
		self.text.place(x=165, y=55, anchor="w")
		self.ok.config(state='disabled')
	def verify_pin(self,pin):
		self.pins=self.account[0][2]
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
			showinfo("Warming","Invalid pin")			
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
	 		self.btn4.config(command=self.changepins)
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
		self.btn2.config(state='disabled')
		self.btn4.config(state='disabled')
		self.btn3.config(state='disabled')
		self.btn7.config(state='disabled')
		self.btn8.config(state='disabled')
		
	def enter2(self):
		# self.balance=self.account[0][3]
		self.withdraw=float(self.text1.get())
		self.balance=round(self.balance - self.withdraw,2)
		self.result=round(self.withdraw,2)
		print(self.withdraw)
		print(self.balance)
		self.id=self.res[0]
		self.sql = "UPDATE account_info SET amount = %s WHERE customer_id = %s"
		self.val = (self.balance,self.id)
		self.mycursor.execute(self.sql, self.val)
		self.mycon.commit()
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
		self.btn2.config(state='disabled')
		self.btn4.config(state='disabled')
		self.btn3.config(state='disabled')
			# self.btn5.config(state='disabled')
		self.btn8.config(state='disabled')
		self.btn7.config(state='normal')
	def balances(self):
		# self.balance=self.account[0][3]
		# print('here')
		print(self.balance)
		self.lb4.place_forget()
		self.lb5.place_forget()
		self.lb6.place_forget()
		self.lb7.place_forget()
		self.lb8.place_forget()
		self.lb18.place(x=0, y=15, anchor="w")
		self.lb19.place(x=165, y=15, anchor="w")
		self.lb19.config(text=self.balance)
		self.lb15.place(x=0, y=50, anchor="w")
		self.lb16.place(x=280, y=15, anchor="w")
		self.lb17.place(x=280, y=55, anchor="w")
		self.btn5.config(command=self.back)
		# self.btn8.config(command=lambda:self.numb(20000))
		self.btn7.config(command=self.no)
		self.btn2.config(state='disabled')
		self.btn4.config(state='disabled')
		self.btn3.config(state='disabled')
			# self.btn5.config(state='disabled')
		self.btn8.config(state='disabled')
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
		self.btn2.config(state='disabled')
		self.btn4.config(state='disabled')
		self.btn3.config(state='disabled')
		self.btn7.config(state='disabled')
		self.btn8.config(state='disabled')
		# print('here')
		pass
	def enter3(self):
		# self.balance=self.account[0][3]
		self.payin=float(self.text1.get())
		self.balance=round(self.balance + self.payin,2)
		self.result=round(self.balance,2)
		self.id=self.res[0]
		self.sql = "UPDATE account_info SET amount = %s WHERE customer_id = %s"
		self.val = (self.balance,self.id)
		self.mycursor.execute(self.sql, self.val)
		self.mycon.commit()
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
		self.btn2.config(state='disabled')
		self.btn4.config(state='disabled')
		self.btn3.config(state='disabled')
		self.btn7.config(state='normal')
			# self.btn5.config(state='disabled')
		self.btn8.config(state='disabled')
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
		self.btn2.config(state='disabled')
		self.btn4.config(state='disabled')
		self.btn3.config(state='disabled')
		self.btn7.config(state='disabled')
		self.btn8.config(state='disabled')
		pass
	def enter4(self):
		# self.balance=self.account[0][3]
		self.number=float(self.text1.get())
		self.amount=float(self.text2.get())
		self.balance=round(self.balance - self.amount,2)
		self.result=round(self.balance,2)
		self.id=self.res[0]
		self.sql = "UPDATE account_info SET amount = %s WHERE customer_id = %s"
		self.val = (self.balance,self.id)
		self.mycursor.execute(self.sql, self.val)
		self.mycon.commit()
		self.lb22.place_forget()
		self.lb23.place_forget()
		self.text1.place_forget()
		self.text2.place_forget()
		self.lb3.place_forget()
		self.lb15.place(x=0, y=50, anchor="w")
		self.lb16.place(x=280, y=15, anchor="w")
		self.lb17.place(x=280, y=55, anchor="w")
		self.lbb.place(x=0, y=15, anchor="w")
		self.btn2.config(state='disabled')
		self.btn4.config(state='disabled')
		self.btn3.config(state='disabled')
		self.btn7.config(state='normal')
		self.btn8.config(state='disabled')
		self.lbb.config(text=self.result)
		self.btn5.config(command=self.back)
		self.btn7.config(command=self.no)		
	def changepins(self):
		print('here')
		pass
	def numb(self,numbers):
		self.withdraw=numbers
		# self.balance=self.account[0][3]
		# self.balance=self.balance - self.withdraw
		print(self.withdraw)
		print(self.balance)

		if self.balance <= self.withdraw:
			showinfo("Warming","Insufficient balance")
			print('Insufficient balance')
		else:
			self.id=self.res[0]
			self.balance=self.balance - self.withdraw
			self.result=round(self.withdraw,2)
			print(self.balance)
			self.sql = "UPDATE account_info SET amount = %s WHERE customer_id = %s"
			self.val = (self.balance,self.id)
			self.mycursor.execute(self.sql, self.val)
			self.mycon.commit()
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
			self.btn2.config(state='disabled')
			self.btn4.config(state='disabled')
			self.btn3.config(state='disabled')
			# self.btn5.config(state='disabled')
			self.btn8.config(state='disabled')
			# self.btn7.config(state='disabled')

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
		self.btn2.config(state='normal')
		self.btn4.config(state='normal')
		self.btn3.config(state='normal')
			# self.btn5.config(state='disabled')
		self.btn8.config(state='normal')
		self.ans1.set("")
		self.ans.set("")
		self.num=""
	def no(self):
		self.btn2.config(state='normal')
		self.btn4.config(state='normal')
		self.btn3.config(state='normal')
			# self.btn5.config(state='disabled')
		self.btn8.config(state='normal')
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
		# self.num +=number
		# print(self.n)
		self.num+=str(number)
		# print(self.numbs)
		self.ans.set(self.num)
		self.ans1.set(self.num)
Gui()

