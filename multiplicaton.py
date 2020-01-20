 #using for loop  2nd class
b =int(input("Enter the block: "));
g=int(input("Enter the group: "))
start_value=int(input("Enter the starting value: "))
for x in range(1,b+1):
	for i in range(start_value,g+1):
		print(x,"*", i ,"=", x*i)
		if i ==g:
			print("...................")
	#print(%d time %x)
	#for y in range(b,g):	
	#print(x*2)
	#using while loop 3rd class
	