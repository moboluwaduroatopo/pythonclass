class Myapp:
	def __init__(self,name,age):
		self.course=''
		self.name=name
		self.age=age
		# self.addition()
		self.printname()

	def printname(self):
	# def addition(self):
		print(self.name, self.age)
	def printcourse(self,course,name):
		self.course=course
		self.name=name
		print(self.course,self.name)

mp = Myapp('tawa', 20)
# mp.addition()
mp.printcourse('python','adio')		
