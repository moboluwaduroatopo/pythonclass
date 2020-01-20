# class Human():
# 	no_of_eyes=2
# 	no_of_legs=2
# 	skin_color="black"
# 	def walk(this,speed):
# 		if this.no_of_legs == 2:
# 			if speed>0:
# 				print("I am walking")
# 		elif this.no_of_legs>0:
# 				if speed>0:
# 					print("i am leeping")
# 	def bleach(this):
# 		this.skin_color="white"
						
# titi =Human()
# tawa= Human()
# print("Titi is",titi.skin_color)
# print("Tawa",tawa.skin_color)
# tawa.bleach()
# tawa.walk(5)
# print(tawa.skin_color)
# print(titi.skin_color)

# class SuperHuman(Human):
# 	def fly():
# 		s= SuperHuman()
# 		s.walk()
# 		s.fly()
# 		tawa.fly()
		
	# contractor in python
class Parent:
	def __init__(self):
		self.name="parent"
		self.leg=2 
		self.eye=2
		self.mouth=1
		self.hand=2
		self.complexion="dark"
		self.height="tall"
		self.speed=""
	def walk(self):
		self.speed=input('enter speed between 1 and 2')
		if self.speed == '1':
			print(self.name+ " is walking")
		elif(self.speed == '2'):
			print(self.name+ " is running")
		else:
			print("invalid speed number")
	def talk(self):
		print(self.name + "is talking now please listen")
	def parentDetails(self):
		print("parent is "+self.complexion+" in complexion and is " +self.height)
# class Child(Parent):
# 	def __init__(self):
# 		self.complexion="light"
# 		self.name="child"
# 		super().__init__()
# ch=Child()
# ch.complexion='light'
# # self.complexion="light"
# ch.parentDetails()
# ch.talk()		