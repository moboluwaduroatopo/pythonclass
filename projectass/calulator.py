from tkinter import *
import  math
class Gui():
	def __init__(self):
		self.root=Tk()
		self.root.title('GUI example')
		self.root.resizable(0,0)
		self.ans= StringVar()
		self.op= StringVar()
		

		self.ans1=Entry(self.root,font=('arial',20,'bold'), textvariable=self.ans,bd=30,insertwidth=4,bg="powder blue",justify='right')
		self.ans1.grid(columnspan=5)
		self.ans1.focus()

		self.Sqroot=Button(self.root,padx=16,bd=8,fg='black',font=('arial',13,'bold'),text="√",bg="powder blue",command=lambda:self.operateSqroot('√'))
		self.Sqroot.grid(row=3, column=0)

		self.sq=Button(self.root,padx=16,bd=8,fg='black',font=('arial',13,'bold'),text="X*2",bg="powder blue",command=lambda:self.operateSq('sq'))
		self.sq.grid(row=3, column=1)

		self.per=Button(self.root,padx=16,bd=8,fg='black',font=('arial',13,'bold'),text="%",bg="powder blue",command=lambda:self.operate('%'))
		self.per.grid(row=3, column=2)

		self.oneD=Button(self.root,padx=16,bd=8,fg='black',font=('arial',13,'bold'),text="1/x",bg="powder blue",command=lambda:self.operateoneD(''))
		self.oneD.grid(row=3, column=3)

		self.mod=Button(self.root,padx=16,bd=8,fg='black',font=('arial',13,'bold'),text="±",bg="powder blue",command=lambda:self.numb('-'))
		self.mod.grid(row=3, column=4)

		self.log=Button(self.root,padx=16,bd=8,fg='black',font=('arial',13,'bold'),text="log",bg="powder blue",command=lambda:self.operateLog('In'))
		self.log.grid(row=4, column=0)

		self.pie=Button(self.root,padx=16,bd=8,fg='black',font=('arial',13,'bold'),text="π",bg="powder blue",command=lambda:self.operatePie('π'))
		self.pie.grid(row=4, column=1)

		self.sin=Button(self.root,padx=16,bd=8,fg='black',font=('arial',13,'bold'),text="sin",bg="powder blue",command=lambda:self.operateSin('sin'))
		self.sin.grid(row=4, column=2)

		self.cos=Button(self.root,padx=16,bd=8,fg='black',font=('arial',13,'bold'),text="cos",bg="powder blue",command=lambda:self.operateCos('cos'))
		self.cos.grid(row=4, column=3)

		self.tan=Button(self.root,padx=16,bd=8,fg='black',font=('arial',13,'bold'),text="tan",bg="powder blue",command=lambda:self.operateTan('tan'))
		self.tan.grid(row=4, column=4)

		self.num7=Button(self.root,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text="7",bg="powder blue",command=lambda:self.numb(7))
		self.num7.grid(row=5, column=0)

		self.num8=Button(self.root,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text="8",bg="powder blue",command=lambda:self.numb(8))
		self.num8.grid(row=5, column=1)

		self.num9=Button(self.root,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text="9",bg="powder blue",command=lambda:self.numb(9))
		self.num9.grid(row=5, column=2)

		self.dell=Button(self.root,padx=16,bd=8,fg='black',font=('arial',13,'bold'),text="DEL",bg="powder blue",command=lambda:self.ndel(''))
		self.dell.grid(row=5, column=3)

		self.on=Button(self.root,padx=16,bd=8,fg='black',font=('arial',13,'bold'),text="AC",bg="powder blue",command=lambda:self.onn('AC'))
		self.on.grid(row=5, column=4)

		self.num4=Button(self.root,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text="4",bg="powder blue",command=lambda:self.numb(4))
		self.num4.grid(row=6, column=0)

		self.num5=Button(self.root,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text="5",bg="powder blue",command=lambda:self.numb(5))
		self.num5.grid(row=6, column=1)

		self.num6=Button(self.root,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text="6",bg="powder blue",command=lambda:self.numb(6))
		self.num6.grid(row=6, column=2)

		self.muti=Button(self.root,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text="*",bg="powder blue", command=lambda:self.operate('*'))
		self.muti.grid(row=6, column=3)

		self.divi=Button(self.root,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text="/",bg="powder blue",command=lambda:self.operate('/'))
		self.divi.grid(row=6, column=4)

		self.num3=Button(self.root,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text="3",bg="powder blue",command=lambda:self.numb(3))
		self.num3.grid(row=7, column=0)

		self.num2=Button(self.root,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text="2",bg="powder blue",command=lambda:self.numb(2))
		self.num2.grid(row=7, column=1)

		self.num1=Button(self.root,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text="1",bg="powder blue",command=lambda:self.numb(1))
		self.num1.grid(row=7, column=2)

		self.plus=Button(self.root,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text="+",bg="powder blue", command=lambda:self.operate('+'))
		self.plus.grid(row=7, column=3)

		self.min=Button(self.root,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text="-",bg="powder blue", command=lambda:self.operate('-'))
		self.min.grid(row=7, column=4)

		self.zero=Button(self.root,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text="0",bg="powder blue",command=lambda:self.numb(0))
		self.zero.grid(row=8, column=0)

		self.dot=Button(self.root,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text=".",bg="powder blue",command=lambda:self.numb('.'))
		self.dot.grid(row=8, column=1)

		self.ten=Button(self.root,padx=16,bd=8,fg='black',font=('arial',13,'bold'),text="10*X",bg="powder blue",command=lambda:self.operateTen(1))
		self.ten.grid(row=8, column=2)

		self.equ=Button(self.root,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text="=",bg="powder blue", command=self.calculate)
		self.equ.grid(row=8, column=3)


		self.num=""
		self.ope=""
		self.c=""
		self.val1=self.val2=0
		self.root.mainloop()
	def calculate(self):
		self.val2=float(self.ans1.get())
		print(self.val2)
		self.ans.set("")
		if self.ope == '+':
			self.ans.set(self.val1 + self.val2)
		elif(self.ope == '-'):
			self.ans.set(self.val1 - self.val2)
		elif(self.ope =='*'):
			self.ans.set(self.val1 * self.val2)
		elif(self.ope== '/'):
			self.ans.set(self.val1 / self.val2)
		elif(self.ope== '%'):
			self.ans.set(self.val1 % self.val2)	
	def operateSin(self,a):
		self.val1=float(self.ans1.get())
		self.ans.set(math.sin((self.val1)*(math.pi/180)) )
		print(self.val1)
	def operateCos(self,a):
		self.val1=float(self.ans1.get())
		self.ans.set(math.cos((self.val1)*(math.pi/180)) )
		print(self.val1)
	def operateTan(self,a):
		self.val1=float(self.ans1.get())
		self.ans.set(math.tan((self.val1)*(math.pi/180)) )
		print(self.val1)
	def operateLog(self,a):
		self.val1=float(self.ans1.get())
		self.ans.set(math.log10(self.val1) )
		print(self.val1)
		
	def operatePie(self,a):
		# self.val1=float(self.ans1.get())
		self.ans.set(math.pi)
		# print(self.val1)Math.pow(10,result.value)
	def operateTen(self,a):
		self.val1=float(self.ans1.get())
		self.ans.set(math.pow(10,self.val1) )
		print(self.val1)
	def operateSqroot(self,a):
		self.val1=float(self.ans1.get())
		self.ans.set(math.sqrt(self.val1) )
		print(self.val1)
	def operateoneD(self,a):
		self.val1=float(self.ans1.get())
		self.ans.set(1/self.val1 )
		print(self.val1)
	def operateSq(self,a):
		self.val1=float(self.ans1.get())
		self.ans.set(math.pow(self.val1,2) )
		print(self.val1)
		
			
			
			
			
				
			
		
		
	def operate(self,x):
		# print(x)
		# self.op.set(x)
		self.ope=x
		print(self.ope)
		self.val1=float(self.ans1.get())
		self.ans.set("")
		self.num=""
		# self.num=""
		print(self.val1)
		# self.val2=float(self.entry.get())
	def ndel(self,m):
		self.ans.set("")
		self.num=""
	def onn(self,m):
		on=self.ans.set("0")
		self.num=""
	def numb(self,numbers):
		on=""
		self.num+=str(numbers)
		# print(self.num)
		self.ans.set(self.num)
		

Gui()


# import math
# firstNumber = float(input())
# op = input().lower()
# secondNumber = float(input())

# if op == "+":
#     print (firstNumber, "+", secondNumber, "=", firstNumber + secondNumber )
# elif op == "-": 
#     print (firstNumber, "-", secondNumber, "=", firstNumber - secondNumber )
# elif op == "*":
#     print (firstNumber, "*", secondNumber, "=", firstNumber * secondNumber )
# elif op == "/":
#     print (firstNumber, "/", secondNumber, "=", firstNumber / secondNumber )
# elif op == "^":
#     print (firstNumber, "^", secondNumber, "=", firstNumber ** secondNumber )
# elif op == "r":
#     print (firstNumber, "root", secondNumber, "=", secondNumber ** (1 / firstNumber) )
# elif op == "%":
#     print (firstNumber, "%", secondNumber, "=", firstNumber % secondNumber )
# #factorial
# elif op == "!":
#     theNumber = firstNumber = secondNumber 
#     secondNumber = 1
#     while firstNumber > 1:
#         secondNumber *= firstNumber 
#         firstNumber = firstNumber - 1  
#     print ("n!(", theNumber, ")=", secondNumber )
# elif op == "sin":
#     print ("sin(", secondNumber, ")=", math.sin((secondNumber )*(math.pi/180)))
# elif op == "cos":
#     print ("cos(", secondNumber, ")=", math.cos((secondNumber )*(math.pi/180)))
# elif op == "tan":
#     print ("tan(", secondNumber, ")=", math.tan(secondNumber ))
# elif op == "pie" or op == "pi":
#     print ("Pie =", math.pi)
# elif op == "e":
#     print = ("E =", math.e)
# elif op == "ln":
#     print ("ln(", secondNumber , ")= ", math.log(secondNumber))
# else:
#     print ("incorrect operator") 