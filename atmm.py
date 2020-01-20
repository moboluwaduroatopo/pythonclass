print('Welcome to python ATM machine')
restart=('Y')
chances = 3
balance = 260.14
# regpin=''
while chances >=0:
	pin =int(input('Please Enter Your 4 Digit Pin:'))
	if pin == pin:
		print('You entered you pin Correctly\n')
		while restart not in ('n','no','No','N'):
			print('Please Press 1 For Your Balance\n')
			print('Please Press 2 To Make a Withdraw\n')
			print('Please Press 3 To Pay in\n')
			# print('Please Press 4 To Return Card\n')
			print('Please Press 4 To recharge\n')
			print('Please Press 5 To change pin\n')
			# recharge change pin
			option = int(input('What Would you like to choose?'))
			if option == 1:
				print('Your Balance is #', balance)
				restart = input('Would You you like to go back? ')
				if restart in ('n','no','No','N'):
					print('Thank You for Banking with us')
					break
			if option ==2:
				# print('How Much Would u like Withdraw?')
				# option2 = ('y')
				withdraw = float(input('How Much Would u like Withdraw? \n#10/#20/#40/#60/#80/#100  for other enter 1:'))
				if balance <=withdraw:
					print('Insufficient balance')
				elif withdraw in [10,20,40,60,80,100]:
					balance=balance - withdraw
					print('Your balance is #',balance)
					restart=input('Would You you like to go back? ')
					if restart in ('n','no','No','N'):
						print('Thank You for Banking with us')
						break	
				
					
				elif withdraw != [10,20,40,60,80,100]:
					print('Invalid Amount, Please Re-try')
					restart=('y')
					if withdraw == 1:
						withdraw=float(input('Please Enter Desired amount:'))
						if balance <= withdraw:  
							print('Insufficient balance')
						else:	

							balance=balance - withdraw
							print('Your balance is #',balance)
			if option == 3:	
				payin=float(input('How Much Would You like To pay In?'))
				balance=balance + payin
				print('Your new Balance is #',balance)
				restart=input('Would You you like to go back? ')
				if restart in ('n','no','No','N'):
					print('Thank You for Banking with u')
					break

			if option == 4:
				number=float(input('Please enter Your number:'))
				amount=float(input('Please enter the amount :'))
				if balance <=amount:
					print('Insufficient balance')
				else:	
					balance=balance - amount
					print('Your balance is #',balance)
					print(amount,'Successful recharge to your number',number )
					restart=input('Would You you like to go back? ')
					if restart in ('n','no','No','N'):
						print('Thank You for Banking with u')
						break

                	
	elif pin != pin:
		print('Incorrect Password')
		chances = chances - 1
		if chances == 0:
			print('\nNo more tries')
			break