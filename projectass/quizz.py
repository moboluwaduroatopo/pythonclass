from tkinter import *
import json
from tkinter.messagebox import *
import mysql.connector
class Quiz():
	def __init__(self):
		# self.root=Tk()
		self.root = Tk()
		self.width = 690
		self.height = 480
		self.screen_width = self.root.winfo_screenwidth()
		self.screen_height =self.root.winfo_screenheight()
		self.x = (self.screen_width/2) - (self.width/2)
		self.y = (self.screen_height/2) - (self.height/2)
		self.root.geometry("%dx%d+%d+%d" % (self.width, self.height, self.x, self.y))
		self.root.title('ICT Quiz')
		self.root.resizable(0,0)
		self.qindex=0;
		self.qn = 0
		self.ans= StringVar()
		self.results= StringVar()
		self.opt_selected= StringVar()
		self.USERNAME = StringVar()
		self.PASSWORD = StringVar()
		self.FIRSTNAME = StringVar()
		self.LASTNAME = StringVar()
		self.mycon=mysql.connector.connect(host="localhost",user='root',passwd='',database='pythoncbt_db')
		self.mycursor=self.mycon.cursor()
		self.mycursor.execute("SELECT * FROM question")
		self.y= self.mycursor.fetchall()
		self.a=self.y[self.qn]
		print(self.a)
		self.ops=[self.a[2],self.a[3],self.a[4],self.a[5]]
		# print(self.ops)
		self.correct = 0
		
		self.LoginForm()
		# self.ques = self.create_q(master, self.qn)
		# self.opts = self.create_options(master,4)
		# self.opts2 = self.anything(master,4)
		
		
		# self.button = Button(master, text="Next", command=self.next_btn)
		# self.button.pack(side=TOP)
		# self.button = Button(master, text="Back", command=self.back)
		# self.button.pack(side=TOP)
		# self.result=Label(master, textvariable=self.results)
		# self.result.pack(side=TOP, anchor="w")
		self.root.mainloop()
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
	def RegisterForm(self):
		self.RegisterFrame = Frame(self.root)
		self.RegisterFrame.pack(side=TOP, pady=40)
		self.lbl_username = Label(self.RegisterFrame, text="Username:", font=('arial', 18), bd=18)
		self.lbl_username.grid(row=1)
		self.lbl_password = Label(self.RegisterFrame, text="Password:", font=('arial', 18), bd=18)
		self.lbl_password.grid(row=2)
		
		self.lbl_result2 = Label(self.RegisterFrame, text="", font=('arial', 18))
		self.lbl_result2.grid(row=5, columnspan=2)
		self.username = Entry(self.RegisterFrame, font=('arial', 20), textvariable=self.USERNAME, width=15)
		self.username.grid(row=1, column=1)
		self.password = Entry(self.RegisterFrame, font=('arial', 20), textvariable=self.PASSWORD, width=15, show="*")
		self.password.grid(row=2, column=1)
		# self.firstname = Entry(self.RegisterFrame, font=('arial', 20), textvariable=self.FIRSTNAME, width=15)
		# self.firstname.grid(row=3, column=1)
		# self.lastname = Entry(self.RegisterFrame, font=('arial', 20), textvariable=self.LASTNAME, width=15)
		# self.lastname.grid(row=4, column=1)
		self.btn_login = Button(self.RegisterFrame, text="Register", font=('arial', 18), width=35, command=self.Register)
		self.btn_login.grid(row=6, columnspan=2, pady=20)
		self.lbl_login = Label(self.RegisterFrame, text="Login", fg="Blue", font=('arial', 12))
		self.lbl_login.grid(row=0, sticky=W)
		self.lbl_login.bind('<Button-1>', self.ToggleToLogin)
	def Login(self):
		# pass
		# self.Database()
		if self.USERNAME.get == "" or self.PASSWORD.get() == "":
			self.lbl_result2.config(text="Please complete the required field!", fg="orange")	
		else:
			self.user1=self.USERNAME.get()
			self.passwd=str(self.PASSWORD.get())
			self.sqlf="SELECT * FROM user where user_name=%s and password=%s"
			self.val=(self.user1,self.passwd)
			self.mycursor.execute(self.sqlf,self.val)
			self.result=self.mycursor.fetchall()
			self.res=self.result[0]
			print(self.res[0])
			print(self.val)
			if self.mycursor.rowcount:
				self.LoginFrame.destroy()
				self.QusetionrFrame = Frame(self.root)
				self.QusetionrFrame.pack(side=BOTTOM)
				self.ques = self.create_q(self.qn)
				self.opts = self.create_options(4)
				self.display_q(self.qn)
				self.l_result = Label(self.QusetionrFrame, text="", font=('arial', 18))
				self.l_result.grid(row=3, columnspan=2)
				self.button = Button(self.QusetionrFrame, text="Next",width=10 , command=self.next_btn)
				self.button.grid(row=4)
				self.button = Button(self.QusetionrFrame, text="Back",width=10 , command=self.back)
				self.button.grid(row=4,column=2)
			else:
				self.lbl_result1.config(text="Invalid Username or password", fg="red")
			print(self.result)	
		
	def Register(self):
		if self.USERNAME.get == "" or self.PASSWORD.get() == "":
			self.lbl_result2.config(text="Please complete the required field!", fg="orange")	
		else:
			self.user1=self.USERNAME.get()
			self.sqlf="SELECT * FROM user where user_name=%s"
			self.val=(self.user1,)
			self.mycursor.execute(self.sqlf,self.val)
			self.result=self.mycursor.fetchall()
			print(self.result)
			if self.mycursor.rowcount > 0:
				self.lbl_result2.config(text="Username is already taken", fg="red")
			else:
				self.user=str(self.USERNAME.get())
				self.passwd=str(self.PASSWORD.get())
				self.sql="INSERT INTO user (user_name,password) VALUES(%s,%s)"
				self.val=[(self.user,self.passwd)]
				print(self.val)
				self.mycursor.executemany(self.sql,self.val)
				self.mycon.commit()
				self.USERNAME.set("")
				self.PASSWORD.set("")
				self.lbl_result2.config(text="Successfully Created!", fg="black")
	def ToggleToRegister(self,event=None):
		self.LoginFrame.destroy()
		self.RegisterForm()
	def ToggleToLogin(self,event=None):
		self.RegisterFrame.destroy()
		self.LoginForm()
	def create_q(self,qn):
		self.qFrame = Frame(self.root)
		self.qFrame.pack(side=TOP, pady=30)
		self.lab=Label(self.qFrame, text=self.a[1],font=('arial', 12), bd=18)
		self.lab.grid(row=1)
		return  self.lab
	def create_options(self,n):
		# print(n)
		b_val = 0
		b = []
		while b_val < n:
			# print(b_val+1)
			# print(n)
			# print('here')
			self.oFrame = Frame(self.root)
			self.oFrame.pack(side=TOP, pady=2)
			btn = Radiobutton(self.oFrame, text="foo",font=('arial', 12), bd=18, variable=self.opt_selected, value=b_val+1)
			b.append(btn)
			btn.grid(row=2)
			b_val +=1
			# print('here')
			
		return b
		
		# self.optiona=Radiobutton(master, variable=self.opt_selected, text=self.a['optiona'], value=self.a['optiona']).pack(side=TOP, anchor="w")
		# self.optionb=Radiobutton(master, variable=self.opt_selected, text=self.a['optionb'], value=self.a['optionb']).pack(side=TOP, anchor="w")
		# self.optionc=Radiobutton(master, variable=self.opt_selected, text=self.a['optionc'], value=self.a['optionc']).pack(side=TOP, anchor="w")
		# self.optiond=Radiobutton(master, variable=self.opt_selected, text=self.a['optiond'], value=self.a['optiond']).pack(side=TOP, anchor="w")
		
	def display_q(self,qn):
		val = 0
		self.opt_selected.set(0)
		self.b=self.y[qn]
		self.ops=[self.b[2],self.b[3],self.b[4],self.b[5]]
		# print(self.ops)
		self.ans=self.b[6]
		# self.create_q()
		# self.create_options()
		self.ques['text'] = self.b[1]
		# self.opts['text'] = self.b['optiona']
		for op in self.ops:
			# print(op)
			self.opts[val]['text'] = op
			self.opts[val]['value'] =op
			val = val + 1
			# print(b_val)
	def check_q(self,qn):
		# print('here')
		# print(self.opt_selected.get())
		self.optio=self.opt_selected.get()
		# print(self.ans)
		# print(self.ops)
		if self.optio == self.ans:
			return True
		return False
	def print_results(self):
		self.s="Your Score:"
		self.result=self.s , self.correct, '/', len(self.y)
		# self.res = "Your result",self.result
		# self.l_results.set(self.result)
		self.l_result.config(text=self.result, fg="orange")	
		showinfo("Score",self.result)
		# self.result.pack(side=TOP, anchor="w")
		# print("Your Score: ", self.correct, "/", len(self.y))	
		print(self.result)
	def next_btn(self):
		if self.check_q(self.qn):
			print('correct')
			self.correct+=1
		else:
			print('wrong')
		self.qn = self.qn + 1
		if self.qn >= len(self.y):
			self.print_results()
			# self.results.set()
		else:
			# self.qn = self.qn + 1
			self.display_q(self.qn)	
			print(self.display_q(self.qn))
		# if n=='ZERO':
		# 	self.qindex=0
		# elif(n=='next'):
		# 	if(self.qindex=len())	

		# self.ans.set(val1 + val2)
	def back(self):
		self.qn = self.qn - 1
		self.display_q(self.qn)
	def operate(self,x):
		pass



# root.geometry("500x300")
app = Quiz()


#npm i nodemom
# ternary operator