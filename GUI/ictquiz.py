from tkinter import *
import json
from tkinter.messagebox import *
import mysql.connector
class Quiz():
	def __init__(self, master):
		# self.root=Tk()
		master.title('ICT Quiz')
		master.resizable(0,0)
		self.qindex=0;
		self.qn = 0
		self.ans= StringVar()
		self.results= StringVar()
		self.opt_selected= StringVar()
		# val1=self.congroup.get()
		self.mycon=mysql.connector.connect(host="localhost",user='root',passwd='',database='pythoncbt_db')
# print(mycon)
		self.mycursor=self.mycon.cursor()

# 		self.sql="INSERT INTO question (q_name,optiona,optionb,optionc,optiond,ans) VALUES(%s,%s,%s,%s,%s,%s)"
# 		self.val=[("What is the verb to weep in the first person singular future simple tense1?", "I will weep","I will have wept","I  will be weeping","I will have been weeping","I will weep"),("What is the verb to weep in the first person singular future simple tense2?", "I will weep2","I will have wept2","I  will be weeping2","I will have been weeping2","I will weep2"),("What is the verb to weep in the first person singular future simple tense1?3", "I will weep3","I will have wept3","I  will be weeping3","I will have been weeping3","I will weep3"),("What is the verb to weep in the first person singular future simple tense4?", "I will weep4","I will have wept4","I  will be weeping4","I will have been weeping4","I will weep4")]
# # mycursor.execute(sql, val)
# 		self.mycursor.executemany(self.sql,self.val)
# 		self.mycon.commit()
# 		print(self.mycursor.rowcount,'record inserted successfuly')
		self.mycursor.execute("SELECT * FROM question")

		self.y= self.mycursor.fetchall()
		# print(self.yy[self.qn][0])
# for x in myresult:
#   print(x)
		# self.x = '[{"q_name": "What is the verb to weep in the first person singular, future simple tense1?", "optiona": "I will weep","optionb":"I will have wept","optionc":"I  will be weeping","optiond":"I will have been weeping","ans":"I will weep"},{"q_name": "What is the verb to weep in the first person singular, future simple tense2?", "optiona": "I will weep1","optionb":"I will have wept1","optionc":"I  will be weeping1","optiond":"I will have been weeping1","ans":"I will weep"},{"q_name": "What is the verb to weep in the first person singular, future simple tense?", "optiona": "I will weep","optionb":"I will have wept","optionc":"I  will be weeping","optiond":"I will have been weeping","ans":"I will weep"}]'
		# self.y = json.loads(self.x)
		# self.y = json.loads(self.x)
		# print(len(self.y))
		self.a=self.y[self.qn]
		print(self.a)
		self.ops=[self.a[2],self.a[3],self.a[4],self.a[5]]
		# print(self.ops)
		self.correct = 0
		

		self.ques = self.create_q(master, self.qn)
		self.opts = self.create_options(master,4)
		# self.opts2 = self.anything(master,4)
		
		self.display_q(self.qn)
		self.button = Button(master, text="Next", command=self.next_btn)
		self.button.pack(side=TOP)
		self.button = Button(master, text="Back", command=self.back)
		self.button.pack(side=TOP)
		self.result=Label(master, textvariable=self.results)
		self.result.pack(side=TOP, anchor="w")
		
	
	# def result(self,master):
		
# the result is a Python dictionary:
		# print(self.y['model'])
				# print(self.a['model'])
				# print(self.a['mpg']
	def create_q(self,master,qn):
		self.lab=Label(master, text=self.a[1])
		self.lab.pack(side=TOP, anchor="w")
		return  self.lab
	def create_options(self,master,n):
		# print(n)
		b_val = 0
		b = []
		while b_val < n:
			# print(b_val+1)
			# print(n)
			# print('here')
			btn = Radiobutton(master, text="foo", variable=self.opt_selected, value=b_val+1)
			b.append(btn)
			btn.pack(side=TOP, anchor="w")
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
		self.results.set(self.result)
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


root = Tk()
root.geometry("500x300")
app = Quiz(root)
root.mainloop()

#npm i nodemom
# ternary operator